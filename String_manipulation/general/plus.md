# URL

A URL ( Uniform Resource Locator ) é o endereço de rede onde se encontra um recurso de alguma aplicação WEB. Como vimos nessa aula, a URL pode conter algumas informações de grande importância para que nossos programas funcionem corretamente. Vejamos a url de exemplo abaixo:

https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500

Essa string pode ser divida em duas partes: "endereço"?"argumentos", sendo que a “?” é o divisor entre essas duas partes e é essa caractere que determina que os argumentos começarão a ser passados para uma aplicação.

Vamos dar um zoom no lado dos argumentos da url: "nomeArgumento1"="valorArgumento1"&"nomeArgumento2"="valorArgumento2". Aqui nós percebemos que pode ser passado mais de 1 (um) argumento e que eles são separados pelo caractere especial “&”. Além disso o argumento possui um nome e um valor que são separados pelo caractere “=”.
