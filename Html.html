<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lista de tarefas</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">


</head>
<body>
<div class="container">

<h1>Lista de tarefas</h1>

<div id="inicio">
    <button id="iniciarBtn" class="btn">Iniciar lista de tarefas</button>
</div>

<div id="lista" class="hidden">
    <div class="formulario">
        <input id="novaTarefa" type="text" placeholder="Digite uma tarefa">
        <input id="categoriaTarefa" type="text" placeholder="Categoria (opcional)">
        <button id="adicionarBtn" class="btn">Adicionar</button>
    </div>

    <div class="filtros">
        <input id="filtroCategoria" type="text" placeholder="Filtrar por categoria">
        <select id="filtroStatus">
            <option value="">Todos</option>
            <option value="feito">Feitas</option>
            <option value="nao_feito">Não feitas</option>
        </select>
        <button id="filtrarBtn" class="btn">Filtrar</button>
    </div>

    <ul id="taskList"></ul>
</div>
</div>

<script>
const iniciarBtn = document.getElementById("iniciarBtn");
const inicioDiv = document.getElementById("inicio");
const listaDiv = document.getElementById("lista");

const taskList = document.getElementById("taskList");
const novaTarefaInput = document.getElementById("novaTarefa");
const categoriaInput = document.getElementById("categoriaTarefa");
const filtroCategoria = document.getElementById("filtroCategoria");
const filtroStatus = document.getElementById("filtroStatus");

let tarefas = [];
let proximoId = 1;

iniciarBtn.addEventListener("click", () => {
    inicioDiv.classList.add("hidden");
    listaDiv.classList.remove("hidden");
});

function renderizar() {
    taskList.innerHTML = "";
    let filtroCat = filtroCategoria.value.trim().toLowerCase();
    let filtroStat = filtroStatus.value;

    tarefas.forEach(t => {
        if (filtroCat && (!t.categoria || !t.categoria.toLowerCase().includes(filtroCat))) return;
        if (filtroStat === "feito" && !t.feito) return;
        if (filtroStat === "nao_feito" && t.feito) return;

        const li = document.createElement("li");
        li.className = t.feito ? "feito" : "";
        li.dataset.id = t.id;

        const span = document.createElement("span");
        span.textContent = t.categoria ? `${t.descricao} - ${t.categoria}` : t.descricao;

        const divAcoes = document.createElement("div");
        divAcoes.className = "acoes";

        const btnFeito = document.createElement("button");
        btnFeito.className = "btn feitoBtn";
        btnFeito.textContent = t.feito ? "✔" : "Marcar";
        btnFeito.onclick = () => {
            t.feito = !t.feito;
            renderizar();
        };

        const btnRemover = document.createElement("button");
        btnRemover.className = "btn removerBtn";
        btnRemover.textContent = "✖";
        btnRemover.onclick = () => {
            tarefas = tarefas.filter(task => task.id !== t.id);
            renderizar();
        };

        const btnEditar = document.createElement("button");
        btnEditar.className = "btn editarBtn";
        btnEditar.textContent = "Editar";
        btnEditar.onclick = () => {
            const nova = prompt("Edite a tarefa:", t.descricao);
            if (nova && nova.trim() !== "") {
                t.descricao = nova;
                renderizar();
            }
        };

        divAcoes.appendChild(btnFeito);
        divAcoes.appendChild(btnRemover);
        divAcoes.appendChild(btnEditar);

        li.appendChild(span);
        li.appendChild(divAcoes);
        taskList.appendChild(li);
    });
}

// Eventos
document.getElementById("adicionarBtn").addEventListener("click", () => {
    const desc = novaTarefaInput.value.trim();
    if (!desc) return;
    const cat = categoriaInput.value.trim();
    tarefas.push({id: proximoId++, descricao: desc, categoria: cat, feito: false});
    novaTarefaInput.value = "";
    categoriaInput.value = "";
    renderizar();
});

document.getElementById("filtrarBtn").addEventListener("click", () => renderizar());

</script>
</body>
</html>
