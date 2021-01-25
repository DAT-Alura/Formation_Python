# Perguntas

## Aula 1

1 - Gustavo decidiu praticar o que aprendeu no vídeo deste capítulo e escreveu o seguinte código. Leia-o atentamente:
```py
def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    palavra_secreta = "banana"
    enforcou = false
    acertou = false

    while(Not enforcou and Not acertou):
        print("jogando...")

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()
```
No entanto, seu código não funcionou. Sem executar o programa, apenas olhando o código anterior, podemos afirmar que a quantidade de erros cometidos é:

- 3
- __4__
> São quatro erros. Os valores lógicos das variáveis enforcou e acertou iniciam com letra minúscula. O correto é maiúscula como True e False. Já o operador not foi utilizado duas vezes começando com letra maiúscula, quando no correto é minúscula.
- 2

2 - Qual é o tipo que representa verdadeiro ou falso no mundo Python?

- __bool__
> Correto! O tipo se chama bool!
- int
- bool()
- boolean

> Devemos utilizar o tipo bool para representar verdadeiro (True) e falso (False), por exemplo:
> 
> ```>>> existe = True```  
> ```>>> type(existe)```  
> ```<class 'bool'>```
> 
> Dica: Nesse tipo de perguntas, sinta-se sempre à vontade de usar a documentação do Python. Aliás, aconselhamos a usar a documentação para se acostumar. É um documento bastante técnico e menos didático, mas ajuda tirar dúvidas pontuais: https://docs.python.org/3.5/index.html

## Aula 2

1 - Temos a seguinte variável declarada, que armazena uma string:
```py
palavra = "aluracursos"
```
Com base na variável declarada anteriormente, marque somente as verdadeiras:

- palavra.find('s') # resultado é 9
- __palavra.find("l") # resultado é 1__
> Correto! Lembrando que as posições começam de 0 até o tamanho da string menos um. A posição 1 é a segunda letra, logo "l".
- palavra.find("a") # resultado é 4
- __palavra.find("b") # resultado é -1__
> Correto! Quando a busca nada encontra, o resultado é sempre -1.

> A função find encontra a primeira ocorrência do texto que estamos procurando e devolve o índice. Lembrando também que o índice começa com 0.
> 
> O find também aceita um segundo parâmetro, que define a partir de qual posição gostaríamos de começar, por exemplo:
> ```py
> >>> palavra = "aluracursos"
> >>> palavra.find("a",1) #procurando "a" a partir da segunda posição 
> 4
> ```

2 - Uma palavra nada mais é do que uma sequência de caracteres. Tanto isso é verdade, que podemos usar o laço for para iterar. Nesse contexto iterar significa receber em cada iteração uma letra da palavra.
Sabendo disso, qual das opções abaixo itera corretamente através da palavra Alura?

- A
```py
palavra = "Alura"
for letra in palavra:
    if(letra == "l"):
    print("Achou!")
```

- __B__
```py
palavra = "Alura"
for letra in palavra:
    if(letra == "l"):
        print("Achou!")
```
> Correto! Respeita a indentação do Python.

- C
```py
palavra = "Alura"
for palavra in letra:
    if(letra == "l"):
        print("Achou!")
```

> Nesse curso vamos falar ainda muito mais sobre sequências, mas já saiba que uma string não é a única sequência no mundo Python!

3 - Vamos recordar um exemplo de formatação de strings em Python:
```py
a = "Cavalo"
b = "Calopsita"
"{} e {}".format(b, a)
```
O que será exibido no terminal?

- 'Calopsita Cavalo'
- 'Cavalo e Calopsita'
- __'Calopsita e Cavalo'__
> Correto! Nossa string possui duas lacunas definidas com {}. Os parâmetros passados para a função format são passados na mesma ordem para preencherem a lacuna.

4 - Clarice aprendeu que strings não são apenas um local onde armazenamos informações, elas também sabem executar tarefas. Por exemplo, ela aprendeu a usar .format para formatar uma string.

Ela decidiu experimentar usar .capitalize no seguinte exemplo:
```py
nome = "clarice"
nome.capitalize()
```
No entanto, ao imprimir a variável nome, logo depois da instrução nome.capitalize(), a variável continuou com a primeira letra minúscula:
```py
nome = "clarice"
nome.capitalize()
print(nome) ## continua como clarice e não Clarice como ela esperava
```
Marque a opção abaixo que corrige o código de Clarice para que o resultado de print(nome) seja seu nome iniciando com a letra maiúscula.

- __A__
```py
nome = "clarice"
nome = nome.capitalize()
print(nome)
```
> Correto! Quando chamamos capitalize, no lugar dela alterar a variável, ela devolve um novo texto modificado. É por isso que precisamos capturar o retorno de capitalize() na própria variável, para que ela passe a apontar para o novo valor.
- B
```py
nome = "clarice"
nome.capitalize(nome)
print(nome)
```
- C
```py
nome = "clarice"
nome2 = nome.capitalize()
print(nome)
```

## Aula 3

1 - Mariana montou o seguinte código Python para controlar se a sua barraca de frutas possui determinadas frutas solicitadas pelos seus clientes:
```py
# coding: utf-8
frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar ?')

if(#####):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')
```
Qual código deve substituir o hasheado (#####) para que o programa funcione de modo esperado ?

- frutas contains frutaPedida
- frutaPedida not in frutas
- frutas has frutaPedida
- __fruta_pedida in frutas__
> Correto! Assim como nas Strings, podemos utilizar o operador in para verificar se um determinado elemento está dentro de uma lista.

> Para verificar se um determinado elemento existe em uma Lista, podemos utilizar o operador in. Ele nos retorna True ou False caso o elemento esteja ou não dentro da lista verificada, tornado este processo de verificação bem simples!
> O Python é uma linguagem de programação que nos facilita muito para trabalhar com estruturas de dados, pois ele já tem diversas funções e operadores que auxiliam as tarefas mais comuns em trabalhar com Listas e Strings , nos tornando programadores muito produtivos.

2 - Douglas deseja comprar um celular novo e tem monitorado o preço do celular desejado através de um pequeno script de Python.
Ele salva todos os dias o preço atual do celular que ele deseja, e como ele monitora o preço de várias lojas e já está namorando este celular há muito tempo, ele acabou com uma lista muito grande, veja:
```py
precos = [
    1525,1120,1464,1200,1330,1356,1312,1531,1232,1234,1250,1114,1553,
    1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,
    1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,
    1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026
]
```
Recentemente ele esbarrou com uma promoção e o celular está custando R$ 1025. Ele ficou interessado e quer saber se esse é o menor preço que ele já encontrou deste celular.
Qual dos códigos abaixo retorna o melhor preço até agora, para que o Douglas veja, de modo rápido, e decida se vale aproveitar a promoção ?

- print( precos.min )
- print( min precos )
- print( not max(precos) )
- __print( min(precos) )__
> Correto! A função min nos retorna o menor item de uma lista.

> Se desejamos descobrir o menor item de uma Lista, podemos utilizar a função min(), e passar a lista para ela como parâmetro. Então, no caso do Douglas, para descobrir o menor preço do celular até hoje, faríamos assim:  
> ```print( min(precos))```  
> E teríamos como resposta 1015, ou seja a promoção de R$ 1025 não valeria a pena!  
> É importante notar também que só conseguimos utilizar a função min() em listas de mesmo tipo, então por exemplo na lista abaixo:  
> ```precos = [ 1050, 'mil reais', 1020]```  
> O Python não vai saber comparar a String mil reais com os inteiros numéricos. Então sempre que utilizarmos o min() a lista deve possuir todos os elementos do mesmo tipo.  
> E claro, assim como temos a função min() que nos retorna o menor item da Lista, também temos a função max() que nos retorna o maior item da mesma.

3 - Marina precisava gerar um relatório sobre o último ano fiscal de sua empresa. Ela solicitou à equipe de TI que gerasse uma lista com todos os nomes dos funcionários da empresa.  
Ela recebeu a lista, que era como a lista abaixo:
```py
print(funcionarios)
['Astrid','Flavia','Talia', ... ,'Mauricio', 'Waldemar', 'Marina']
```
Marina estava acabando o relatório 10 minutos antes do prazo final de envio quando notou que além do nome de todos os funcionários, ela também precisava do total de funcionários! Como ela tinha pouco tempo e não conseguiria contar manualmente, precisou recorrer aos seus conhecimentos de Python para contar o número de itens da lista.  
Qual comando abaixo retorna o número de funcionários corretos da empresa de Marina?

- print(length(funcionarios))
- print(funcionarios.length)
- print(funcionarios.len())
- __print(len(funcionarios))__
> Correto! A função len() retorna a quantidade de itens das listas

4 - Romeu e seus colegas estavam competindo em um campeonato de futebol com o seu time 'Drible da emoção'.  
Como ele era um dos organizadores, tinha de manter a colocação de cada um dos 4 times manualmente, levando em consideração diversos fatores como número de pontos, gols marcados e etc... Como Romeu era um estudante de Ciências da Computação, ele resolveu automatizar este processo todo em um script em Python, para facilitar sua vida e dedicar mais tempo aos treinos.  
O seu script funcionou maravilhosamente bem, porém no dia de entrega dos resultados ele percebeu um erro. O script gerava a lista de colocação corretamente, porém na hora de exibir o resultado final com o campeão, ele sempre mostrava o segundo colocado em vez do primeiro colocado na Lista.  
```py
## Restante do código que gera a lista de colocação...

print(colocacao)
#Resultado: ['Drible da Emoção', 'Bruxos como Ronaldinho', 'Só golaço', '3x1 não é goleada']

campeao = colocacao[1]

print(' O grande campeão do torneio é o time ' + campeao)
#Resultado:  O grande campeão do torneio é o time Bruxos como Ronaldinho
```
Aponte o provável erro de Romeu na hora de exibir o primeiro colocado de sua lista, para que o seu time Drible da Emoção seja devidamente coroado campeão.

- __A__  
Romeu fez quase tudo corretamente, errando apenas na linha:  
```campeao = colocacao[1]```  
Apesar dele querer o primeiro colocado de seu torneio, ele deve pedir o primeiro elemento da lista, que é o elemento de índice 0** e não de índice **1.
> Correto! Vale lembrar que apesar de querermos o primeiro item de uma Lista, temos sempre que lembrar que as listas começam contando do índice 0

- B  
Romeu errou ao salvar o resultado em um variaveĺ na linha abaixo:  
```campeao = colocacao[1]```  
Quando fez isto, acabou alterando a ordem da lista, então quando ele pede para imprimir o campeao no print final, o resultado não vem como ele espera.

- C  
Romeu deveria ter impresso diretamente o resultado no print final, pulando a etapa de criar uma variável campeao. Caso ele tivesse feito assim:  
```print(' O grande campeão do torneio é o time ' + colocacao[1])```  
Ele obteria o resultado esperado.

## Aula 4

1 - Quais dos tipos abaixo são considerados sequências?

- __tuple__
> Correto! O tipo tuple é considerado uma sequência de valores.
- int
- bool
- __string__
> Correto! O tipo string é considerado uma sequência de caracteres.
- __list__
> Correto! O tipo list é considerado uma sequência de valores.

> Uma sequência é nada mais do que um conjunto de valores ordenados. Essa ordem é definida pelo índice. Por isso podemos acessar listas, tuples ou strings através dos [] (colchetes), por exemplo:
> 
> ```py
> >>>palavra = "alura"
> >>>palavra[3]
> r
> ```
>
> Ou usando uma tuple:
>
> ```py
> >>>letras = ("p", "y", "t", "h", "o", "n")
> >>>letras[2] 
> t
> ```
>
> Além disso, as sequências possuem várias funções em comuns, mas isso fica para a próxima pergunta!

2 - Veja o código:
```py
valores = ("a","b","c","d","e")
#AQUI
```
Dentre as funções abaixo, quais podem ser inseridas e executadas corretamente no lugar de #AQUI?

- __len( valores )__
> Correto! O len funciona para qualquer sequência, inclusive para tuples
- __max( valores )__
> Correto! O max funciona para qualquer sequência, inclusive para tuples.
- del( valores[0] )
- __min( valores )__
> Correto! O min funciona para qualquer sequência, inclusive para tuples.

> Importante saber que existem algumas funções que funcionam com todos os tipos de sequências como os built-ins: len, min e max.
> O del também é uma função built-in, mas só funciona para sequências mutáveis como listas. Como o tuple é imutável, não podemos remover seus elementos, e logo o código dá erro.
> Veja o mesmo exemplo correto usando uma lista:
> 
> ```py
> valores = ["a","b","c","d","e"]
> del(valores[0]) #funciona pois é lista
> ```

3 - Quais são as principais diferenças entre as sequências do tipo list e tuple?

- __list usa colchetes [] para inicialização, tuple usa parênteses ()__
> Correto! Para criar uma lista usamos [] e para criar um tuple usamos ()
- list possui um índice, tuple não
- __list é mutável, tuple é imutável__
> Correto! Isso é a principal diferença. Listas são mutáveis e Tuples são imutáveis
- list não pode ser usado no laço for, tuple sim
- list tem um limite de valores, tuple não

> Uma diferença que encontramos entre list e tuple é na hora de criá-las, em que usamos [] ou ():
> 
> ```py
> >>> lista = [4,3,2,1]
> >>> tuple = (4,3,2,1)
> ```
> 
> Outra diferença é a questão de podermos alterar a sequência ou não. Listas podem ser alteradas, podendo adicionar ou remover elementos. Tuples, uma vez criadas, não podem ser alteradas. Tuples são imutáveis.

4 - Veja todas as afirmações abaixo. Todas as sequências abaixo são imutáveis, exceto:

- __list__
> Correto! Listas são mutáveis, podemos adicionar e remover elementos como quisermos.
- tuple
- range
- str

> Já vimos nos vídeos as sequências str (strings), tuple, list e range.  
> Entre essas sequências, list é a única que é mutável. tuple, str e range são imutáveis.  
> Não falamos explicitamente que range é imutável, mas saiba que ele se comporta como tuples e strs.

5 - O Pedro é um desenvolvedor Python Junior e precisa corrigir o código abaixo que está dando erro:
```py
nomes = ("Nico", "Douglas", "Flavio", "Daniel")
#AQUI
nomes.append("Fabio") 
```
Quais alternativas ele pode usar no lugar de #AQUI para o código funcionar?

- nomes = tuple(nomes)
- nomes = (nomes)
- nomes = nomes[0]
- __nomes = []__
> Correto! Nomes será uma lista vazia.
- __nomes = list(nomes)__
> Correto! Estamos usando a função list para criar uma lista baseando-se nos valores da tuple nomes.

> Lembrando que para transformar um tuple em uma lista, temos a função list(..). Se queremos transformar de list para tuple devemos usar tuple(..) Ambas são funções built-in.

6 - Quais dos exemplos abaixo são mais propensos a serem usados como tuples em vez de listas?

- Nomes de pessoas onde não sabemos quantas existem.
- __Nomes dos meses.__
> Correto! É ideal para uma tuple pois são sempre 12 meses.
- Valores de CPF variáveis.
- __Nomes dos estados do país.__
> Correto! Como os estados do país são fixos, usar um tuple é uma boa opção.
- Nome das estações do ano.
> Correto! Temos sempre 4 estações no ano. Isso nunca muda e por isso é o cenário ideal para uma tuple.

## Aula 5

1 - Carlos criou um loop para calcular a quantidade de caracteres em uma palavra através do seguinte código:
```py
total = 0
palavra = "python rocks!"
acabou = False
while (not acabou):
    #AQUI 
    total = total + 1
print(total - 1)
```
O que Carlos precisa colocar dentro do while no lugar de #AQUI para que se encerre e consiga imprimir o total de caracteres da palavra?

- acabou = True
- __acabou = ( total == len(palavra) )__
> Correto! Carlos poderia ter simplesmente usado a própria função len, mas esse código definirá True para a variável acabou apenas quando total for igual ao tamanho da palavra.
- acabou = ( total == 11 )

> Só para deixar claro, usando a função len:
> ```py
> len(palavra)
> ```
> Já imprime o tamanho da string!

2 - Considere o seguinte trecho de código com um loop:
```py
passos = 0
while (#######):
  passos += 1
print(passos)
```
O que precisa ser colocado na condição do while para que o loop saia após 10 passos?

- __passos<10__
> Correto! O loop será executado 10 vezes, conforme o pedido do enunciado.
- passos==10
- __passos<=9__
> Correto! O loop será executado 10 vezes (0 até 9), conforme o pedido do enunciado.
- passos<=10

3 - No nosso jogo da forca imagine que você inicialize a variável erros com 6 tentativas:
```py
erros = 6
```
O que você precisa mudar no código para manter o jogador sendo enforcado após 6 tentativas frustradas?

- A  
    Nada.

- B  
    Apenas decrementar a variável erros com:
    ```py
    erros = erros - 1
    ```

- __C__  
    Apenas mudar o teste da variável enforcou para:
    ```py
    enforcou =  erros == 12
    ```
> Correto! Se a variável erros começou com 6, pra manter a quantidade de tentativas em 6, precisamos mudar o teste da variável enforcou para 6 + 6, mas seria nada elegante e legível, certo?

- __D__  
    Decrementar a variável erros com:
    ```py
    erros = erros - 1
    ```
    e mudar o teste da variável enforcou para:
    ```py
    enforcou = erros == 0
    ```
> Correto! Podemos decrementarmos a variável erros para que ela chegue até zero e com isso o teste da variável enforcou precisará mudar para refletir isso.

4 - João criou a seguinte lista:
```py
frutas = ["maçã", "banana", "laranja", "melancia"]
```
Agora ele precisa criar uma nova lista com as mesmas frutas, mas tudo escrito em letras maiúsculas. Ele escreveu o laço abaixo:
```py
lista = []
for fruta in frutas:
    lista.append(fruta.upper())
```
O código funciona, mas será que você pode mostrar para ele como usar as List Comprehensions? Qual solução abaixo é relativa ao laço?

- lista = [for fruta.upper() in frutas]
- __lista = [fruta.upper() for fruta in frutas]__
> Correto! Criamos uma nova lista [] e dentro dos colchetes usamos a List Comprehension.
- lista = [for fruta in frutas fruta.upper() ]

> O código com List Comprehension, que inicializaria a lista acima, seria:
> ```py
> frutas = ["maçã", "banana", "laranja", "melancia"]
> lista = [fruta.upper() for fruta in frutas]
> ```
> Repare que é muito mais enxuto e, uma vez acostumado com a sintaxe, é até mais fácil de entender.

5 - Suponha que tenhamos uma lista com os seguintes inteiros:
```py
inteiros = [1,3,4,5,7,8]
```
Podemos preencher uma nova lista com o quadrado de cada número da lista anterior, através do recurso List Comprehension. Considerando que, para calcular o quadrado de um número, fazemos x*x, qual seria o código para obter a lista de quadrados?

- quadrados = [2 for n in inteiros]
- Não é possível inicializar uma lista de números inteiros, apenas caracteres.
- __quadrados = [n*n for n in inteiros]__

## Aula 6

1 - Se desejamos trabalhar com arquivos, precisamos primeiro abrí-lo utilizando a função open(). A função open() recebe um ou mais parâmetros. Em uma determinada ordem, quais são eles?

- __O nome do arquivo e o modificador de acesso.__
> Correto! Precisamos informar qual é o nome do arquivo que queremos abrir, e podemos também informar qual modificador de acesso válido.
- O modificador de acesso primário e o modificador de acesso secundário.
- O modificador de acesso e o nome de arquivo.

> Importante é que não precisamos passar o modificador de acesso, pois o segundo parâmetro é opcional:
> ```py
> arquivo = open("entrada.txt")
> ```
> Nesse caso será utilizado o modo de leitura (r) por padrão.

2 - Marque todas as alternativas abaixo que são modificadores de acesso da função ```open()```:

- __r__
> Correto! Utilizamos o modificador r para o modo de leitura
- __a__
> Correto! Utilizamos o modificador a para modo de append, adicionando conteúdo a um arquivo pré existente
- w+r
- __w__
> Correto! Utilizamos o modificador w para modo de escrita.

> Além do r, w e a existe o modificador b que devemos utilizar quando queremos trabalhar no modo binário. Para abrir uma > imagem devemos usar:
> ```py
> imagem = open("foto.jpg", "rb")
> ```
> Por exemplo, o código abaixo cria uma cópia de uma imagem:
> ```py
> #arquivo copia.py
> logo = open('python-logo.png', 'rb')
> data = logo.read()
> logo.close()
> 
> logo2 = open('python-logo2.png', 'wb')
> logo2.write(data)
> logo2.close()
> ```

3 - É uma boa prática fecharmos o arquivo depois de utilizá-lo para escrita ou leitura, assim outros programas ou processos podem ter acesso ao arquivo e ele não fica preso apenas ao nosso script Python.  
Qual das funções abaixo é utilizada para fechar um arquivo que foi aberto desse jeito:
```py
arquivo = open('nome.txt', 'w')
```

- arquivo.flush()
- __arquivo.close()__
> Correto! A função close é responsável por fechar o arquivo.
- arquivo.clear()
- arquivo.end()

4 - Dado o arquivo abaixo chamado de pessoas.txt, onde estão separados os nomes e a idade de um grupo de pessoas:
```py
Romário 37
Junior 32
Daniel 28
Izzy 38
```
Se queremos ler apenas a primeira linha do arquivo, quais comandos abaixo realizam este feito?

- A
```py
arquivo = open('pessoas.txt', 'r')
linha = arquivo.read()
print(linha)
```
- B
```py
arquivo = open('pessoas.txt', 'r')
linha = arquivo.firstline()
print(linha)
```

- __C__
```py
arquivo = open('pessoas.txt', 'r')
linha = arquivo.readline()
print(linha)
```
> Correto! A função readline lê apenas uma linha do arquivo.

> Se desejamos ler linha a linha de nosso arquivo, podemos utilizar a função readline(). Ela nos retorna uma linha por vez, e faz com que a nossa leitura seja feita de modo mais controlado. Também existe a função read() que por sua vez lê o arquivo inteiro.

5 - Dado um arquivo como o seguinte: frutas.txt
```py
Banana
Maçã
Pera
Uva
Jamelão
```
Que foi aberto deste modo:
```py
arquivo = open('frutas.txt','r')
```
E quando executamos os comandos:
```py
linha = arquivo.readline()
print(linha)
linha = arquivo.readline()
print(linha)
```
É exibido corretamente as linhas:
```py
Banana
Maçã
```
Mas quando abrimos o arquivo e usamos os comandos:
```py
arquivo = open('frutas.txt','r')
conteudo = arquivo.read()
print(conteudo)
conteudo = arquivo.read()
print(conteudo)
```
A primeira vez é exibida corretamente o conteudo, porém na segunda não é exibido nada. Porque?

- Se desejamos ler duas vezes o arquivo inteiro, temos que utilizar o modificador de acesso r+. O modificador de acesso r perde o efeito de leitura após a função read ser executada pela primeira vez.
- __Pois o comando read() lê o arquivo inteiro de uma vez, colocando o ponteiro de leitura no final do mesmo. Se chamarmos a função read() novamente, como o ponteiro de leitura está no final, nada será lido.__
> Correto! Se desejarmos ler o arquivo novamente, devemos fechá-lo com o comando .close(), reabri-lo com o comando .open() e ai sim conseguiremos lê-lo por inteiro novamente.
- Pois como abrimos o comando com o modificador de acesso r, fica implícito que só tentaremos ler uma vez com a função read(), quando tentamos pela segunda vez obtemos um erro e a leitura é abortada.

## Aula 7

1 - Sobre funções em Python, temos as seguintes afirmativas:

a - Uma função é um bloco de código que pode ser guardado, para ser chamado assim que desejarmos, contanto que saibamos seu nome. Contudo, não é necessário sabermos a sua implementação.

b - A seguinte declaração de função é válida:
```py
# declara a função
def imprime_mensagem():
    print("Olá")

# chama a função
imprime_mensagem()
```

c - A convenção é criarmos funções no padrão lowerCamelCase, isto é, a primeira palavra é escrita com todas as letras minúsculas, as palavras restantes com a primeira letra maiúscula e unidas sem espaço.  
Sobre as afirmativas anteriores, podemos afirmar que:

- __Apenas a alternativa 3 é falsa.__
> Correto! Em Python, a convenção é criarmos funções no padrão snake_case, isto é, cada palavra é iniciada com letras minúsculas e separadas por um underscore (_).
- Nenhuma alternativa é falsa.
- Apenas a alternativa 1 é falsa.
- Apenas a alternativa 2 é falsa.

> Uma função, quando carregada, não tem o seu bloco de código executado automaticamente. A função é guardada em algum lugar, para mais tarde alguém chamá-la. Mas para que alguém a chame, execute-a, precisa saber seu nome. É por isso que a declaração de uma função é:
> ```py
> def imprime_mensagem():
>     print("Olá")
> ```
> Quando a função é carregada, nada acontece, mas se chamamos a função pelo seu nome, executamos todo aquele código do bloco da função:
> ```py
> def imprime_mensagem():
>     print("Olá")
> 
> imprime_mensagem()
> ```
> É através de imprime_mensagem( ) que executamos tudo que está dentro do bloco (após os dois pontos, que esteja indentado corretamente) da função. Inclusive podemos chamar a função mais de uma vez:
> ```py
> def imprime_mensagem():
>     print("Olá")
> 
> imprime_mensagem()
> imprime_mensagem()
> imprime_mensagem()
> imprime_mensagem()
> ```
> No exemplo acima, executaremos o bloco da função quatro vezes, porque a chamamos quatro vezes!
> 
> Aliás, há uma convenção no nome de funções assim como nos nomes das variáveis, usamos o padrão snake_case. Sendo assim, toda função possui todas as letras minúsculas e cada palavra que forma o nome da função é separada por um underscore (o caractere _).

2 - Douglas está criando uma calculadora simples, para realizar cálculos entre dois números. Para isso, ele criou quatro funções, uma para cada operação matemática (soma, subtração, multiplicação e divisão):
```py
def soma_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero + segundo_numero)

def subtrai_dois_numeros{primeiro_numero, segundo_numero}
    print(primeiro_numero - segundo_numero)

def multiplica_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero * segundo_numero)

def divide_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero / segundo_numero)
```
Mas na hora de testá-las, Douglas reparou algo estranho no funcionamento da sua calculadora. Então, das quatro funções declaradas acima, podemos dizer que:

- A função ```multiplica_dois_numeros``` possui erro de sintaxe.
- A função ```divide_dois_numeros``` possui erro de sintaxe.
- A função ```soma_dois_numeros``` possui erro de sintaxe.
- __A função ```subtrai_dois_numeros``` possui erro de sintaxe.__
> Correto! A função subtrai_dois_numeros possui não só um, mas dois erros de sintaxe. Após o nome da função, deve haver parênteses (e não são chaves!), e está faltando os dois pontos após o nome da função.

> Quando declaramos uma função, é importante os parênteses logo após o seu nome, é dentro dele que os parâmetros da função ficam. Inclusive toda função possui um bloco, em que podemos adicionar o código que quisermos que a função execute quando for chamada.  
> Lembre-se que um bloco é caracterizado por tudo que fica após os dois pontos, indentado por quatro espaços. Tudo que estiver indentado por quatro espaços são instruções da função.

3 - Entre as boas práticas de código, está a divisão do código de uma função grande em funções pequenas. Pensando nisso, todas as afirmativas abaixo são verdadeiras, exceto uma. Qual?

- Dividindo o código de uma função grande em funções pequenas, evitamos o problema das múltiplas responsabilidades em única grande função, afinal uma função só deve ter uma única responsabilidade.
- O código fica mais fácil de testar, pois com diversas pequenas funções, é muito mais fácil testá-las individualmente em busca de erros.
- __A legibilidade do código fica prejudicada, visto que temos de ler diversas funções, em vez de apenas uma.__
> Essa afirmativa é falsa! Quebrar o código em pequenas partes aumenta a legibilidade. Mas é preciso tomar cuidado com a criação de funções, pois criar funções desnecessariamente pode aumentar a complexidade do código.
- Melhora a manutenção do código, já que é mais fácil você cuidar de vários pequenos blocos simples do que um grande bloco complexo.

> Sabemos que quebrar uma grande função complexa em pequenas funções é uma boa prática por causa de diversos fatores, mas podemos citar como os principais deles:  
> - Dar manutenção ao código fica muito mais fácil, visto que agora podemos examinar vários pequenos blocos, que são muito mais fáceis de compreender do que um grande bloco de código.
> - Ao quebrar uma grande função, também estamos deixando ela com menos responsabilidades, com a meta de atingir o ideal de que cada função tenha apenas uma única responsabilidade.
> - O código também fica muito mais fácil de testar, pois se temos diversas funções pequenas, conseguimos testar uma a uma em busca de erros no código.
> - E por último, a legibilidade do código aumenta muito, pois dando nomes semânticos a cada uma das funções menores, conseguimos deixar bem claro o que aquela parte do código deve fazer e facilita o entendimento do todo como um geral.
