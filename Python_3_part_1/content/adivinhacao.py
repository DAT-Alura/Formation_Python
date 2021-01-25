import random


def jogar():
    print("*************************************")
    print("* Bem vindo no jogo de Adivinhação! *")
    print("*************************************")

    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil\n(2) Normal\n(3) Difícil")
    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 3:
        total_de_tentativas = 5
    else:
        total_de_tentativas = 10

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você chutou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100", end="\n\n")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print(
                    "Você errou! O seu chute foi maior do que o número secreto.",
                    end="\n\n"
                )
            elif(menor):
                print(
                    "Você errou! O seu chute foi menor do que o número secreto.",
                    end="\n\n"
                )
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")


if (__name__ == "__main__"):
    jogar()
