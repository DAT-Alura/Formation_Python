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

# Lei de Demeter

Vamos analisar a classe Leilao:

```py
class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

       # restante do código
```

Nesta classe, existe uma lista de lances. Ou seja, uma composição com uma lista. O que esperamos que ocorra com ela?

Esperamos que sejam adicionados os lances pertencentes ao leilão. Algo como leilao.lances.append(lance) é uma má prática, já que estamos muito acoplados com a implementação da classe Leilao.

Além de ferir o princípio do Diga, não pergunte (o Tell don't ask), estamos ferindo outro princípio chamado Lei de Demeter, ou o Princípio do menor conhecimento (Principle of least knowledge).

Esse princípio diz que devemos ter o menor conhecimento sobre a implementação da classe. Dessa forma, evitamos o acoplamento entre as classes do sistema.

Claro, o acoplamento sempre existirá. Quando estamos utilizando uma lista, string, dicionário, estamos acoplados com essa classe. Porém, isso é chamado de "acoplamento bom". A chance de uma dessas classes mudarem e afetarem o código são muito pequenas.

Acoplar com classes estáveis é muito melhor do que com classes instáveis

Então só devemos nos acoplar com classes do sistema?

Não! No código que escrevemos existem classes mais estáveis do que outras. São essas que devemos optar por acoplar.

Seguindo esses princípios como a Lei de Demeter e o Diga, não pergunte, escrevemos um código mais simples de ser alterado e escalado.

Quem quiser ver um pouco mais sobre a Lei de Demeter, deixo [esse texto](https://en.wikipedia.org/wiki/Law_of_Demeter), em inglês, da Wikipédia.

# Copia profunda

No curso, devolvemos uma cópia da lista de lances quando utilizamos a property:

```py
class Leilao:
    # código omitido

    @property
    def lances(self):
        return self.__lances[:]
```

Foi dito que isso é uma cópia rasa, mas o que isso significa?

Quando utilizamos uma cópia rasa, apenas a referência da lista, neste caso, é diferente. Todos os outros objetos dentro dessa lista compartilham a mesma referência. Ou seja, apesar da lista de lances ser uma cópia, os lances dentro da lista copiada são os mesmos lances do leilão.

Para que os lances sejam diferentes, precisamos copiar a lista profundamente. Por isso os termos cópia rasa e cópia profunda.

Poderia dar exemplos e falar sobre o funcionamento das cópias, porém, o Yan, um dos escritores do blog da Alura já escreveu um excelente post sobre cópias de lista no Python. Recomendo muito a leitura desse post. Para quem estiver interessado, pode encontrar a leitura neste [link](http://blog.alura.com.br/como-fazer-copia-de-lista-python/).
