import json

def adicionar_musica(letra, titulo, recebido_por, tom):
    musica = {
        "id": len(musicas) + 1,
        "Titulo": titulo,
        "Recebido por": recebido_por,
        "Letra": letra,
        "Tom": tom
    }

    musicas.append(musica)

    with open("musicas.json", "w", encoding="utf-8") as arquivo:
        json.dump(musicas, arquivo, ensure_ascii=False, indent=4)

    print(f"A música '{titulo}' foi adicionada ao arquivo 'musicas.json' com sucesso!")

def main():
    print("Bem-vindo(a) ao criador de arquivos JSON para músicas!")
    print("Por favor, preencha as informações abaixo:")

    titulo = input("Título da música: ")
    recebido_por = input("Recebido por: ")
    tom = input("Tom da música: ")

    print("Digite a letra da música. Pressione Enter para inserir uma nova estrofe.")
    print("Digite 'fim' em uma linha separada quando terminar.")

    letra = ""
    while True:
        estrofe = input()
        if estrofe == "fim":
            break
        letra += estrofe + "\n"

    adicionar_musica(letra, titulo, recebido_por, tom)

if __name__ == "__main__":
    try:
        with open("musicas.json", "r", encoding="utf-8") as arquivo:
            musicas = json.load(arquivo)
    except FileNotFoundError:
        musicas = []

    main()
