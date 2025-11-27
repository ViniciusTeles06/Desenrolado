from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(_name_)
ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    filtro_categoria = request.args.get("categoria", "")
    filtro_status = request.args.get("status", "")

    tarefas = carregar_tarefas()
    
    # Aplicar filtros
    lista_filtrada = []
    for t in tarefas:
        if filtro_categoria and filtro_categoria.lower() not in t.get("categoria","").lower():
            continue
        if filtro_status == "feito" and not t.get("feito"):
            continue
        if filtro_status == "nao_feito" and t.get("feito"):
            continue
        lista_filtrada.append(t)
    
    return render_template("index.html", tarefas=lista_filtrada, filtro_categoria=filtro_categoria, filtro_status=filtro_status)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    tarefas = carregar_tarefas()
    descricao = request.form.get("tarefa", "").strip()
    categoria = request.form.get("categoria", "").strip()
    if descricao:
        novo_id = str(int(max([t["id"] for t in tarefas], default="0")) + 1) if tarefas else "1"
        tarefas.append({"id": novo_id, "descricao": descricao, "feito": False, "categoria": categoria})
        salvar_tarefas(tarefas)
    return redirect(url_for("index"))

@app.route('/remover/<id>', methods=['POST'])
def remover(id):
    tarefas = carregar_tarefas()
    tarefas = [t for t in tarefas if str(t["id"]) != str(id)]
    salvar_tarefas(tarefas)
    return redirect(url_for("index"))

@app.route('/alternar/<id>', methods=['POST'])
def alternar(id):
    tarefas = carregar_tarefas()
    for t in tarefas:
        if str(t["id"]) == str(id):
            t["feito"] = not t["feito"]
            break
    salvar_tarefas(tarefas)
    return redirect(url_for("index"))

# NOVA ROTA: Editar tarefa
@app.route('/editar/<id>', methods=['POST'])
def editar(id):
    tarefas = carregar_tarefas()
    nova_descricao = request.form.get("nova_descricao", "").strip()
    if nova_descricao:
        for t in tarefas:
            if str(t["id"]) == str(id):
                t["descricao"] = nova_descricao
                break
        salvar_tarefas(tarefas)
    return redirect(url_for("index"))

if _name_ == "_main_":
    app.run(debug=True)
