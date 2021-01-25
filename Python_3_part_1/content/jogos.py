import forca
import adivinhacao

print("**********************")
print("* Escolha o seu jogo *")
print("**********************")

print("(1) Forca\n(2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando Forca", end="\n\n")
    forca.jogar()
else:
    print("Jogando Adivinhação", end="\n\n")
    adivinhacao.jogar()
