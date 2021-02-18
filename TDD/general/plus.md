# Testes e Produtividade

Um debate muito comum quando falamos sobre testes de software é se escrever testes aumenta a produtividade.

Muitas pessoas falam que quando escrevemos testes de software, garantimos o comportamento daquele trecho de código. Logo, no futuro, não precisaremos nos preocupar em arrumar um bug no sistema. Os testes já garantem, ou pelo menos deveriam, garantir que o código está correto.

Outras pessoas dizem que perdemos muito tempo escrevendo testes e que poderíamos utilizar esse tempo para implementar novas funcionalidades no sistema.

O fato é que ser produtivo é relativo! Cada um tem uma conclusão diferente das afirmações acima. O fato é que escrevendo testes ou não, o sistema tem que estar funcional e com o mínimo de erros para não afetar as pessoas e outros sistemas que dependam dele.

Logo, se escrever testes nos deixa mais produtivo ou não, depende! Depende do que enxergamos como produtividade.

# Metodos da TestCase

Vimos na aula o método setUp que é executado antes de cada método de testes. Este não é o único método que herdamos da classe TestCase, além deste, temos outros métodos como o tearDown, setUpClass e o tearDownClass.

Vamos imaginar que estamos realizando um teste que faz a conexão com um serviço externo, envia um e-mail ou então faz uma modificação no banco de dados.

Nesses casos, precisamos abrir uma conexão, executar os testes e fechar a conexão em seguida. Fechar a conexão é algo em comum com esses tipos de testes.

Podemos então declarar o método tearDown que é executado logo após a execução do teste. Ou seja, caso abrimos uma conexão, podemos utilizar o método tearDown para fechá-la após os testes.

Analogamente ao método setUp e tearDown, temos o setUpClass e o tearDownClass. Ambos funcionam de uma forma parecida com o setUp e tearDown, porém, ao invés de serem executados antes de cada método, são executados apenas uma vez - o setUpClass no momento que a classe é criada e o tearDownClass após o último teste da classe ser rodado.

Os métodos tearDown e tearDownClass são muito utilizados em testes que integram duas partes do sistema - banco de dados, sistemas externos, ou então desejamos fechar uma conexão que foi aberta.

Esses tipos de testes, que verificam como duas partes do sistema se integram, são chamados de testes de integração.

# Como nomear um teste

Como vimos na aula, os métodos de testes precisam ser semânticos. Em muitos casos, os testes são utilizados como a documentação do código no projeto.

Existem algumas formas de nomeação, contudo, em muitos casos os times definem qual padrão utilizar. O importante é que o nome dos métodos sejam expressivos e que o padrão escolhido seja seguido.

Caso queiram conhecer outras formas comuns de nomear os testes, neste [link](https://dzone.com/articles/7-popular-unit-test-naming) de um artigo em inglês mostra algumas formas de nomeação.
