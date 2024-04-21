alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direcao = input("Escreva 'Encriptar' para encriptar ou 'Descriptar' para decodificar\n").lower()
mensagem = input("Escreva a mensagem\n").lower().replace(" ","")
deslocamento = int(input("Digite o número do turno\n"))

def cesar(direcao_de_cesar,texto_inicial,desloc):
    texto_final = ""
    if direcao_de_cesar == "descriptar":
        desloc *= -1
    for letra in texto_inicial:
        posicao = alfabeto.index(letra)
        nova_posicao = posicao + desloc
        texto_final += alfabeto[nova_posicao]

    print(texto_final)

cesar(direcao_de_cesar = direcao,texto_inicial = mensagem,desloc = deslocamento)


