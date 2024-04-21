alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import logo
def cesar(direcao_de_cesar,texto_inicial,desloc):
    texto_final = ""

    if direcao_de_cesar == "descriptar":
        desloc *= -1

    for caractere in texto_inicial:
        if caractere in alfabeto:
            posicao = alfabeto.index(caractere)
            nova_posicao = posicao + desloc
            texto_final += alfabeto[nova_posicao]
        else:
            texto_final += caractere
    print(texto_final)

print(logo.logo)

escolha = True
while escolha:
    direcao = input("Escreva 'Encriptar' para encriptar ou 'Descriptar' para decodificar\n").lower()
    mensagem = input("Escreva a mensagem\n").lower()
    deslocamento = int(input("Digite o número do turno\n"))

    deslocamento = deslocamento %  26

    cesar(direcao_de_cesar = direcao,texto_inicial = mensagem,desloc = deslocamento)

    pergunta = input("Quer encriptar ou descriptar outra mensagem? (Sim/Nao)\n").lower()

    if pergunta == "nao":
        escolha = False

print("Até Logo!")

