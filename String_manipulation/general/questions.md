# Aula 1

Nesta aula aprendemos como retirar partes de uma string utilizando slice (fatiamento). Com esse conhecimento veja o código abaixo:

```py
texto = "Izuku Midoriya"
texto[0:10]
texto2 = texto[:4]
print( texto2)
print(texto)
```

Qual será a Saída deste código?

A -
```py
Izuk
Izuku Mido
```

B -
```py
Iuzuku
Izuku Midoriya
```

__C__ -
```py
Izuk
Izuku Midoriya
```
> Correta! Uma string não é modificada quando fazemos qualquer fatiamento nela, e além disso o segundo índice é exclusor.

---

Vimos nessa aula que o método find ajuda a capturar valores de uma forma mais dinâmica dentro de uma string qualquer. Analise o código abaixo:

```py
celular = "(41)96574-1728"
indiceInicialCodigoArea = x
indiceFinalCodigoArea   = y

print (celular[indiceInicialCodigoArea:indiceFinalCodigoArea])
```

Com o objetivo de retirar o código de área sem os "()", os valores de x e y podem ser substituídos por:

__A__ -
```py
Termo x = celular.find("(") + 1
Termo y = celular.find(")")
```
> Correto! É preciso colocar um + 1 no termo x para poder pegar o índice após o (.

B -
```py
Termo x = celular.find("(")
Termo y = celular.find(")")
```

C -
```py
Termo x = celular.find("(") + 1
Termo y = celular.find(")") + 1
```

# Aula 2

Aprendemos sobre o funcionamento do if durante essa aula, tendo o que vimos em mente dê uma olhada no código abaixo:

```py
nome = "Rodrigo"
sobreNome = ""

if nome:
    print("Nome Correto")
else:
    print("Nome Incorreto")

if sobreNome:
    print("Sobrenome Correto")
else:
    print("Sobrenome Incorreto")
```

Marque qual é a saída desse código:

__A__ - Nome Correto Sobrenome Incorreto
> Correto! O programa não retorna um erro pois o if do Python consegue lidar com não booleanos e além disso ele trata uma string vazia como False.

B - Nome Correto Sobrenome Correto

C - O programa retornaria algum erro!

---

Nesta aula, vimos mais métodos que as strings possuem. Tendo em mente tudo que vimos até aqui, dê uma olhada no código abaixo:

```py
nome = "Eren Yeager"
tamanho = len(nome)
indice = nome.find("Eren")
print(tamanho)
print(nome[indice:tamanho])
```

Qual será a saída desse código

__A__ - 11 Eren Yeager
> Correto! O tamanho da string é um inteiro maior que o último índice da mesma, então o "r" no final vai aparecer.

B - 11 Yeager

C - 11 Eren Yeage

# Aula 3

Lembre-se do conteúdo do capítulo e analise o código abaixo:

```py
episodio = "Boku no hero - TEmporada 1, episódio 12"
episodioFormatado = episodio\
.lower()\
.replace("episódio ","ep")\
.upper()\
.replace("temporada ", "s")

print(episodioFormatado)
```

Qual será a saída?

A - boku no hero academia - s1, e12

__B__ - BOKU NO HERO - TEMPORADA 1, EP12
> Correto! O upper() deixou todas as letras maiúsculas e o segundo replace() não encontrou "temporada".

C - BOKU NO HERO - S2, EP12

---

Nessa aula vimos duas formas diferentes de verificar se uma string começa com algum texto que queremos ou não, com isso em mente dê uma olhada no código abaixo.

```py
filme = "Vingadores - Era de Ulton"
filme = "Os quase Vingadores - End Game"
filme = "Detonadores  - Os Vingadores"
```

Uma forma de saber se os filmes listados são dos "Vingadores" ou não é verificando se o nome do filme começa com a palavra "Vingadores", analise as sugestões de códigos para resolver esse problema e marque a alternativa que retornaria a resposta __incorreta__ para os itens listados acima

A -
```py
filmeEhVingadores = filme.find("Vingadores")
if filmeEhVingadores == 0:
    print("Esse filme é dos vingadores")
else:
    print("Esse filme não é dos vingadores")
```

__B__ -
```py
filmeEhVingadores = filme.find("Vingadores")
if filmeEhVingadores:
    print("Esse filme é do vingadores")
else:
    print("Esse filme não é dos vingadores")
```
> Correto! Esse código não estaria certo para nenhum dos itens acima, no filme1 o find retorna 0 sendo assim a variável filmeEhVingadores iria para condição else, e nesse caso o filme é sim dos vingadores.

C -
```py
filmeEhVingadores = filme.startswith("Vingadores")
if filmeEhVingadores:
    print("Esse filme é dos vingadores")
else:
    print("Esse filme não é dos vingadores")
```

# Aula 4

O padrão abaixo identifica o episódio e a temporada de uma série que alguém está assistindo.

```py
[e][0-9]{1,2} [s,t][0-9]{1,2}
```

Vamos testá-la nas seguintes conversas:

```py
padrao = "e[0-9]{1,2} [s,t][0-9]{1,2}"
conversa1 = "Estou no e 1 t 3 de Naruto"
conversa2 = "O e02 t2 é o melhor de Rick and Morty"
conversa3 = "Eu parei GOT no e2 s3"
conversa4 = "Não gostei do ep4 t5 de Vikings"
conversa5 = "O melhor episódio de Boku no Hero é o e011 s02"
```

Marque a alternativa que o padrão correto foi retornado. A ordem está da conversa1 até a conversa5.

__A__ - "e02 t2"
> Correto! O padrão pode identificar 1 ou 2 números para episódios e para temporada.

B - "ep4 t5"

__C__ - "e2 s3"
> Correto! É possível identificar "t" ou "s" dentro do padrão buscado

D - "episódio 9 temporada 2"

E - "e011 s02"

---

Aprendemos o que é e como usar uma expressão regular em Python, com tudo que você viu em mente analise as frases abaixo.

```py
frase1 = "podemos marcar de sair sabado 23h"
frase2 = "acho que quinta 21h é a melhor hora para a gente ir lá"
frase3 = "terca 19h é um bom momento para sairmos"
```

Das expressões listadas abaixo qual consegue capturar o dia e o horário nas frases.

A -
```py
padrao = "[a-z]{20}[ ][0-9]{1,2}[h]"
```

__B__ -
```py
padrao = "[a-z]{1,20}[ ][0-9]{1,2}[h]"
```
> Correto! Essa expressão regular funciona de pega todas as possibilidades de "a" até "z" repetidos até 20 vezes, pega um espaço em branco e após isso pega 2 número em seguida a letra "h"

C -
```py
padrao = "[a]{1,20}[ ] [0-9]{3}"
```

# Aula 5

Suponha a classe abaixo:

```py
class Quadrado:
    def __init__(self,nome,lado):
        self.nome = nome
        self.lado = lado
    def __str__(self):
        return "Nome = {} Lado ={}".format(self.lado,self.nome)
```

Caso você crie a seguinte instância dessa classe:

```py
quadradinho = Quadrado("Meu Quadrado",2)
print(quadradinho)
```

Qual seria o resultado na tela?

A - "Quadrado object at 0x00000197A08142E8"

B - "Meu Quadrado Lado = 2"

__C__ - "Nome = 2 Lado = Meu Quadrado"
> Correto! Nossa classe possui um método str e os valores estão sendo mostrados em locais incorretos.

---

Vimos nessa aula os métodos especiais do Python, também chamado de métodos mágicos, esses métodos fazem parte das classes padrões do Python, como int ou str dando funcionalidades para tais classes.

Analise o código abaixo:

```py
nome = “Rodrigo Siqueira”
print (nome)
print (len(nome))
```

Com base no que vimos qual método especial não influencia no funcionamento do código acima?

__A__ - O método eq()
> Correto! Esse método é responsável por comparar duas strings diferentes, e o código acima não faz isso.

B - O método str()

C - O método len()
