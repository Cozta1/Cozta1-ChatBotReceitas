"""
dados.py — Dados estaticos do ChefBot.

Contem:
  - DADOS_TREINO   : exemplos rotulados para treinar o classificador Naive Bayes
  - SAUDACOES      : respostas variaveis para saudacoes
  - DESPEDIDAS     : respostas variaveis para despedidas
  - AGRADECIMENTOS : respostas variaveis para agradecimentos
  - AJUDA          : texto fixo do menu de ajuda
"""

# ============================================================
# Dados de treino para o classificador de intencoes
# (CountVectorizer + MultinomialNB — Intencao.py)
# ============================================================

DADOS_TREINO = [
    # ----------------------------------------------------------
    # saudacao
    # ----------------------------------------------------------
    ("oi",                  "saudacao"),
    ("ola",                 "saudacao"),
    ("hey",                 "saudacao"),
    ("eai",                 "saudacao"),
    ("bom dia",             "saudacao"),
    ("boa tarde",           "saudacao"),
    ("boa noite",           "saudacao"),
    ("salve",               "saudacao"),
    ("fala",                "saudacao"),
    ("hello",               "saudacao"),
    ("tudo bem",            "saudacao"),
    ("como vai",            "saudacao"),
    ("ola tudo bom",        "saudacao"),
    ("eai tudo certo",      "saudacao"),

    # ----------------------------------------------------------
    # despedida
    # ----------------------------------------------------------
    ("tchau",               "despedida"),
    ("ate mais",            "despedida"),
    ("ate logo",            "despedida"),
    ("bye",                 "despedida"),
    ("flw",                 "despedida"),
    ("falou",               "despedida"),
    ("adeus",               "despedida"),
    ("xau",                 "despedida"),
    ("vou indo",            "despedida"),
    ("vou embora",          "despedida"),
    ("vou sair agora",      "despedida"),

    # ----------------------------------------------------------
    # agradecimento
    # ----------------------------------------------------------
    ("obrigado",            "agradecimento"),
    ("obrigada",            "agradecimento"),
    ("valeu",               "agradecimento"),
    ("brigado",             "agradecimento"),
    ("brigada",             "agradecimento"),
    ("thanks",              "agradecimento"),
    ("muito obrigado",      "agradecimento"),
    ("grato",               "agradecimento"),
    ("legal valeu",         "agradecimento"),
    ("agradeco",            "agradecimento"),
    ("gratidao",            "agradecimento"),

    # ----------------------------------------------------------
    # ajuda
    # ----------------------------------------------------------
    ("ajuda",               "ajuda"),
    ("help",                "ajuda"),
    ("como funciona",       "ajuda"),
    ("o que voce faz",      "ajuda"),
    ("comandos",            "ajuda"),
    ("menu",                "ajuda"),
    ("quais opcoes",        "ajuda"),
    ("como usar",           "ajuda"),
    ("o que posso fazer",   "ajuda"),
    ("me ajuda",            "ajuda"),
    ("preciso de ajuda",    "ajuda"),
    ("nao sei usar",        "ajuda"),

    # ----------------------------------------------------------
    # receita_aleatoria
    # ----------------------------------------------------------
    ("receita aleatoria",           "receita_aleatoria"),
    ("qualquer receita",            "receita_aleatoria"),
    ("receita surpresa",            "receita_aleatoria"),
    ("sugestao de receita",         "receita_aleatoria"),
    ("sugira uma receita",          "receita_aleatoria"),
    ("sorteia uma receita",         "receita_aleatoria"),
    ("me surpreenda",               "receita_aleatoria"),
    ("escolha por mim",             "receita_aleatoria"),
    ("me da uma receita",           "receita_aleatoria"),
    ("random",                      "receita_aleatoria"),
    ("surpresa",                    "receita_aleatoria"),
    ("aleatoria",                   "receita_aleatoria"),
    ("sorteia",                     "receita_aleatoria"),
    ("sugere algo",                 "receita_aleatoria"),
    ("qualquer coisa para comer",   "receita_aleatoria"),

    # ----------------------------------------------------------
    # categoria:sobremesa
    # ----------------------------------------------------------
    ("quero uma sobremesa",     "categoria:sobremesa"),
    ("receita de sobremesa",    "categoria:sobremesa"),
    ("tem algum doce",          "categoria:sobremesa"),
    ("receita de bolo",         "categoria:sobremesa"),
    ("quero um pudim",          "categoria:sobremesa"),
    ("algo doce",               "categoria:sobremesa"),
    ("brigadeiro",              "categoria:sobremesa"),
    ("sobremesa",               "categoria:sobremesa"),
    ("torta",                   "categoria:sobremesa"),
    ("receita doce",            "categoria:sobremesa"),
    ("doce para sobremesa",     "categoria:sobremesa"),

    # ----------------------------------------------------------
    # categoria:prato principal
    # ----------------------------------------------------------
    ("receita de almoco",           "categoria:prato principal"),
    ("o que fazer para almoco",     "categoria:prato principal"),
    ("prato principal",             "categoria:prato principal"),
    ("receita para jantar",         "categoria:prato principal"),
    ("comida",                      "categoria:prato principal"),
    ("almoco",                      "categoria:prato principal"),
    ("jantar",                      "categoria:prato principal"),
    ("refeicao",                    "categoria:prato principal"),
    ("prato do dia",                "categoria:prato principal"),
    ("janta",                       "categoria:prato principal"),
    ("prato quente",                "categoria:prato principal"),

    # ----------------------------------------------------------
    # categoria:lanche
    # ----------------------------------------------------------
    ("receita de lanche",   "categoria:lanche"),
    ("quero um salgado",    "categoria:lanche"),
    ("tem tapioca",         "categoria:lanche"),
    ("receita de coxinha",  "categoria:lanche"),
    ("lanche rapido",       "categoria:lanche"),
    ("lanche",              "categoria:lanche"),
    ("salgadinho",          "categoria:lanche"),
    ("sanduiche",           "categoria:lanche"),
    ("petisco",             "categoria:lanche"),
    ("coxinha",             "categoria:lanche"),
    ("pao de queijo",       "categoria:lanche"),

    # ----------------------------------------------------------
    # categoria:bebida
    # ----------------------------------------------------------
    ("receita de suco",     "categoria:bebida"),
    ("quero uma bebida",    "categoria:bebida"),
    ("tem drink",           "categoria:bebida"),
    ("vitamina de fruta",   "categoria:bebida"),
    ("receita de limonada", "categoria:bebida"),
    ("bebida",              "categoria:bebida"),
    ("suco",                "categoria:bebida"),
    ("vitamina",            "categoria:bebida"),
    ("limonada",            "categoria:bebida"),
    ("quentao",             "categoria:bebida"),
    ("algo para beber",     "categoria:bebida"),

    # ----------------------------------------------------------
    # categoria:acompanhamento
    # ----------------------------------------------------------
    ("receita de farofa",       "categoria:acompanhamento"),
    ("quero um acompanhamento", "categoria:acompanhamento"),
    ("tem salada",              "categoria:acompanhamento"),
    ("receita de pure",         "categoria:acompanhamento"),
    ("acompanhamento",          "categoria:acompanhamento"),
    ("farofa",                  "categoria:acompanhamento"),
    ("salada",                  "categoria:acompanhamento"),
    ("pure",                    "categoria:acompanhamento"),
    ("vinagrete",               "categoria:acompanhamento"),
    ("acompanha o prato",       "categoria:acompanhamento"),

    # ----------------------------------------------------------
    # buscar_por_ingredientes
    # ----------------------------------------------------------
    ("tenho frango",                            "buscar_por_ingredientes"),
    ("tenho ovos e queijo",                     "buscar_por_ingredientes"),
    ("o que fazer com batata",                  "buscar_por_ingredientes"),
    ("tenho leite condensado",                  "buscar_por_ingredientes"),
    ("posso fazer com frango e alho",           "buscar_por_ingredientes"),
    ("o que posso cozinhar com arroz",          "buscar_por_ingredientes"),
    ("tenho cebola e alho em casa",             "buscar_por_ingredientes"),
    ("o que fazer com macarrao",                "buscar_por_ingredientes"),
    ("tenho banana e ovo",                      "buscar_por_ingredientes"),
    ("usar frango e batata",                    "buscar_por_ingredientes"),
    ("preparar algo com ovo",                   "buscar_por_ingredientes"),
    ("tenho bacon e linguica",                  "buscar_por_ingredientes"),
    ("como usar feijao preto",                  "buscar_por_ingredientes"),
    ("tenho frango cebola alho",                "buscar_por_ingredientes"),
    ("o que preparo com esses ingredientes",    "buscar_por_ingredientes"),
    ("tenho so esses ingredientes",             "buscar_por_ingredientes"),
    ("receita com frango",                      "buscar_por_ingredientes"),
    ("fazer com leite e ovo",                   "buscar_por_ingredientes"),

    # ----------------------------------------------------------
    # buscar_por_nome
    # ----------------------------------------------------------
    ("receita de feijoada",             "buscar_por_nome"),
    ("como fazer estrogonofe",          "buscar_por_nome"),
    ("quero fazer frango xadrez",       "buscar_por_nome"),
    ("tem receita de bolo de cenoura",  "buscar_por_nome"),
    ("busca feijoada",                  "buscar_por_nome"),
    ("me mostra a receita de arroz",    "buscar_por_nome"),
    ("quero a receita de coxinha",      "buscar_por_nome"),
    ("como se faz limonada",            "buscar_por_nome"),
    ("procura receita de pudim",        "buscar_por_nome"),
    ("me da a receita de moqueca",      "buscar_por_nome"),
    ("receita de farofa",               "buscar_por_nome"),
    ("como preparar feijao tropeiro",   "buscar_por_nome"),
]


# ============================================================
# Respostas estaticas com variacao
# ============================================================

SAUDACOES = [
    (
        "Ola! Sou o ChefBot, seu assistente de receitas culinarias!\n"
        "Me diga quais ingredientes voce tem ou peca uma receita por categoria.\n"
        "Dica: use 'ajuda' para ver todas as opcoes."
    ),
    (
        "Fala! Sou o ChefBot e estou pronto para ajudar na cozinha!\n"
        "Pode me contar o que tem na geladeira ou pedir uma receita especifica.\n"
        "Dica: use 'ajuda' para ver todos os comandos."
    ),
    (
        "Boa! ChefBot aqui, especialista em receitas brasileiras!\n"
        "Me conte os ingredientes que voce tem ou escolha uma categoria.\n"
        "Dica: digite 'ajuda' para saber mais."
    ),
]

DESPEDIDAS = [
    "Tchau! Bom apetite e ate a proxima!",
    "Ate mais! Espero ter ajudado na cozinha!",
    "Ate logo! Que o seu prato fique uma delicia!",
]

AGRADECIMENTOS = [
    "De nada! Espero que a receita fique otima!",
    "Por nada! Qualquer duvida sobre receitas, e so chamar!",
    "Disponha! Bom apetite!",
]

AJUDA = (
    "Veja o que posso fazer por voce:\n\n"
    "  - INGREDIENTES: Me diga o que voce tem e sugiro receitas.\n"
    "    Exemplo: 'Tenho frango, alho e cebola'\n\n"
    "  - NOME: Busque uma receita pelo nome.\n"
    "    Exemplo: 'Receita de feijoada' ou 'Como fazer estrogonofe'\n\n"
    "  - CATEGORIA: Peca receitas de uma categoria especifica.\n"
    "    Opcoes: prato principal, sobremesa, lanche, bebida, acompanhamento\n"
    "    Exemplo: 'Quero uma sobremesa' ou 'Me sugere um lanche'\n\n"
    "  - ALEATORIA: Peca uma receita surpresa.\n"
    "    Exemplo: 'Me da uma receita aleatoria' ou 'Sorteia uma receita'\n\n"
    "  - SAIR: Digite 'sair' para encerrar o chat."
)
