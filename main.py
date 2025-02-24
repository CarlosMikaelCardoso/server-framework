# # # # # # # # # # import ply.lex as lex
# # # # # # # # # # import ply.yacc as yacc

# # # # # # # # # # # === 1️⃣ Definir os Tokens (Analisador Léxico) ===
# # # # # # # # # # tokens = (
# # # # # # # # # #     'ID', 'NUM',
# # # # # # # # # #     'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
# # # # # # # # # #     'LPAREN', 'RPAREN', 'EQUALS', 'SEMICOLON'
# # # # # # # # # # )

# # # # # # # # # # t_PLUS     = r'\+'
# # # # # # # # # # t_MINUS    = r'-'
# # # # # # # # # # t_TIMES    = r'\*'
# # # # # # # # # # t_DIVIDE   = r'/'
# # # # # # # # # # t_LPAREN   = r'\('
# # # # # # # # # # t_RPAREN   = r'\)'
# # # # # # # # # # t_EQUALS   = r'='
# # # # # # # # # # t_SEMICOLON = r';'
# # # # # # # # # # t_ID       = r'[a-zA-Z_][a-zA-Z0-9_]*'

# # # # # # # # # # # Tratamento de números inteiros
# # # # # # # # # # def t_NUM(t):
# # # # # # # # # #     r'\d+'
# # # # # # # # # #     t.value = int(t.value)
# # # # # # # # # #     return t

# # # # # # # # # # # Ignorar espaços e tabulações
# # # # # # # # # # t_ignore = ' \t'

# # # # # # # # # # # Tratamento de erros léxicos
# # # # # # # # # # def t_error(t):
# # # # # # # # # #     print(f"Caractere inválido: {t.value[0]}")
# # # # # # # # # #     t.lexer.skip(1)

# # # # # # # # # # # Criar o analisador léxico
# # # # # # # # # # lexer = lex.lex()

# # # # # # # # # # # === 2️⃣ Definir a Gramática Livre de Contexto (Analisador Sintático) ===
# # # # # # # # # # def p_statement_assign(p):
# # # # # # # # # #     "statement : ID EQUALS expression SEMICOLON"
# # # # # # # # # #     print(f"{p[1]} = {p[3]}")

# # # # # # # # # # def p_expression_binop(p):
# # # # # # # # # #     """expression : expression PLUS term
# # # # # # # # # #                   | expression MINUS term"""
# # # # # # # # # #     if p[2] == '+': p[0] = p[1] + p[3]
# # # # # # # # # #     elif p[2] == '-': p[0] = p[1] - p[3]

# # # # # # # # # # def p_expression_term(p):
# # # # # # # # # #     "expression : term"
# # # # # # # # # #     p[0] = p[1]

# # # # # # # # # # def p_term_binop(p):
# # # # # # # # # #     """term : term TIMES factor
# # # # # # # # # #             | term DIVIDE factor"""
# # # # # # # # # #     if p[2] == '*': p[0] = p[1] * p[3]
# # # # # # # # # #     elif p[2] == '/': p[0] = p[1] / p[3]

# # # # # # # # # # def p_term_factor(p):
# # # # # # # # # #     "term : factor"
# # # # # # # # # #     p[0] = p[1]

# # # # # # # # # # def p_factor_num(p):
# # # # # # # # # #     "factor : NUM"
# # # # # # # # # #     p[0] = p[1]

# # # # # # # # # # def p_factor_expr(p):
# # # # # # # # # #     "factor : LPAREN expression RPAREN"
# # # # # # # # # #     p[0] = p[2]

# # # # # # # # # # def p_error(p):
# # # # # # # # # #     print("Erro de sintaxe!")

# # # # # # # # # # # Criar o parser
# # # # # # # # # # parser = yacc.yacc()

# # # # # # # # # # # === 3️⃣ Testar o compilador ===
# # # # # # # # # # while True:
# # # # # # # # # #     try:
# # # # # # # # # #         entrada = input("Digite uma expressão: ")
# # # # # # # # # #     except EOFError:
# # # # # # # # # #         break
# # # # # # # # # #     if not entrada:
# # # # # # # # # #         continue
# # # # # # # # # #     parser.parse(entrada)



# # # # # # # # # import re
# # # # # # # # # import random
# # # # # # # # # from typing import List, Dict

# # # # # # # # # class VoiceCommandFramework:
# # # # # # # # #     def __init__(self, grammar: Dict[str, List[str]]):
# # # # # # # # #         """
# # # # # # # # #         Inicializa o framework com uma gramática livre de contexto.
# # # # # # # # #         :param grammar: Dicionário representando regras da gramática.
# # # # # # # # #         """
# # # # # # # # #         self.grammar = grammar
    
# # # # # # # # #     def validate_command(self, command: str) -> bool:
# # # # # # # # #         """
# # # # # # # # #         Valida se um comando segue a gramática definida.
# # # # # # # # #         :param command: String do comando de voz.
# # # # # # # # #         :return: True se for válido, False caso contrário.
# # # # # # # # #         """
# # # # # # # # #         pattern = self._generate_regex_pattern()
# # # # # # # # #         return bool(re.fullmatch(pattern, command))
    
# # # # # # # # #     def generate_command(self, start_symbol: str = "<command>") -> str:
# # # # # # # # #         """
# # # # # # # # #         Gera um comando válido aleatoriamente.
# # # # # # # # #         :param start_symbol: Símbolo inicial da gramática.
# # # # # # # # #         :return: Comando gerado.
# # # # # # # # #         """
# # # # # # # # #         return self._expand_rule(start_symbol)
    
# # # # # # # # #     def _expand_rule(self, rule: str) -> str:
# # # # # # # # #         """
# # # # # # # # #         Expande recursivamente uma regra da gramática.
# # # # # # # # #         """
# # # # # # # # #         if rule not in self.grammar:
# # # # # # # # #             return rule  # Terminal
# # # # # # # # #         production = random.choice(self.grammar[rule])
# # # # # # # # #         return ' '.join(self._expand_rule(token) for token in production.split())
    
# # # # # # # # #     def _generate_regex_pattern(self) -> str:
# # # # # # # # #         """
# # # # # # # # #         Converte a gramática em uma expressão regular para validação.
# # # # # # # # #         """
# # # # # # # # #         regex = self.grammar["<command>"][0]
# # # # # # # # #         for key in self.grammar:
# # # # # # # # #             regex = regex.replace(key, f"({'|'.join(self.grammar[key])})")
# # # # # # # # #         return regex.replace(" ", "\\s*")  # Permitir espaços flexíveis

# # # # # # # # # # Exemplo de uso do framework
# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     grammar = {
# # # # # # # # #         "<command>": ["<action> <object>"],
# # # # # # # # #         "<action>": ["ligar", "desligar", "abrir", "fechar"],
# # # # # # # # #         "<object>": ["luz", "porta", "janela", "televisão"]
# # # # # # # # #     }
    
# # # # # # # # #     vc_framework = VoiceCommandFramework(grammar)
    
# # # # # # # # #     # Teste de validação
# # # # # # # # #     print(vc_framework.validate_command("ligar luz"))  # True
# # # # # # # # #     print(vc_framework.validate_command("desligar porta"))  # True
# # # # # # # # #     print(vc_framework.validate_command("comer maçã"))  # False
    
# # # # # # # # #     # Teste de geração
# # # # # # # # #     print(vc_framework.generate_command())  # Exemplo: "abrir janela"



# # # # # # # # class CommandNode:
# # # # # # # #     def __init__(self, value):
# # # # # # # #         self.value = value
# # # # # # # #         self.children = []

# # # # # # # # def build_derivation_tree():
# # # # # # # #     root = CommandNode('Command')
# # # # # # # #     action = CommandNode('Action: Turn On')
# # # # # # # #     object = CommandNode('Object: Lights')
# # # # # # # #     root.children.append(action)
# # # # # # # #     root.children.append(object)
# # # # # # # #     return root

# # # # # # # # def print_tree(node, indent=0):
# # # # # # # #     print('  ' * indent + node.value)
# # # # # # # #     for child in node.children:
# # # # # # # #         print_tree(child, indent + 1)

# # # # # # # # tree = build_derivation_tree()
# # # # # # # # print_tree(tree)



# # # # # # # from flask import Flask, request, jsonify
# # # # # # # from flask_cors import CORS

# # # # # # # app = Flask(__name__)
# # # # # # # CORS(app)  # Enable CORS for cross-origin requests from your React app

# # # # # # # @app.route('/process_command', methods=['POST'])
# # # # # # # def process_command():
# # # # # # #     data = request.get_json()
# # # # # # #     command = data['command']
# # # # # # #     # Simplificação: assume que todo comando é válido para o exemplo
# # # # # # #     return jsonify({"response": f"Comando '{command}' reconhecido e aceito!"})

# # # # # # # if __name__ == '__main__':
# # # # # # #     app.run(debug=True, host='0.0.0.0')



# # # # # # from flask import Flask, request, jsonify
# # # # # # from flask_cors import CORS

# # # # # # app = Flask(__name__)
# # # # # # CORS(app)  # Permite conexões do React ao Flask

# # # # # # # Definição da Gramática Livre de Contexto (GLC)
# # # # # # valid_actions = {
# # # # # #     "ligar": ["luz", "ventilador", "televisão"],
# # # # # #     "desligar": ["luz", "ventilador", "televisão"],
# # # # # #     "abrir": ["porta"],
# # # # # #     "fechar": ["porta"],
# # # # # #     "ajustar": ["ar-condicionado"]
# # # # # # }

# # # # # # # Classe para representar a árvore de derivação
# # # # # # class TreeNode:
# # # # # #     def __init__(self, value):
# # # # # #         self.value = value
# # # # # #         self.children = []

# # # # # # def build_derivation_tree(action, obj):
# # # # # #     root = TreeNode("<comando>")
# # # # # #     action_node = TreeNode(f"<ação>: {action}")
# # # # # #     object_node = TreeNode(f"<objeto>: {obj}")
    
# # # # # #     root.children.append(action_node)
# # # # # #     root.children.append(object_node)
# # # # # #     return root

# # # # # # def validate_command(command):
# # # # # #     parts = command.split()
# # # # # #     if len(parts) != 2:
# # # # # #         return False, None  # Comando inválido, não segue a estrutura <ação> <objeto>
    
# # # # # #     action, obj = parts
# # # # # #     if action in valid_actions and obj in valid_actions[action]:
# # # # # #         tree = build_derivation_tree(action, obj)
# # # # # #         return True, tree
# # # # # #     return False, None

# # # # # # def print_tree(node, level=0):
# # # # # #     print("  " * level + node.value)
# # # # # #     for child in node.children:
# # # # # #         print_tree(child, level + 1)

# # # # # # @app.route('/process_command', methods=['POST'])
# # # # # # def process_command():
# # # # # #     data = request.get_json()
# # # # # #     command = data['command'].lower()  # Converter para minúsculas para normalização
    
# # # # # #     is_valid, tree = validate_command(command)
    
# # # # # #     if is_valid:
# # # # # #         print("Árvore de Derivação do Comando:")
# # # # # #         print_tree(tree)  # Imprime no console a árvore gerada
# # # # # #         return jsonify({"response": f"Comando '{command}' reconhecido e aceito!", "valid": True})
# # # # # #     else:
# # # # # #         return jsonify({"response": f"Comando '{command}' não é válido pela gramática.", "valid": False})

# # # # # # if __name__ == '__main__':
# # # # # #     app.run(debug=True)


# # # # # from flask import Flask, request, jsonify
# # # # # from flask_cors import CORS
# # # # # import json
# # # # # import os

# # # # # app = Flask(__name__)
# # # # # CORS(app)

# # # # # # Arquivo que armazenará os comandos aprendidos
# # # # # COMMANDS_FILE = "commands.json"

# # # # # # Verifica se o arquivo de comandos existe, senão cria um vazio
# # # # # if not os.path.exists(COMMANDS_FILE):
# # # # #     with open(COMMANDS_FILE, "w") as f:
# # # # #         json.dump({}, f)

# # # # # # Função para carregar os comandos armazenados
# # # # # def load_commands():
# # # # #     with open(COMMANDS_FILE, "r") as f:
# # # # #         return json.load(f)

# # # # # # Função para salvar novos comandos
# # # # # def save_commands(commands):
# # # # #     with open(COMMANDS_FILE, "w") as f:
# # # # #         json.dump(commands, f, indent=4)

# # # # # # Carregar os comandos existentes
# # # # # commands = load_commands()

# # # # # # Estrutura de Árvore de Derivação
# # # # # class TreeNode:
# # # # #     def __init__(self, value):
# # # # #         self.value = value
# # # # #         self.children = []

# # # # # def build_derivation_tree(action, obj):
# # # # #     root = TreeNode("<comando>")
# # # # #     action_node = TreeNode(f"<ação>: {action}")
# # # # #     object_node = TreeNode(f"<objeto>: {obj}")
# # # # #     root.children.append(action_node)
# # # # #     root.children.append(object_node)
# # # # #     return root

# # # # # def print_tree(node, level=0):
# # # # #     print("  " * level + node.value)
# # # # #     for child in node.children:
# # # # #         print_tree(child, level + 1)

# # # # # @app.route('/process_command', methods=['POST'])
# # # # # def process_command():
# # # # #     data = request.get_json()
# # # # #     command = data['command'].lower()
# # # # #     parts = command.split()

# # # # #     if len(parts) != 2:
# # # # #         return jsonify({"response": "Comando inválido. Deve ser no formato '<ação> <objeto>'", "valid": False})

# # # # #     action, obj = parts

# # # # #     # Verifica se a ação já foi aprendida antes
# # # # #     if action in commands:
# # # # #         if obj in commands[action]:
# # # # #             # Comando já conhecido, retorna a árvore de derivação
# # # # #             tree = build_derivation_tree(action, obj)
# # # # #             print("\nÁrvore de Derivação:")
# # # # #             print_tree(tree)
# # # # #             return jsonify({"response": f"Comando '{command}' reconhecido!", "valid": True})
# # # # #         else:
# # # # #             commands[action].append(obj)
# # # # #     else:
# # # # #         # Nova ação, adiciona ao banco de dados
# # # # #         commands[action] = [obj]

# # # # #     # Salva a nova gramática aprendida
# # # # #     save_commands(commands)
    
# # # # #     return jsonify({"response": f"Comando '{command}' foi aprendido!", "valid": True})

# # # # # if __name__ == '__main__':
# # # # #     app.run(debug=True)


# # # # from flask import Flask, request, jsonify
# # # # from flask_cors import CORS
# # # # import json
# # # # import os

# # # # app = Flask(__name__)
# # # # CORS(app)

# # # # # Arquivo que armazenará os comandos aprendidos
# # # # COMMANDS_FILE = "commands.json"

# # # # # Verifica se o arquivo de comandos existe, senão cria um vazio
# # # # if not os.path.exists(COMMANDS_FILE):
# # # #     with open(COMMANDS_FILE, "w") as f:
# # # #         json.dump({}, f)

# # # # # Função para carregar os comandos armazenados
# # # # def load_commands():
# # # #     with open(COMMANDS_FILE, "r") as f:
# # # #         return json.load(f)

# # # # # Função para salvar novos comandos
# # # # def save_commands(commands):
# # # #     with open(COMMANDS_FILE, "w") as f:
# # # #         json.dump(commands, f, indent=4)

# # # # commands = load_commands()

# # # # # Estrutura de Árvore de Derivação
# # # # class TreeNode:
# # # #     def __init__(self, value):
# # # #         self.value = value
# # # #         self.children = []

# # # #     def add_child(self, child):
# # # #         self.children.append(child)

# # # # def build_derivation_tree(parts):
# # # #     root = TreeNode("<comando>")
# # # #     current_node = root
# # # #     for part in parts:
# # # #         new_node = TreeNode(part)
# # # #         current_node.add_child(new_node)
# # # #         current_node = new_node
# # # #     return root

# # # # def print_tree(node, level=0):
# # # #     print("  " * level + node.value)
# # # #     for child in node.children:
# # # #         print_tree(child, level + 1)

# # # # @app.route('/process_command', methods=['POST'])
# # # # def process_command():
# # # #     data = request.get_json()
# # # #     command = data['command'].lower()
# # # #     parts = command.split()

# # # #     if len(parts) < 2:
# # # #         return jsonify({"response": "Comando inválido. Formato esperado com mais detalhes.", "valid": False})

# # # #     action, *middle, obj = parts  # Decomposição básica do comando

# # # #     if action in commands:
# # # #         if obj in commands[action]:
# # # #             tree = build_derivation_tree(parts)
# # # #             print("\nÁrvore de Derivação:")
# # # #             print_tree(tree)
# # # #             return jsonify({"response": f"Comando '{command}' reconhecido!", "valid": True})
# # # #         else:
# # # #             commands[action].append(obj)
# # # #     else:
# # # #         commands[action] = [obj]

# # # #     save_commands(commands)
# # # #     return jsonify({"response": f"Comando '{command}' foi aprendido!", "valid": True})

# # # # if __name__ == '__main__':
# # # #     app.run(debug=True)


# # # import re
# # # from flask import Flask, request, jsonify
# # # from flask_cors import CORS
# # # import json
# # # import os

# # # app = Flask(__name__)
# # # CORS(app)

# # # COMMANDS_FILE = "commands.json"

# # # if not os.path.exists(COMMANDS_FILE):
# # #     with open(COMMANDS_FILE, "w") as f:
# # #         json.dump({}, f)

# # # def load_commands():
# # #     with open(COMMANDS_FILE, "r") as f:
# # #         return json.load(f)

# # # def save_commands(commands):
# # #     with open(COMMANDS_FILE, "w") as f:
# # #         json.dump(commands, f, indent=4)

# # # commands = load_commands()

# # # # Definição da gramática
# # # GRAMMAR = {
# # #     "AÇÃO": r"\b(ligar|desligar|abrir|fechar|aumentar|diminuir|ajustar|ativar|desativar)\b",
# # #     "OBJETO": r"\b(luz|porta|ventilador|tv|ar-condicionado|alarme|cortina|som|sensor|projetor|câmera)\b",
# # #     "ADJETIVO": r"\b(principal|secundária|da frente|dos fundos|grande|pequena|rápida|lenta)\b",
# # #     "PREPOSIÇÃO": r"\b(no|na|do|da|de|para|em|com)\b",
# # #     "LOCAL": r"\b(quarto|sala|cozinha|banheiro|garagem|varanda|corredor)\b"
# # # }

# # # # Estrutura de Árvore de Derivação
# # # class TreeNode:
# # #     def __init__(self, value):
# # #         self.value = value
# # #         self.children = []

# # #     def add_child(self, child):
# # #         self.children.append(child)

# # # def build_derivation_tree(parts):
# # #     root = TreeNode("<comando>")
# # #     for part in parts:
# # #         new_node = TreeNode(part)
# # #         root.add_child(new_node)
# # #     return root

# # # def print_tree(node, level=0):
# # #     print("  " * level + node.value)
# # #     for child in node.children:
# # #         print_tree(child, level + 1)

# # # # Função para validar se o comando segue a gramática
# # # def is_valid_command(parts):
# # #     if len(parts) < 2:
# # #         return False

# # #     # Separar partes do comando
# # #     action = parts[0]
# # #     obj = parts[1]
# # #     rest = parts[2:]

# # #     # Verifica se a ação é válida
# # #     if not re.match(GRAMMAR["AÇÃO"], action):
# # #         return False

# # #     # Verifica se o objeto é válido
# # #     if not re.match(GRAMMAR["OBJETO"], obj):
# # #         return False

# # #     # Verifica os elementos opcionais no meio do comando
# # #     for word in rest:
# # #         if not (
# # #             re.match(GRAMMAR["ADJETIVO"], word) or
# # #             re.match(GRAMMAR["PREPOSIÇÃO"], word) or
# # #             re.match(GRAMMAR["LOCAL"], word)
# # #         ):
# # #             return False

# # #     return True

# # # @app.route('/process_command', methods=['POST'])
# # # def process_command():
# # #     data = request.get_json()
# # #     command = data['command'].lower()
# # #     parts = command.split()

# # #     # Validação do comando com base na gramática
# # #     if not is_valid_command(parts):
# # #         return jsonify({"response": "Comando inválido! Estrutura incorreta ou palavras desconhecidas.", "valid": False})

# # #     action, obj = parts[0], parts[1]

# # #     # Se o comando for válido, verifica se já existe ou aprende um novo
# # #     if action in commands:
# # #         if obj in commands[action]:
# # #             tree = build_derivation_tree(parts)
# # #             print("\nÁrvore de Derivação:")
# # #             print_tree(tree)
# # #             return jsonify({"response": f"Comando '{command}' reconhecido!", "valid": True})
# # #         else:
# # #             commands[action].append(obj)
# # #     else:
# # #         commands[action] = [obj]

# # #     save_commands(commands)
# # #     return jsonify({"response": f"Comando '{command}' foi aprendido!", "valid": True})

# # # if __name__ == '__main__':
# # #     app.run(debug=True)


# # import re
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # import json
# # import os
# # import webbrowser  # Biblioteca para abrir URLs no navegador

# # app = Flask(__name__)
# # CORS(app)

# # COMMANDS_FILE = "commands.json"

# # if not os.path.exists(COMMANDS_FILE):
# #     with open(COMMANDS_FILE, "w") as f:
# #         json.dump({}, f)

# # def load_commands():
# #     with open(COMMANDS_FILE, "r") as f:
# #         return json.load(f)

# # def save_commands(commands):
# #     with open(COMMANDS_FILE, "w") as f:
# #         json.dump(commands, f, indent=4)

# # commands = load_commands()

# # # Relações semânticas (ações e objetos válidos)
# # valid_relations = {
# #     "ligar": ["luz", "ventilador", "tv", "ar-condicionado", "alarme"],
# #     "desligar": ["luz", "ventilador", "tv", "ar-condicionado", "alarme"],
# #     "abrir": ["porta", "janela", "cortina"],
# #     "fechar": ["porta", "janela", "cortina"],
# #     "aumentar": ["volume", "temperatura", "brilho"],
# #     "diminuir": ["volume", "temperatura", "brilho"],
# #     "ajustar": ["temperatura", "brilho", "sensibilidade"],
# #     "ativar": ["alarme", "sensor", "câmera"],
# #     "desativar": ["alarme", "sensor", "câmera"]
# # }
 
# # # Preposições e locais opcionais
# # GRAMMAR = {
# #     "PREPOSIÇÃO": r"\b(no|na|do|da|de|para|em|com)\b",
# #     "LOCAL": r"\b(quarto|sala|cozinha|banheiro|garagem|varanda|corredor)\b"
# # }

# # # Estrutura de Árvore de Derivação
# # class TreeNode:
# #     def __init__(self, value):
# #         self.value = value
# #         self.children = []

# #     def add_child(self, child):
# #         self.children.append(child)

# # def build_derivation_tree(parts):
# #     root = TreeNode("<comando>")
# #     for part in parts:
# #         new_node = TreeNode(part)
# #         root.add_child(new_node)
# #     return root

# # def print_tree(node, level=0):
# #     print("  " * level + node.value)
# #     for child in node.children:
# #         print_tree(child, level + 1)

# # # Função para validar se o comando segue a gramática e é coerente
# # def is_valid_command(parts):
# #     if len(parts) < 2:
# #         return False

# #     action = parts[0]
# #     obj = parts[1]
# #     rest = parts[2:]  # Restante do comando (adjetivos, preposições, locais)

# #     # 1. Verificar se a ação existe
# #     if action not in valid_relations:
# #         return False

# #     # 2. Verificar se o objeto pode ser usado com a ação
# #     if obj not in valid_relations[action]:
# #         return False

# #     # 3. Verificar preposições e locais (se existirem)
# #     for word in rest:
# #         if not (
# #             re.match(GRAMMAR["PREPOSIÇÃO"], word) or
# #             re.match(GRAMMAR["LOCAL"], word)
# #         ):
# #             return False

# #     return True



# # @app.route('/process_command', methods=['POST'])
# # def process_command():
# #     data = request.get_json()
# #     command = data['command'].lower()
# #     parts = command.split()

# #     # Se o usuário pedir para pesquisar algo no Google
# #     if parts[0] == "pesquisar" and "no google" in command:
# #         search_term = command.replace("pesquisar", "").replace("no Google", "").strip()
# #         if search_term:
# #             search_url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
# #             return jsonify({"response": f"Redirecionando para pesquisa: {search_url}", "valid": True, "redirect": search_url})

# #     # Validação normal de comandos
# #     if not is_valid_command(parts):
# #         return jsonify({"response": "Comando inválido! Estrutura incorreta ou ação não compatível com o objeto.", "valid": False})

# #     action, obj = parts[0], parts[1]

# #     if action in commands:
# #         if obj in commands[action]:
# #             tree = build_derivation_tree(parts)
# #             print("\nÁrvore de Derivação:")
# #             print_tree(tree)
# #             return jsonify({"response": f"Comando '{command}' reconhecido!", "valid": True})
# #         else:
# #             commands[action].append(obj)
# #     else:
# #         commands[action] = [obj]

# #     save_commands(commands)
# #     return jsonify({"response": f"Comando '{command}' foi aprendido!", "valid": True})


# # if __name__ == '__main__':
# #     app.run(debug=True)



# import re
# import webbrowser
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import json
# import os

# app = Flask(__name__)
# CORS(app)

# COMMANDS_FILE = "commands.json"

# if not os.path.exists(COMMANDS_FILE):
#     with open(COMMANDS_FILE, "w") as f:
#         json.dump({}, f)

# def load_commands():
#     with open(COMMANDS_FILE, "r") as f:
#         return json.load(f)

# def save_commands(commands):
#     with open(COMMANDS_FILE, "w") as f:
#         json.dump(commands, f, indent=4)

# commands = load_commands()

# # Relações semânticas (ações e objetos válidos)
# valid_relations = {
#     "ligar": ["luz", "ventilador", "tv", "ar-condicionado", "alarme"],
#     "desligar": ["luz", "ventilador", "tv", "ar-condicionado", "alarme"],
#     "abrir": ["porta", "janela", "cortina"],
#     "fechar": ["porta", "janela", "cortina"],
#     "aumentar": ["volume", "temperatura", "brilho"],
#     "diminuir": ["volume", "temperatura", "brilho"],
#     "ajustar": ["temperatura", "brilho", "sensibilidade"],
#     "ativar": ["alarme", "sensor", "câmera"],
#     "desativar": ["alarme", "sensor", "câmera"]
# }

# # Preposições e locais opcionais
# GRAMMAR = {
#     "PREPOSIÇÃO": r"\b(no|na|do|da|de|para|em|com)\b",
#     "LOCAL": r"\b(quarto|sala|cozinha|banheiro|garagem|varanda|corredor)\b"
# }

# # Estrutura de Árvore de Derivação
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.children = []

#     def add_child(self, child):
#         self.children.append(child)

# def build_derivation_tree(parts):
#     root = TreeNode("<comando>")
#     for part in parts:
#         new_node = TreeNode(part)
#         root.add_child(new_node)
#     return root

# def print_tree(node, level=0):
#     print("  " * level + node.value)
#     for child in node.children:
#         print_tree(child, level + 1)

# # Função para validar se o comando segue a gramática e é coerente
# def is_valid_command(parts):
#     if len(parts) < 2:
#         return False

#     action = parts[0]
#     obj = parts[1]
#     rest = parts[2:]  # Restante do comando (adjetivos, preposições, locais)

#     # 1. Verificar se a ação existe
#     if action not in valid_relations:
#         return False

#     # 2. Verificar se o objeto pode ser usado com a ação
#     if obj not in valid_relations[action]:
#         return False

#     # 3. Verificar preposições e locais (se existirem)
#     for word in rest:
#         if not (
#             re.match(GRAMMAR["PREPOSIÇÃO"], word) or
#             re.match(GRAMMAR["LOCAL"], word)
#         ):
#             return False

#     return True

# # Função para detectar se é uma pesquisa no Google
# def is_google_search(command):
#     return command.startswith("pesquisar ")

# @app.route('/process_command', methods=['POST'])
# def process_command():
#     data = request.get_json()
#     command = data['command'].lower()

#     # Se o usuário pedir para pesquisar algo no Google
#     if is_google_search(command):
#         search_term = command.replace("pesquisar", "").strip()
#         if search_term:
#             search_url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
#             return jsonify({"response": f"Redirecionando para pesquisa: {search_url}", "valid": True, "redirect": search_url})
#         else:
#             return jsonify({"response": "Erro: Nenhuma palavra-chave para pesquisar.", "valid": False})

#     # Validação normal de comandos
#     parts = command.split()
#     if not is_valid_command(parts):
#         return jsonify({"response": "Comando inválido! Estrutura incorreta ou ação não compatível com o objeto.", "valid": False})

#     action, obj = parts[0], parts[1]

#     if action in commands:
#         if obj in commands[action]:
#             tree = build_derivation_tree(parts)
#             print("\nÁrvore de Derivação:")
#             print_tree(tree)
#             return jsonify({"response": f"Comando '{command}' reconhecido!", "valid": True})
#         else:
#             commands[action].append(obj)
#     else:
#         commands[action] = [obj]

#     save_commands(commands)
#     return jsonify({"response": f"Comando '{command}' foi aprendido!", "valid": True})

# if __name__ == '__main__':
#     app.run(debug=True)



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
