alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direcao = input("Escreva 'Encode' para enciptar ou 'Decode' para decodificar\n").lower()
mensagem = input("Escreva a mensagem\n").lower()
deslocamento = int(input("Digite o número do turno\n"))

def encriptar(string,inteiro):
    texto_escondido = ""
    for letra in string:
       posicao = alfabeto.index((letra))
       nova_posicao = posicao + inteiro
       nova_letra = alfabeto[nova_posicao]
       texto_escondido += nova_letra

    print(texto_escondido)

encriptar(mensagem,deslocamento)