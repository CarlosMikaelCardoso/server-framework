import re
import webbrowser
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

COMMANDS_FILE = "commands.json"

if not os.path.exists(COMMANDS_FILE):
    with open(COMMANDS_FILE, "w") as f:
        json.dump({}, f)

def load_commands():
    with open(COMMANDS_FILE, "r") as f:
        return json.load(f)

def save_commands(commands):
    with open(COMMANDS_FILE, "w") as f:
        json.dump(commands, f, indent=4)

commands = load_commands()

# Relações semânticas (ações e objetos válidos)
valid_relations = {
    "ligar": ["luz", "ventilador", "tv", "ar-condicionado", "alarme"],
    "desligar": ["luz", "ventilador", "tv", "ar-condicionado", "alarme"],
    "abrir": ["porta", "janela", "cortina"],
    "fechar": ["porta", "janela", "cortina"],
    "aumentar": ["volume", "temperatura", "brilho"],
    "diminuir": ["volume", "temperatura", "brilho"],
    "ajustar": ["temperatura", "brilho", "sensibilidade"],
    "ativar": ["alarme", "sensor", "câmera"],
    "desativar": ["alarme", "sensor", "câmera"]
}

# Preposições e locais opcionais
GRAMMAR = {
    "PREPOSIÇÃO": r"\b(no|na|do|da|de|para|em|com)\b",
    "LOCAL": r"\b(quarto|sala|cozinha|banheiro|garagem|varanda|corredor)\b"
}

# Lista de palavras irrelevantes que podem ser removidas da pesquisa
STOP_WORDS = ["no google", "sobre", "na internet", "o que é", "como", "onde", "pesquisar"]

# Estrutura de Árvore de Derivação
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def build_derivation_tree(parts):
    root = TreeNode("<comando>")
    for part in parts:
        new_node = TreeNode(part)
        root.add_child(new_node)
    return root

def print_tree(node, level=0):
    print("  " * level + node.value)
    for child in node.children:
        print_tree(child, level + 1)

# Função para validar se o comando segue a gramática e é coerente
def is_valid_command(parts):
    if len(parts) < 2:
        return False

    action = parts[0]
    obj = parts[1]
    rest = parts[2:]  # Restante do comando (adjetivos, preposições, locais)

    # 1. Verificar se a ação existe
    if action not in valid_relations:
        return False

    # 2. Verificar se o objeto pode ser usado com a ação
    if obj not in valid_relations[action]:
        return False

    # 3. Verificar preposições e locais (se existirem)
    for word in rest:
        if not (
            re.match(GRAMMAR["PREPOSIÇÃO"], word) or
            re.match(GRAMMAR["LOCAL"], word)
        ):
            return False

    return True

# Função para detectar se é uma pesquisa no Google
def is_google_search(command):
    return command.startswith("pesquisar")

# Função para limpar e formatar corretamente a pesquisa no Google
def clean_search_query(command):
    """
    Remove palavras irrelevantes da pesquisa e retorna apenas o termo relevante.
    """
    query = command.replace("pesquisar", "").strip()  # Remove "pesquisar"
    
    for word in STOP_WORDS:
        query = query.replace(word, "").strip()  # Remove palavras irrelevantes

    return query

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.get_json()
    command = data['command'].lower()

    # Se o usuário pedir para pesquisar algo no Google
    if is_google_search(command):
        search_term = clean_search_query(command)  # Limpa a pesquisa

        if search_term:
            search_url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
            return jsonify({"response": f"Redirecionando para pesquisa: {search_url}", "valid": True, "redirect": search_url})
        else:
            return jsonify({"response": "Erro: Nenhuma palavra-chave para pesquisar.", "valid": False})

    # Validação normal de comandos
    parts = command.split()
    if not is_valid_command(parts):
        return jsonify({"response": "Comando inválido! Estrutura incorreta ou ação não compatível com o objeto.", "valid": False})

    action, obj = parts[0], parts[1]

    if action in commands:
        if obj in commands[action]:
            tree = build_derivation_tree(parts)
            print("\nÁrvore de Derivação:")
            print_tree(tree)
            return jsonify({"response": f"Comando '{command}' reconhecido!", "valid": True})
        else:
            commands[action].append(obj)
    else:
        commands[action] = [obj]

    save_commands(commands)
    return jsonify({"response": f"Comando '{command}' foi aprendido!", "valid": True})

if __name__ == '__main__':
    app.run(debug=True)
