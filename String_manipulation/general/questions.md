# Aula 1

Nesta aula aprendemos como retirar partes de uma string utilizando slice (fatiamento). Com esse conhecimento veja o código abaixo:

```py
texto = “Izuku Midoriya”
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

Com o objetivo de retirar o código de área sem os “()”, os valores de x e y podem ser substituídos por:

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
> Correto! O tamanho da string é um inteiro maior que o último índice da mesma, então o “r” no final vai aparecer.

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
> Correto! O upper() deixou todas as letras maiúsculas e o segundo replace() não encontrou “temporada”.

C - BOKU NO HERO - S2, EP12

---

Nessa aula vimos duas formas diferentes de verificar se uma string começa com algum texto que queremos ou não, com isso em mente dê uma olhada no código abaixo.

```py
filme = "Vingadores - Era de Ulton"
filme = "Os quase Vingadores - End Game"
filme = "Detonadores  - Os Vingadores"
```

Uma forma de saber se os filmes listados são dos “Vingadores” ou não é verificando se o nome do filme começa com a palavra “Vingadores”, analise as sugestões de códigos para resolver esse problema e marque a alternativa que retornaria a resposta __incorreta__ para os itens listados acima

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
