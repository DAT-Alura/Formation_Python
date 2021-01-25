# Perguntas

## Aula 1

1 - Qual é a função utilizada para imprimir algo na tela?
- puts()
- println()
- __print()__
- printf()

> A função é a print(). Basta passar a mensagem como parâmetro para a função, que a mensagem será impressa. Ela inclusive apareceu várias vezes no vídeo!

2 - Veja o código a seguir:
``` py
>>> subst = "Python"
>>> verbo = "é"
>>> adjetivo = "fantástico"
>>> print(subst, verbo, adjetivo, sep="_", end="!\n")
```
Qual será a saída do comando print?
- __Python_é_fantástico!__
- Python é fantástico!
- Python!é!fantástico_
- Python_é_fantástico

> Repare que usamos o parâmetro sep="_" para definir um _ entre cada valor, por isso é impresso:
> 
> ``` py
> Python_é_fantástico
> ```
> 
> Além disso, definimos através do end para imprimir uma exclamação (!), seguida pelo \n:
> 
> ``` py
> end="!\n"
> ```
> 
> Lembrando que o \n é um caractere especial, que faz com que o novo prompt comece em uma nova linha.
> 
> Com isso recebemos a saída:
> 
> ``` py
> Python_é_fantástico!
> >>>
> ```

3 - Para representar uma data, temos as variáveis dia, mes e ano:
``` py
>>> dia = 15
>>> mes = 10
>>> ano = 2015
```
Sem alterar as variáveis e sem passar nenhuma string adicional à função print(), como faríamos para ter como resultado da impressão, uma data formatada:

```
15/10/2015
```

Para ver a resposta do instrutor, basta clicar em Continuar.

- __print(dia, mes, ano, sep="/")__

> Podemos alterar o separador entre os valores que a função print() recebe, utilizando o parâmetro sep, que por padrão é um espaço em branco. Basta utilizá-lo, dizendo que seu valor será uma barra (/):
> ``` py
> >>> dia = 15
> >>> mes = 10
> >>> ano = 2015
> >>> print(dia, mes, ano, sep="/")
> 15/10/2015
> ```

4 - Temos a seguinte variável, que representa o preço de um produto:
``` py
preco = 49.99
```
Qual será o tipo da variável preco? Faça o teste!
- int
- double
- __float__
- decimal

> O valor 49.99, é um número decimal, ou seja, com um ponto flutuante, por isso em Python o seu tipo será o float. Podemos verificar isso no console do Python:
> ``` py
> >>> preco = 49.99
> >>> type(preco)
> <class 'float'>
> ```

5 - Sabendo que o Python usa uma tipagem dinâmica, qual alternativa abaixo é correta?
- __Uma variável só passa a existir quando atribuímos um valor.__
> Correto! É preciso atribuir um valor para inicializar uma variável, definindo assim o seu tipo.
- Uma variável passa a existir ao ser declarada, sem necessariamente termos atribuído um valor para ela, nem o tipo.
- Python permite declaração estática/explícita de variáveis.

> Não há declaração de variáveis estáticas em Python, como em linguagens como C, Java ou C#. Nessas linguagens, indicamos o tipo e o nome das variáveis e ela já passa a existir.
> Por exemplo:
> ``` py
> int idade;
> ```
> Repare que só declaramos o tipo e o nome da variável, sem ter atribuído o valor.
> Em Python, a variável só passa a existir quando atribuímos um valor, como no exemplo abaixo:
> ``` py
> idade = 12
> ```
> Isso faz todo sentido, já que não temos uma declaração explícita do tipo, como na linguagem Java ou C#. O interpretador do Python não tem como assumir um tipo.

## Aula 2

1 - Romário, seguindo o que foi aprendido neste curso, resolveu testar o código que compara o chute digitado pelo usuário com um número secreto definido no programa.
``` py
numero_secreto = 42
chute = input("Digite seu número")
print("Você digitou ", chute)
if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")
```
Com base no código de Romário, temos as seguintes afirmações:

a) Sempre exibirá a mensagem Você errou, independentemente se o chute for igual ao número secreto

b) Todo valor retornado pela função input é um número.

c) É necessário converter o retorno de input para um número, no caso, um inteiro.

Sobre as afirmações anteriores, podemos dizer que:
- __Apenas B é falsa.__
- Apenas C é falsa.
- Apenas A é falsa.

> Não importa o número digitado, a comparação com == envolvendo tipos diferentes resultará em falso. Isso porque a função input sempre retorna um texto (string). Sendo assim, é necessário converter o valor retornado em inteiro, para que a comparação com outro inteiro, no caso o numero_secreto, seja possível. Realizamos essa conversão através da função int.
> Corrigindo o código:
> ``` py
> numero_secreto = 42
> chute_str = input("Digite seu número")
> chute = int(chute_str)
> print("Você digitou ", chute)
> if(numero_secreto == chute):
>     print("Você acertou")
> else:
>     print("Você errou")
> ```
> No lugar de criarmos outra variável, usamos a mesma para receber o valor da sua conversão.

2 - Fernanda, colocando em prática o que aprendeu neste capítulo, escreveu o seguinte código para testar se realmente aprendeu a criar uma condição if em seu código:
``` py
minha_idade = 26
idade_namorado = 25
if(minha_idade == idade_namorado)
    print('temos idades iguais')
else:
    print('temos idades diferentes')
```
O problema é que o código dela não funciona. Consegue enxergar onde está o problema? Para quem está começando com Python, pode ser bem sutil. Descobriu? Clique em Ver Opinião do Instrutor, que você verá a resposta do instrutor.

- __Está faltando o ":" no final da linha do if__

>O problema é que para indicar o início do bloco if, é necessário utilizar dois pontos (:). Veja que no código dele faltou os dois pontos. O código corrigido ficará assim:
> ``` py
> minha_idade = 26
> idade_namorado = 25
> if(minha_idade == idade_namorado):
>     print('temos idades iguais')
> else:
>     print('temos idades diferentes')
> ```
> Importante também é sempre usar a indentação correta. Ou seja, depois da linha com o if, devemos usar 4 espaços ou pressionar a tecla tab para começar o novo bloco de código.

3 - Romeu fez uma simples comparação entre números, mas que não funciona. Segue o código:
``` py
numero1 = 10
numero2 = 10
if(numero1 = numero2):
    print("São números iguais")
```
Consegue descobrir onde Romeu errou? Pense bem para em seguida clicar em Ver Opinião do Instrutor e ver a resposta do instrutor.

- __Em vez de utilizar "==" ele utilizou "=" que significa atribuição em vez de ter usado o simbolo duplo que significa comparação__

> O problema é que foi usado um = para realizar a comparação. Quando usamos apenas um =, estamos atribuindo um valor à variável. Para compararmos valores ou variáveis, usamos o ==. Sendo assim, para o código do Romeu funcionar:
> ``` py
> numero1 = 10
> numero2 = 10
> if(numero1 == numero2):
>     print("São números iguais")
> ```

4 - Temos o seguinte código:
``` py
idade1 = 10
idade2 = "20"
print(idade1 + idade2)
```
Qual das opções abaixo possui o resultado do código? Fique à vontade de testar esse código no console do Python.
- "1020"
- 30
- __O código não funciona!__

> O código na verdade não funciona, e exibe a seguinte mensagem de erro no console:
> ``` py
> unsupported operand type(s) for +: 'int' and 'str'
> ```
> Isso acontece porque não podemos realizar uma operação de soma envolvendo uma string. Para resolvermos o problema, podemos apelar para a função int(), que converte uma string que contém um número, em um número inteiro:
> ``` py
> idade1 = 10
> idade2 = int("20")
> print(idade1 + idade2)
> ```

5 - Temos o seguinte trecho de código:
``` py
nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)
```
O resultado da operação é:
- Não é possível concatenar as duas variáveis.
- Nico Steppat
- __NicoSteppat__

> A resposta correta é NicoSteppat.
> O caractere + aqui não tem o significado de somar e sim de concatenar. Estamos concatenando (juntando) duas strings!
> Repare também que não há espaço entre as palavras. Para que haja, basta fazer assim:
> ``` py
> nome = "Nico"
> sobrenome = "Steppat"
> print(nome, sobrenome)
> ```
> Lembrando que a função print automaticamente aplica um separador entre os valores. O separador é um espaço por padrão, mas pode ser reconfigurado pelo parâmetro sep:
> ``` py
> nome = "Nico"
> sobrenome = "Steppat"
> print(nome, sobrenome, sep="_")
> ```

6 - Quais funções existem no Python 3?
- raw_input(..)
- __input(...)__
- __print(...)__
- __int(...)__

> As funções input(...), print(...) e int(...) existem no Python 3.
> A função raw_input(..) existe apenas no Python 2.

7 - Marque todas as alternativas verdadeiras:
- __No Python 3, a instrução print("ola", "mundo") imprime como saída ola mundo, diferente do Python 2, que possui como saída ('ola', 'mundo').__
- No Python 2, a função print aceita o parâmetro nomeado sep.
- __No Python 2, quando digitamos um valor numérico através de input, ele automaticamente converte de str para int. Já o Python 3 não assume essa conversão automática, sendo o desenvolvedor responsável por fazê-la.__
- __A função raw_input só existe em Python 2 e quando usada, lê a entrada como str, sem realizar conversões de tipos, como na função input.__
- __Uma função em Python 3 sempre deve possuir parênteses.__

## Aula 3

1 - Considere o programa abaixo:

``` py
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")
```
Quando o usuário digitar 12, o que será mostrado no console?
- O programa não irá rodar.
- Será impresso Você é um adolescente.
- __Nada.__
- Será impresso Você é maior de idade.
- Será impresso Você é uma criança.

> Quando o usuário digitar 12, nenhuma condição será satisfeita! Repare que:
> 
> - 12 não é maior que 18 (idade > 18).
> - 12 não é menor que 12 (idade < 12).
> - 12 não é maior que 12 (idade > 12).
> 
> É preciso testar a igualdade através do ==.
> 
> Saiba também, que além do == (igualdade), > (maior) e < (menor), também temos >= (maior ou igual), <= (menor ou > igual) e != (diferente).
> 
> Seguem todas as operadores de comparação:
> 
> - < - menor que
> - \> - maior que
> - <= - menor ou igual a
> - \>= - maior ou igual a
> - == - igual a
> - != - diferente de

2 - Considere o programa abaixo:
``` py
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca     = idade < 12
adolescente = idade > 12
```
Quando o usuário digitar 15, o valor das variáveis maior_idade, crianca e adolescente será, respectivamente:
- True, True, False
- __False, False, True__
- True, False, False
- False, False, False
- 0, 0, 1

> Para a idade = 15:
> 
> - maior_idade: 15 > 18 (False)
> - crianca: 15 < 12 (False)
> - adolescente: 15 > 12 (True)

3 - Henrique, mesmo dando os primeiros passos com a linguagem Python, decidiu criar um sistema de identificação de usuários. É claro que em uma aplicação real é necessário acessar o banco de dados, entre outras coisas, mas usando o que ele já aprendeu, ele conseguiu algo parecido. Esse é o código do aluno:
``` py
usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
else(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
else(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")
```
A ideia de Henrique é simples, porém não muito eficiente. Ele quer aceitar apenas os usuários Flávio, Douglas e Nico. No entanto, seu código não funciona!

Consegue identificar a razão? Quebre a cabeça um pouquinho.

- __Existem 2 "else" que de deveriam ser "elif"__

> O problema é que a instrução else não aceita receber uma condição. Nesse caso, para resolver o problema do código, precisamos trocar para a instrução elif:
> ``` py
> usuario = input("Informe o usuário do sistema!")
> 
> if(usuario == "Flávio"):
>     print("Seja bem-vindo Flávio!")
> elif(usuario == "Douglas"):
>     print("Seja bem-vindo Douglas!")
> elif(usuario == "Nico"):
>     print("Seja bem-vindo Nico")
> else:
>     print("Usuário não identificado!")
> ```
> Veja que deixamos apenas um else que não recebe qualquer condição. Também tem que ser assim, porque se o usuário identificado não for nenhum dos que listamos, imprimimos na tela "Usuário não identificado".

4 - No exercício, você usou a variável acertou:
``` py
acertou = (chute == numero_secreto)
```
Qual é o tipo dessa variável? Faça o teste!
- bytes
- int
- __bool__
- str

> A variável acertou é do tipo bool.
> Uma variável do tipo bool pode ter apenas dois valores, True ou False, que podemos usar diretamente:
> ``` py
> passou = True
> errou = False
> ```

## Aula 4

1 - Temos o seguinte código:
``` py
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 2
    if(contador == 5):
        contador = contador + 2
```
Apenas olhando este código, sem executá-lo, qual será a saída no console?
- A
``` bash
1
3
5
7
9
```

- B
``` bash
1
2
3
4
6
7
8
9
```

- C
``` bash
1
3
7
9
11
```

- __D__
``` bash
1
3
7
9
```

> Se você achou que o 5 seria impresso, errou. Isto porque no if(contador == 5), adicionamos novamente 2 ao contador.

2 - O que o if e while tem em comum?
- __Ambos possuem uma condição de entrada.__
- Ambos servem para testar uma condição e executar um bloco uma única vez.
- Ambos possuem uma condição de saída.
- Ambos servem para testar uma condição e executar um bloco enquanto a condição for verdadeira.

> Ambos, if e while, possuem uma condição de entrada. A diferença é que o if executa o bloco apenas uma vez, mas o while repete o bloco enquanto a condição for verdadeira.
> O interessante é que o Python não possui um laço com uma condição de saída, que outras linguagens chamam de do-while.

3 - Veja a declaração das 4 variáveis:
``` py
dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017
```
Pedro precisa criar a seguinte string:

```"Em 2017 o Carnaval acontece em fevereiro do dia 24 até o dia 28"```

Qual é a formatação correta para produzir a string acima?
- A
```"Em [] o Carnaval acontece em [] do dia [] até o dia []".format(ano, mes, dia_ini, dia_fim)```
- B
```"Em {} o Carnaval acontece em {} do dia {} até o dia {}"```
- __C__
```"Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim)```
- D
```"Em {ano} o Carnaval acontece em {mes} do dia {dia_ini} até o dia {dia_fim}".format()```

> Dentro da string, devemos utilizar as chaves ({}) para definir onde o valor da variável deve ser inserido. E logo após a definição da string, chamamos a função format, que recebe as variáveis/parâmetros na ordem de inserção:
> ``` py
> "Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim)
> ```
> No próximo capítulo veremos mais detalhes sobre essa formatação, que também é chamada de interpolação.

## Aula 5

1 - Temos o seguinte loop usando while:
``` py
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 1
```
Qual das opções abaixo possui o mesmo resultado usando for .. range?
- A
``` py
for contador in range(1, 10):
    print(contador)
```

- __B__
``` py
for contador in range(1, 11):
    print(contador)
```

- C
``` py
for contador range in(1, 11):
    print(contador)
```

> Muito cuidado com o for .. range. A posição final é não-inclusiva, por isso que para imprimirmos de 1 até 10, usamos 11 como posição final:
> ``` py
> for contador in range(1, 11):
>     print(contador)
> ```

2 - Temos o seguinte código:
``` py
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 3
```
Que imprime:
``` bash
1
4
7
10
```
Como você poderia substituir o código acima usando o laço for .. range?
- __A__
``` py
for contador in range(1, 11, 3):
    print(contador)
```
> Correto! Utilizando o range com um step 3.

- B
``` py
for contador in range(1, 11):
    print(contador)
```

- C
``` py
for contador in range(1, 11, 4):
    print(contador)
```

- D
``` py
for contador in (1, 11, 3):
    print(contador)
```

> A função range possui os seguintes parâmetros:
> ``` py
> range(start, stop, [step])
> ```
> Onde o step é opcional. Como queremos "pular" de 3 em 3, começando com 1 (start) até 10 (stop), podemos escrever:
> ``` py
> for contador in range(1, 11, 3):
>     print(contador)
> ```

3 - Dentro de um laço, qual é a diferença entre break e continue?
- continue sai do bloco do laço abruptamente, break apenas pula para próxima iteração.
- break é utilizado no laço for, continue no laço while.
- __break sai do bloco do laço abruptamente, continue apenas pula para próxima iteração.__
- Não tem diferença entre break e continue, ambos pulam para próxima iteração.

> Para controlar melhor os laços, existem os comandos break e continue, que são utilizados dentro de um laço (for ou while). Ambos fazem parte do controle de fluxo (control flow).
> A diferença é que o break, quando for executado, sai do bloco do laço abruptamente, enquanto continue apenas pula para próxima iteração.

4 - Temos o seguinte código:
``` py
i = 1
while(i <= 7):
    print(i)
    i = i + 1
    if(i == 5):
        break
```
Apenas olhando esse código, sem executá-lo, qual será a saída no console?
- A
``` bash
1
2
3
4
5
```

- B
``` bash
1
2
3
4
5
6
7
```

- __C__
``` bash
1
2
3
4
```

> A saída será:
> ``` bash
> 1
> 2
> 3
> 4
> ```
> Se você achou que o 5 seria impresso, errou. Isso porque a condição if, que executa o break (que rompe o laço da iteração), é executada após o incremento da variável i, sendo assim, quando o valor dela for 5, paramos a repetição antes que o programa tenha chance de imprimir o valor 5.

5 - E se fosse o código abaixo usando for e continue?
``` py
for i in range(1,8):
    if(i == 5):
        continue
    print(i)
```
Qual será a saída no console?
- A
``` bash
1
2
3
4
6
7
```
> Correto! Pulamos apenas a iteração 5.

- B
``` bash
1
2
3
4
```

- C
``` bash
1
2
3
4
5
6
7
```

> Pulamos apenas a iteração 5. A saída será:
> ``` bash
> 1
> 2
> 3
> 4
> 6
> 7
> ```

6 - Um desenvolvedor Python está tendo que adaptar um sistema americano de cadastro de clientes americanos para os clientes brasileiros. Ele está esbarrando em um problema, pois lá as pessoas têm o costume de se referir pelo sobrenome antes do primeiro nome, por exemplo: Smith, John .

Ele deseja adaptar as mensagens do sistema para o padrão brasileiro, mas sem alterar a estrutura de dados que ele recebe do banco de dados.

Digamos que ele queira exibir a seguinte mensagem: "Ola Sr. Leonardo Cordeiro", como ele pode formatar a string para obter o resultado desejado?
- A
``` py
print("Ola Sr.{-1} {1}".format("Cordeiro","Leonardo"))
```
- B
``` py
print("Ola Sr.{2} {1}".format("Cordeiro","Leonardo"))
```
- __C__
``` py
print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))
```
- D
``` py
print("Ola Sr.{0} {1}".format("Cordeiro","Leonardo"))
```

> Com o .format(), podemos especificar a ordem em que os parâmetros aparecem na string, basta apenas colocar entre as chaves ({}) da string formatada qual parâmetro você quer exibir. É válido lembrar também, que o primeiro parâmetro é o zero, pois tradicionalmente na computação começamos contando de zero, ou seja, no nosso caso:
> ``` py
> print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))
> ```
> O primeiro parâmetro, representado pelo 0** é Cordeiro, e o segundo, que é o **1, é o Leonardo. Assim, formatando a string, na hora de imprimir será exibido:
> ``` bash
> "Ola Sr. Leonardo Cordeiro"
> ```

7 - Temos as seguintes instruções:
``` py
"R$ {:7.1f}".format(1000.12)
"R$ {:07.2f}".format(4.11)
```
Será impresso respectivamente no console:
- A
``` bash
R$ 1000.1
R$ 0004.11
```

- B
``` bash
R$ 1000.12
R$    4.1
```

- C
``` bash
R$ 1000.12
R$ 0004.11
```

> A resposta correta é:
> ``` bash
> R$  1000.1
> R$ 0004.11
> ```
> Vejamos:
> ``` py
> "R$ {:7.1f}".format(1000.12)
> ```
> No exemplo acima, queremos um número com 7 casas inteiras, sendo uma delas decimal, resultado é R$ 1000.1
> ``` py
> "R$ {:07.2f}".format(4.11)
> ```
> Neste exemplo, queremos um número com 7 casas inteiras, sendo duas delas decimais, resultado é R$ 0004.11. Como colocamos um número de casas inteiras superior a quantidade de casas inteiras do número, o Python coloca 0 (zeros) à esquerda. Interessante também é que a função format até arredonda, por exemplo:
> ``` py
> "R$ {:7.1f}".format(1000.16)
> ```
> Retorna:
> ``` bash
> R$  1000.2
> ```

## Aula 6

1 - Vimos no video que foi necessário importar o módulo random:
``` py
import random
```
Por que foi necessário usar o comando import?
- Porque devemos cachear o módulo random para melhorar o desempenho.
- __Porque o módulo random não está automaticamente disponível dentro do programa, só após importação.__
- Porque o random é uma função built-in.

> Diferentemente das funções built-in, o módulo random precisa ser explicitamente importado no seu programa.
> Existem vários módulos no Python para resolver diversos problemas como trabalhar com arquivos, datas ou expressões regulares. Python é muito rico nesse sentido e o programador pode usufruir essas bibliotecas:
> https://docs.python.org/3/library/

2 - Qual é o menor e o maior número possível que o script abaixo consegue imprimir ?
``` py
import random

aleatorio = random.randrange(10)
print(aleatorio)
```
- Menor: 1 e Maior: 10
- Menor: Não definido e Maior: 10
- __Menor: 0 e Maior: 9__
- Nenhuma das outras alternativas.
- Menor: 1 e Maior: 9

> A função random.randrange() quando só possuí um parâmetro supõe que você quer dizer de zero até número passado -1, ou seja, neste caso, o menor número possível quando fazemos:
> ``` py
> random.randrange(10)
> ```
> É o zero e o maior número possível é o 9.

3 - Selecione todas as opções abaixo que são uma instrução do Python capaz de gerar um número inteiro aleatório entre 0 e 100 (incluindo 100, ou seja [0,100]):
- __int(random.random() * 101);__
- round(random.random() * 101);
- __round(random.random() * 100);__
- __random.randrange(0,101)__
- random.randrange(1,100)

> Apesar da função random.randrange() já resolver bem os nossos problemas, é sempre bom conhecer diferentes modos de resolvê-los. Isto nos torna desenvolvedores criativos e capazes de encarar qualquer código que encontrarmos por aí!

4 - O professor Flávio tem o costume de sortear um livro da Casa do Código ao final de todos os seus cursos para os seus 3 melhores alunos. Desta vez, os três melhores alunos foram:
``` py
Paulo
Juliana
Tamires
```
Para realizar o sorteio, foi utilizado o seguinte script em Python para determinar o vencedor:
``` py
import random

sorteado = random.randrange(0,4)

print(sorteado)

if sorteado == 1:
    print( "Paulo")
elif sorteado == 2:
    print("Juliana")
else:
    print("Tamires")
```
Quando executado o script foi anunciado que a Tamires era a vencedora, porém Paulo após conferir o código exclamou que o sorteio não era justo e que ele e a Juliana tinham menos chances de ganhar!

De acordo com seus conhecimentos de Python, analise o código acima e avalie se o sorteio foi justo ou não e dê uma justificativa para tal!

- O sorteio foi justo, afinal os possíveis números retornados são 0, 1 e 2, e cada uma das pessoas está associada a um número.
- O sorteio foi justo, afinal os possíveis números retornados são 1, 2 e 3 e cada uma das pessoas está associada a um número.
- __O sorteio foi injusto, afinal os possíveis números retornados são 0, 1, 2 e 3 , e como o Paulo e a Juliana estão associadas a apenas um número cada sobram ainda outros dois para Tamires poder ganhar.__

> A verdade é que o sorteio não foi justo pois a Tamires realmente tinha mais chance de ganhar! A função random.randrange nos retorna um número no intervalo especificado. Nesse exemplo, temos como saída os possíveis valores 0, 1, 2 e 3. Como o Paulo está associado ao valor 1 e a Juliana ao valor 2, sobram mais dois possíveis valores para a Tamires poder ganhar ( 0 ou 3 ).
> Quando estamos trabalhando com números aleatórios, é importante observar bem o resultado das nossas funções e como se comporta nosso código, além de entender sobre aleatoriedade. Neste caso o sorteio era apenas de um livro, porém em sistemas de verdade pode ser que o efeito de um sorteio indesejado possa beneficiar acidentalmente uma certa pessoa ou até mesmo [causar prejuízos à sua empresa](https://www.engadget.com/2010-12-29-hackers-obtain-ps3-private-cryptography-key-due-to-epic-programm.html).

## Aula 7

1 - Já vimos algumas funções built-in nesse curso!
O que sabemos sobre essas funções built-in? Assinale a afirmação correta!

- Fazem parte da biblioteca padrão do Python, mas não podem ser chamadas em qualquer lugar.
- Fazem parte da biblioteca padrão do Python, mas precisam ser importadas.
- __Estão automaticamente disponíveis e podem ser chamadas em todo lugar do nosso código.__
- São apenas as funções: print(..) type(..), abs(), input(..) e int.

> As funções built-in podem ser chamadas a qualquer momento, em todos os lugares. Exemplo de funções são type(..), abs(), input(..) ou int.
> Segue também o link da documentação (em inglês): https://docs.python.org/3/library/functions.html

2 - Vimos no vídeo como calcular a pontuação do jogador. O cálculo foi simples e usamos a função abs():
``` py
pontos_perdidos = abs(chute - numero_secreto)   #pontos perdidos da rodada
pontos = pontos - pontos_perdidos               #subtraindo os pontos perdidos da pontuação total 
```
Vamos mudar um pouco esse cálculo dos pontos perdidos. Agora não basta apenas calcular o valor absoluto, devemos também dividir esse valor por 3.
``` py
pontos_perdidos = abs(chute - numero_secreto) / 3     #dividindo por três
```
Nada complicado aqui, mas pode surgir uma outra questão. Imagine que o chute é 21 e o número secreto é 32. Isso daria a seguinte conta:
``` py
pontos_perdidos = abs(21 - 32) / 3     #dividindo por três
```
Que é:
``` py
pontos_perdidos = 11 / 3
```
Será que o Python consegue dividir 11 por 3? Se sim, qual será o tipo da variável pontos_perdidos? Faça o teste!

- Não consegue e dá erro.
- Consegue sim e o tipo será int.
- Consegue sim e o tipo será number.
- __Consegue sim e o tipo será float.__

> Você pode testar isso facilmente no console do Python3:
> ``` py
> >>> pontos_perdidos = 11 / 3
> >>> type(pontos_perdidos)
> <class 'float'>
> ```
> Agora temos um outro problema. Ao imprimir esse cálculo, percebemos muitas casas decimais:
> ``` py
> >>> print(pontos_perdidos)
> 3.6666666666666665
> ```
> Bom, já aprendemos a formatar números decimais (lembre-se do {:7.2f}), mas nesse caso não é uma questão de formatação! Gostaríamos de arredondar o número, ou seja o valor decimal 3.66666 deve ser transformado para o valor 4.
> Será que você se lembra da função built-in para o arredondamento?

3 - Nos exercícios falamos sobre a divisão entre dois inteiros. Para ilustrar, execute no console:
``` py
>>>  3 / 2
1.5
```
Repare que recebemos o valor float 1.5 como resposta. O operador / sempre traz um float, mesmo se não for necessário, por isso ele também é chamado de float division:
``` py
>>>  2 / 2
1.0
```
No entanto, existe um outro operador bem parecido, o //. Tente executar:
``` py
>>>  3 // 2
```
Qual foi o resultado?

- __1__
- 2
- 1.5

> O resultado é 1, um valor inteiro (int).
> O operador // também é chamado integer division e sempre devolve o valor inteiro (sem arredondar).
> Para realmente concluir o tópico, saiba que o Python 2 só tem integer division, mesmo tendo os dois operadores / e // ! No Python 2 não existe diferença entre os dois operadores, veja o exemplo:
> ![operadores-divisao](imagens/operadores-divisao.png)

## Aula 8

1 - Marlon criou dois arquivos chamados a.py e b.py. Segue conteúdo de cada um:
``` py
# arquivo a.py
print('executando a')
```
``` py
# arquivo b.py
print('executando b')
```
Ele ainda criou um terceiro arquivo chamado principal.py. Para testar se aprendeu corretamente a importar um módulo criado por ele mesmo, ele fez o seguinte em principal.py
``` py
# principal.py

import a
import b
```
O que acontecerá quando Marlon executar através do terminal o programa principal.py?

- __A__
Será exibido os textos:
``` py
executando a
executando b
```

- B
Será exibido apenas
``` py
executando b
```

- C
Nada será exibido

- D
Será exibido apenas
``` py
executando a
```

> Quando importamos um módulo em Python, a primeira coisa que a nossa linguagem favorita fará é executar o conteúdo de cada módulo importado.

2 - Fernanda, assim como seu amigo Marlon, criou dois arquivos chamados a.py e b.py. Segue o conteúdo de cada um:
``` py
# arquivo a.py
def executa():
    print("Executando a")
```
``` py
# arquivo b.py
def executa():
    print("Executando b")
```
Ela criou também aquele terceiro arquivo chamado principal.py. Para testar se aprendeu corretamente a importar um módulo criado por ela mesmo, ela fez o seguinte em principal.py
``` py
# principal.py

import a
import b
```
Agora qual é a saída ao executar o arquivo principal.py?

- A
Um erro acontecerá.

- B
Será exibido os textos:
``` py
executando a
executando b
```

- __C__
Nada será exibido.

> Como os códigos dos arquivo a.py e b.by foram definidos dentro de uma função, sendo assim, a importação de a e b por principal não executa automaticamente o código contido neles. Para isso, precisamos explicitar que queremos executar esses código em principal. Vejamos:
> ``` py
> # principal.py
> 
> import a
> import b
> 
> a.executa()
> b.executa()
> ```

3 - Kellen criou o seguinte módulo no arquivo a.py:
``` py
# arquivo a.py
def executa():
    print("Executando a")
```
Aprendemos a importar um módulo, inclusive a chamar uma função específica desse módulo. No entanto, Kellen deseja usar a.py independente de outros módulos, ou seja, quer ser capaz de chamá-lo através do console, como:
``` py
python a.py
```
Qual das opções abaixo possui a modificação correta de a.py para que seja possível chamar o arquivo diretamente do terminal?

- A
``` py
def executa():
    print("Executando a")

if(__name__ = "__main__"):
    executa()
```

- B
``` py
def executa():
    print("Executando a")

if(__name__ == "_main_"):
    executa()
```

- __C__
``` py
def executa():
    print("Executando a")

if(__name__ == "__main__"):
    executa()
```

- D
``` py
def executa():
    print("Executando a")

if(_name_ == "__main__"):
    executa()
```

> Mesmo um módulo solitário pode executar alguma funcionalidade quando executado isoladamente, basta adicionar um if no final do código para verificar a variável __name__:
> ``` py
> def executa():
>     print("Executando a")
> 
> if(__name__ == "__main__"):
>     executa()
> ```
