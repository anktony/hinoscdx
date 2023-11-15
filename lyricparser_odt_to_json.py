from odf import text, teletype
from odf.opendocument import load
import json
import os

def parse_odt_to_json(input_odt_file, output_json_file):
    # Carrega o arquivo ODT
    doc = load(input_odt_file)
    
    # Inicializa a lista para armazenar as músicas
    musicas = []
    
    # Inicializa variáveis temporárias
    titulo = ''
    letra = []
    processando_letra = False
    
    # Itera pelo conteúdo do documento
    for elem in doc.getElementsByType(text.P):
        texto = teletype.extractText(elem)
        texto = texto.strip()
        
        if not texto:
            if processando_letra:
                letra.append("")  # Inclui linhas em branco na letra
            continue  # Ignora linhas em branco
        
        if not processando_letra:
            titulo = texto
            processando_letra = True
        elif texto.lower() == 'fim':
            if titulo:
                if letra:
                    # Adiciona a música à lista
                    musicas.append({
                        "id": len(musicas) + 1,
                        "Titulo": titulo,
                        "Recebido por": "",
                        "Letra": "\n".join(letra).strip(),
                        "Tom": ""
                    })
                # Limpa as variáveis para a próxima música
                titulo = ''
                letra = []
                processando_letra = False
        else:
            letra.append(texto)
    
    # Converte a lista de músicas em JSON
    musicas_json = json.dumps(musicas, indent=4, ensure_ascii=False)
    
    # Define o caminho de saída
    output_dir = './Json/'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_json_file)
    
    # Salva o JSON em um arquivo de saída
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(musicas_json)
    
    print(f"Parsing concluído e JSON salvo em '{output_path}'.")

if __name__ == "__main__":
    input_odt_file = 'letrasxango.odt'
    output_json_file = 'hinosdexango.json'
    parse_odt_to_json(input_odt_file, output_json_file)
