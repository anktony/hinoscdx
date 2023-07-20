import json

def buscar_musicas_por_ids(ids, arquivo_entrada, arquivo_saida):
    musicas_encontradas = []
    with open(arquivo_entrada, "r", encoding="utf-8") as arquivo:  # Especificamos a codificação utf-8
        musicas = json.load(arquivo)
        for musica in musicas:
            if musica["id"] in ids:
                musicas_encontradas.append(musica)

    with open(arquivo_saida, "w", encoding="utf-8") as arquivo:  # Especificamos a codificação utf-8
        json.dump(musicas_encontradas, arquivo, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    ids_procurados = [1, 4, 5, 7, 11, 12, 14, 19, 29, 30, 31, 32, 33, 34, 35, 39, 45, 46, 47, 48, 49, 50, 51]  # Insira os IDs que deseja procurar nesta lista

    arquivo_entrada = "./Json/musicas.json"
    arquivo_saida = "./Json/selecao.json"

    buscar_musicas_por_ids(ids_procurados, arquivo_entrada, arquivo_saida)

    print("Busca concluída. As músicas encontradas foram armazenadas no arquivo 'selecao.json'.")
