import random
import string
import unicodedata

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from receitas import RECEITAS
from dados import DADOS_TREINO, SAUDACOES, DESPEDIDAS, AGRADECIMENTOS, AJUDA

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

lemmatizer = WordNetLemmatizer()
stopwords_pt = set(stopwords.words('portuguese'))


def norm(texto):
    sem_acento = unicodedata.normalize('NFKD', texto.lower())
    return ''.join(c for c in sem_acento if not unicodedata.combining(c))


def tokenizar(texto, filtrar_stopwords=False):
    tokens = [
        t for t in word_tokenize(norm(texto), language='portuguese')
        if t not in string.punctuation and len(t) > 1
    ]
    if filtrar_stopwords:
        tokens = [t for t in tokens if t not in stopwords_pt]
    return [lemmatizer.lemmatize(t, pos='v') for t in tokens]

# Classificador
frases_treino = [" ".join(tokenizar(f)) for f, _ in DADOS_TREINO]
labels_treino = [label for _, label in DADOS_TREINO]
vectorizer = CountVectorizer()
classificador = MultinomialNB()
classificador.fit(vectorizer.fit_transform(frases_treino), labels_treino)


def detectar_intencao(tokens):
    if not tokens:
        return "buscar_por_ingredientes"
    texto_proc = " ".join(tokens)
    if not texto_proc.strip():
        return "buscar_por_ingredientes"
    vetor = vectorizer.transform([texto_proc])
    prob = classificador.predict_proba(vetor)[0]
    if prob.max() < prob.mean() * 1.5:
        return "buscar_por_ingredientes"
    return classificador.predict(vetor)[0]

# Busca ingredientes
def batem(ing_norm, ings_norm):
    partes_r = [p for p in ing_norm.split() if len(p) > 2]
    if not partes_r:
        return False
    for ing_u in ings_norm:
        partes_u = [p for p in ing_u.split() if len(p) > 2]
        for pu in partes_u:
            if any(pu in pr or pr in pu for pr in partes_r):
                return True
    return False


def extrair_ingredientes(tokens):
    texto = " ".join(tokens)
    encontrados = []
    for receita in RECEITAS:
        for ing in receita["ingredientes"]:
            partes = [p for p in norm(ing).split() if len(p) > 2]
            if any(p in texto for p in partes) and ing not in encontrados:
                encontrados.append(ing)
    return encontrados


def buscar_receitas(ingredientes):
    ings_norm = [norm(i) for i in ingredientes]
    total_usuario = len(ings_norm)
    resultados = []

    for receita in RECEITAS:
        ings_r = receita["ingredientes"]
        match_r = sum(1 for ing in ings_r if batem(norm(ing), ings_norm))
        if not match_r:
            continue
        match_u = sum(1 for iu in ings_norm if batem(iu, [norm(i) for i in ings_r]))
        cobertura_r = match_r / len(ings_r)
        cobertura_u = match_u / total_usuario if total_usuario else 0
        score = (2 * cobertura_r * cobertura_u / (cobertura_r + cobertura_u)) if (cobertura_r + cobertura_u) else 0
        resultados.append((receita, score, match_r))

    resultados.sort(key=lambda x: (-x[1], -x[2]))
    return resultados[:3]


def buscar_por_nome(texto):
    palavras = [p for p in norm(texto).split() if len(p) > 2]
    resultados = []
    for receita in RECEITAS:
        nome_palavras = [p for p in norm(receita["nome"]).split() if len(p) > 2]
        score = sum(1 for p in nome_palavras if any(p in u or u in p for u in palavras))
        if score:
            resultados.append((receita, score))
    resultados.sort(key=lambda x: -x[1])
    return [r for r, _ in resultados[:3]]


def buscar_por_categoria(categoria):
    return [r for r in RECEITAS if r["categoria"] == categoria]

# Formatacao
def formatar_receita(receita):
    linha = "=" * 44
    info = f"  Tempo: {receita['tempo']} | Porcoes: {receita['porcoes']} | {receita['categoria'].title()}"
    ingredientes = "\n".join(f"    - {ing.capitalize()}" for ing in receita["ingredientes"])
    instrucoes = "\n".join(f"    {i+1}. {p}" for i, p in enumerate(receita["instrucoes"]))
    return (
        f"\n{linha}\n"
        f"  {receita['nome'].upper()}\n"
        f"{linha}\n"
        f"{info}\n\n"
        f"  INGREDIENTES:\n{ingredientes}\n\n"
        f"  MODO DE PREPARO:\n{instrucoes}\n"
        f"{linha}"
    )


def gerar_resposta(mensagem):
    tokens = tokenizar(mensagem, filtrar_stopwords=True)
    intencao = detectar_intencao(tokens)

    if not tokens:
        return "Nao entendi. Tente listar ingredientes ou use 'ajuda'."

    if intencao == "saudacao":
        return random.choice(SAUDACOES)
    if intencao == "despedida":
        return random.choice(DESPEDIDAS)
    if intencao == "agradecimento":
        return random.choice(AGRADECIMENTOS)
    if intencao == "ajuda":
        return AJUDA

    if intencao == "buscar_por_nome":
        resultados = buscar_por_nome(mensagem)
        if resultados:
            resposta = f"Encontrei {len(resultados)} receita(s) pelo nome:\n"
            for r in resultados:
                resposta += formatar_receita(r) + "\n"
            return resposta.rstrip()
        return "Nao encontrei receita com esse nome.\nTente ser mais especifico ou use 'ajuda'."

    if intencao == "receita_aleatoria":
        return f"Receita sorteada para voce!{formatar_receita(random.choice(RECEITAS))}"

    if intencao.startswith("categoria:"):
        categoria = intencao.split(":", 1)[1]
        receitas_cat = buscar_por_categoria(categoria)
        if not receitas_cat:
            return f"Nao encontrei receitas na categoria '{categoria}'."
        resposta = f"Aqui estao ate 3 opcoes de {categoria.title()}:\n"
        for r in receitas_cat[:3]:
            resposta += formatar_receita(r) + "\n"
        return resposta.rstrip()

    
    ingredientes = extrair_ingredientes(tokens)
    if ingredientes:
        resultados = buscar_receitas(ingredientes)
        if resultados:
            resposta = f"Ingredientes detectados: {', '.join(ingredientes)}\n"
            resposta += f"Top {len(resultados)} receita(s) mais compativeis:\n"
            for r, score, match_count in resultados:
                resposta += f"\n  [Compatibilidade: {int(score*100)}% | {match_count} ingrediente(s)]{formatar_receita(r)}\n"
            return resposta.rstrip()


    resultados = buscar_receitas(tokens)
    if resultados:
        resposta = "Possivelmente voce quer receitas com esses ingredientes:\n"
        for r, _, _ in resultados:
            resposta += formatar_receita(r) + "\n"
        return resposta.rstrip()

    return (
        "Nao encontrei receitas com o que voce descreveu.\n"
        "Tente listar ingredientes como: 'Tenho frango, arroz e alho'.\n"
        "Use 'ajuda' para ver todas as opcoes disponiveis."
    )


def main():
    print("=" * 50)
    print("  CHEFBOT - Seu Assistente de Receitas")
    print("  Digite 'sair' para encerrar")
    print("=" * 50)
    print(f"\nChefBot: {AJUDA}\n")

    while True:
        entrada = input("Voce: ").strip()
        if not entrada:
            continue
        if entrada.lower() in ('sair', 'exit', 'quit'):
            print("\nChefBot: Tchau! Bom apetite!")
            break
        print(f"\nChefBot: {gerar_resposta(entrada)}\n")


if __name__ == '__main__':
    main()
