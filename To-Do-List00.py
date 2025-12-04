from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
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
    return render_template("index.html")

@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(carregar_tarefas())

@app.route('/api/tarefas', methods=['POST'])
def post_tarefas():
    tarefas = request.get_json()
    salvar_tarefas(tarefas)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
