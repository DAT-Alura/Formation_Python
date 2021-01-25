# URL

A URL ( Uniform Resource Locator ) é o endereço de rede onde se encontra um recurso de alguma aplicação WEB. Como vimos nessa aula, a URL pode conter algumas informações de grande importância para que nossos programas funcionem corretamente. Vejamos a url de exemplo abaixo:

https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500

Essa string pode ser divida em duas partes: "endereço"?"argumentos", sendo que a “?” é o divisor entre essas duas partes e é essa caractere que determina que os argumentos começarão a ser passados para uma aplicação.

Vamos dar um zoom no lado dos argumentos da url: "nomeArgumento1"="valorArgumento1"&"nomeArgumento2"="valorArgumento2". Aqui nós percebemos que pode ser passado mais de 1 (um) argumento e que eles são separados pelo caractere especial “&”. Além disso o argumento possui um nome e um valor que são separados pelo caractere “=”.

# Metodo format

O método format() serve para criar strings com chaves que serão substituídas por argumentos dentro do método format(). Veja o exemplo abaixo:

```py
texto = “{} é um anime excelente e já possui {} temporada”
print(texto.format(“The Rising of shield Hero”,1))
```

Os campos substituídos estão sempre associados a parâmetros que podem ser nomeados ou não, vamos repetir o exemplo mas dessa vez nomeando os argumentos dentro das chaves e dentro do método format().

```py
texto = "{anime} é um anime excelente e já possui {temporada} temporada"
print(texto.format(temporada=1,anime="The Rising of shield Hero"))
```

É possível utilizar o format para alinhar os textos e para determinar uma quantidade máxima de caracteres que podem ser exibidos. Veja a lista abaixo com alguns exemplos e seus resultados para a seguinte string: texto = “Eu gosto de pizza de {}”.format(“Calabresa”).

{0:>20} - Alinha a string à direita com 20 espaços em branco

Resposta : Eu gosto de pizza de                     Calabresa

{0:#>20} - Alinha a string à direita com 20 símbolos #

Resposta : Eu gosto de pizza de ###########Calabresa

{0:#^20} - A linha a string no centro de 20 símbolos #.

Resposta : Eu gosto de pizza de #####Calabresa######

{0:.5} - Imprime somente os 5 primeiros dígitos

Resposta : Eu gosto de pizza de Calab

Podemos encontrar mais sobre o assunto format(), sendo usado para outros tipos de variáveis na seguinte página: [Post](https://cadernoscicomp.com.br/tutorial/introducao-a-programacao-em-python-3/funcoes-print-input-e-o-metodo-format/)

# Método \_\_eq__()

Aqui temos um conteúdo muito legal para você poder aprender mais sobre esse método que pode deixar suas classes bem mais turbinadas!

[Blog Alura](https://www.alura.com.br/artigos/como-comparar-objetos-no-python)
