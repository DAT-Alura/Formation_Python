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
