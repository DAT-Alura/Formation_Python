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

# Baby steps

Vimos uma abordagem de escrita de testes, os baby steps, ou passos de bebê. Nessa abordagem, começamos primeiro pelos testes e fazemos o mínimo possível para o teste passar. Quando ele passa, refatoramos o teste e o código e vamos mantendo esse ciclo no desenvolvimento.

Apesar dos baby steps ajudarem na escrita do código de testes e no entendimento das regras de negócio, não precisamos fazê-lo sempre.

Quando já temos conhecimento claro das regras de negócio ou então quando já conhecemos o problema, não precisamos realizar baby steps.

Existe um debate na comunidade de como praticar o TDD realizando os baby steps e escrevendo primeiro os testes ajudam a escrever um código mais simples, com um melhor algoritmo. Porém, isso também é relativo.

A verdade é que escrever o código é algo muito pessoal. Existem pessoas que começam pelo código e pessoas que começam pelos testes. Existem pessoas que fazem baby steps, outras que não. O importante é o código estar funcionando sem erros quando for solicitado.

# Pytest Fixture e classes de teste

No vídeo, vimos um pouco sobre as fixtures do pytest. Existem outras fixtures que podemos utilizar além daquelas. [Neste post](https://blog.alura.com.br/montando-cenarios-de-testes-com-o-pytest) são mostrados algumas outras fixtures.

É interessante notar que utilizamos funções para escrever os testes. Porém, se quiséssemos, poderíamos utilizar classes de testes também. A implementação do mesmo módulo de testes como uma classe, ficaria parecida com essa:

```py
from src.leilao.dominio import Usuario, Leilao

import pytest

from src.leilao.excecoes import LanceInvalido

class TestUsuario:

    @pytest.fixture
    def vini(self):
        return Usuario('Vini', 100.0)


    @pytest.fixture
    def leilao(self):
        return Leilao('Celular')


    def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(self, vini, leilao):
        vini.propoe_lance(leilao, 50.0)

        assert vini.carteira == 50.0


    def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(self, vini, leilao):
        vini.propoe_lance(leilao, 1.0)

        assert vini.carteira == 99.0


    def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(self, vini, leilao):
        vini.propoe_lance(leilao, 100.0)

        assert vini.carteira == 0.0


    def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(self, vini, leilao):
        with pytest.raises(LanceInvalido):

            vini.propoe_lance(leilao, 200.0)
```
