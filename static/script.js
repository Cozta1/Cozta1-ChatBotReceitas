function enviar() {
    const input = document.getElementById("msg");
    const mensagem = input.value;

    if (!mensagem) return;

    adicionarMensagem(mensagem, "user");

    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mensagem: mensagem })
    })
    .then(res => res.json())
    .then(data => {
        adicionarMensagem(data.resposta, "bot");
    });

    input.value = "";
}

function adicionarMensagem(texto, tipo) {
    const div = document.createElement("div");
    div.className = "msg " + tipo;
    div.innerText = texto;

    document.getElementById("messages").appendChild(div);
}

document.getElementById("msg").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        enviar();
    }
});