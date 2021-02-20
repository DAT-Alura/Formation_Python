# Aula 1

Quando estamos escrevendo uma aplicação, é importante garantir que o código que foi implementado funcione corretamente.

Uma forma de garantir o funcionamento do sistema é testando suas funcionalidades. Para cada regra de negócio, realizamos testes que cobrem os casos de uso do sistema.

Existem algumas formas de fazer esses testes, uma forma, é imprimir mensagens no console e ir comparando o resultado, outra forma é utilizar um framework, ou uma biblioteca de testes.

Qual a vantagem de utilizar uma biblioteca de testes a conferir manualmente os testes?

A - Não existe diferença entre utilizar uma biblioteca de testes e fazer os testes "na mão". Em ambos os casos teremos que escrever um código de testes.

B - Como muitas aplicações precisam ser testadas, não existe nenhuma biblioteca capaz de realizar testes, já que cada aplicação é única, cada teste também é único

__C__ - Utilizando uma biblioteca de testes, temos um feedback mais rápido e intuitivo sobre os testes.
> Alternativa correta! Quando usamos uma biblioteca as respostas sobre o resultados dos testes é mais direta. Dessa forma, temos um feedback mais rápido sobre o que devemos fazer.

D - É sempre interessante fazer os testes "na mão", já que testamos apenas um caso de uso da regra de negócio e, se passar, podemos ir implementar uma nova funcionalidade.

# Aula 2

Quando estamos escrevendo testes, é comum usarmos os mesmos objetos, isto é, o mesmo cenário para todos os testes.

Repetição de código é um mau cheiro de código (code smell), por isso uma prática comum é isolar a criação do cenário de testes.

Qual solução a biblioteca unittest tem para resolver esse problema?

__A__ - Podemos isolar esse código através do método setUp que é herdado da classe TestCase. Esse método é invocado antes de cada método de testes, dessa forma, garante que um teste não influencie outro.
> Alternativa correta! Através do método setUp, conseguimos criar os objetos utilizados pelos testes. Esse método é executado antes de cada teste, dessa forma, garantimos que um teste não influencia outro, já que sempre teremos novos objetos.

B - PPodemos isolar o código repetido criando um método e chamando-ô antes no começo de cada método de testes.

C - PNão existe como isolar o cenário de criação. Como cada teste verifica a execução de um caso de uso específico, não tem como isolar esses cenários.

D - PCom o método set_up. Esse método é invocado uma única vez e compartilha o mesmo objeto em todos os testes.

# Aula 3

Quando estamos escrevendo testes, é comum que estes nos deem feedbacks sobre o design do código testado. Geralmente, códigos difíceis de serem testados são códigos que não estão muito bem modelados.

Na aula, vimos que a forma que adicionávamos um lance a lista de lances (leilao.lances.append(lance)). Apesar de ser uma abordagem que funciona, ela contém alguns problemas. Quais são esses problemas?

A - Não há problema nessa implementação. Pelo contrário, se tentarmos trocar a implementação da classe Leilao o código das classes clientes podem falhar, o que nos faria arrumá-las.

__B__ - Estamos muito acoplados da implementação da classe Leilao. Ou seja, sempre que a implementação da classe for trocada, os códigos clientes são afetados.
> Resposta certa! Utilizando essa abordagem, ficamos muito acoplados a classe. Uma melhor abordagem seria encapsular a forma de adicionar um lance à lista.

C - Não existe nenhum problema nessa forma de implementação. Essa é a forma correta de se adicionar um lance.

D - O problema dessa implementação é que estamos utilizando uma lista. O correto seria utilizar uma tupla ou outra estrutura imutável.

# Aula 4

Na aula, vimos algumas formas de passar feedbacks para os clientes do código que escrevemos. Dependendo da ação que é tomada, o código pode continuar a execução normalmente ou ir para fluxos alternativos. Como, por exemplo, não adicionar o lance na lista.

O importante é que a pessoa que está usando a aplicação, ou o código cliente estejam a par do ocorrido. Ou seja, temos que passar esse feedback para o usuário. Qual uma boa forma de se passar um feedback para o usuário?

A - A melhor forma de passar um feedback de uma operação é devolvendo um booleano. Retornamos True caso a operação seja bem sucedida e False caso contrário

__B__ - Lançar uma exceção caso a operação seja inválida. Dessa forma, o código cliente consegue tratar essa exceção ou então, o sistema para de funcionar caso ela não seja tratada.
> Isso mesmo! Ao utilizar exceções, fazemos com que o código cliente tenha que tratar essa exceção em algum ponto do código. Ou com blocos try/except ou de outras maneiras

C - A melhor forma de passar um feedback para o usuário é devolvendo um número (número mágico) para caso a operação seja um sucesso e outro número para caso a operação falhe

D - Não precisamos passar nenhum feedback. Quando a pessoa que estiver utilizando o sistema ver que o comportamento não foi esperado, ela saberá o que fazer

# Aula 5

Quando executamos um teste, precisamos conferir os resultados obtidos com os resultados esperados. No caso, quando utilizamos a biblioteca unittest utilizamos o método self.assertEqual que é herdado da classe TestCase passando como parâmetros o resultado da execução e o resultado esperado.

No caso da biblioteca pytest, não herdamos de nenhuma classe, então, como podemos conferir a execução dos testes?

__A__ - Através da palavra reservada assert. Com ela, conseguimos passar uma condição para avaliar se é verdadeira ou não. Com isso, o teste pode passar ou falhar
> Correto! Conseguimos utilizar a palavra reservada assert para conferir o resultado para gente. Com isso, a biblioteca pytest já consegue conferir se o teste passou ou não

B - Através da função is_correct da biblioteca pytest. Nela, passamos como parâmetros o resultado da execução e o resultado esperado

C - Pelo fato de não herdar de nenhuma classe, não conseguimos conferir a execução do programa. Precisamos ainda utilizar a unittest para isso

D - Pela função pytest.assertEqual() da biblioteca conseguimos conferir a execução do programa.

# Aula 6

Quando temos um código muito grande, ou com tendências a crescer, geralmente isolamos esse trecho de código em funções, métodos, classes.

Quebrar o código tem alguns benefícios, entre eles, podemos citar:


__A__ - O código fica mais legível. Logo, conseguimos identificar os pontos que precisam ser alterados mais facilmente, ajudando assim na manutenção do código.
> Correto! Isolar o código é uma técnica de refatoração muito utilizada, já que conseguimos aumentar a legibilidade do código.

B - O código fica menor. Quando isolamos um código, fazemos apenas a chamada da função, ou método, não precisamos saber a implementação.

C - Ao isolar o código, ele fica mais complexo de ler e de manter. Já que ao fazer a chamada do método, não sabemos o que está implementado

D - Não precisamos isolar as condições ou grandes trechos de código. Manter todos em um mesmo lugar facilita a manutenção no futuro.
