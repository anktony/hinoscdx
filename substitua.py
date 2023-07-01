import json

# Abre o arquivo JSON
with open('musicas.json', 'r') as file:
    # Carrega o conteúdo do arquivo JSON
    data = json.load(file)

# Função para substituir a sequência de caracteres
def replace_sequence(value):
    return value.replace("â‡ƒ", "\u21c3")

# Itera sobre os elementos da lista e realiza a substituição
for i, item in enumerate(data):
    if isinstance(item, str):
        data[i] = replace_sequence(item)

# Salva o arquivo JSON atualizado
with open('musicas.json', 'w', encoding="utf-8") as file:
    json.dump(data, file)
