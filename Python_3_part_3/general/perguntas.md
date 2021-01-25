## Aula 1

1 - Com base no vídeo, selecione a alternativa que expressa a ideia central do paradigma da Orientação a Objetos.

- Getters e setters devem ser usados em suas classes.
- Todo código deve estar dentro de uma classe.
- __Dado e funcionalidade (comportamentos) andam juntos.__
> Correto! No exemplo do vídeo, se Conta e, por exemplo, o método deposita estivessem juntos, ai sim teríamos aplicado OO.

2 - De acordo com as situações citadas no vídeo, escolha a única alternativa que não é sinal de programação procedural.

- Copy & Paste e Ctrl + F como prática regular do desenvolvedor para propagar mudanças no projeto.
- Códigos confusos e duplicados.
- __Comportamento e dados caminhando juntos, o que auxilia na manutenção e legibilidade do código.__
> Correto! Para que várias equipes consigam trabalhar em um mesmo projeto, é necessário que as responsabilidades de cada código estejam bem definidas e claras, evitando conflitos na hora de realizar mudanças e evoluções. Código com responsabilidades coesas é sinal do paradigma OO.

3 - Paulo é novo na equipe da empresa ByteBank. Ficou responsável por uma tela de cadastro, onde existe um campo que deve ser validado conforme a regra de negócio XYZ. Ele pergunta ao seu gerente onde pode obter informações sobre a tal regra. Marque as alternativas que podem ser identificadas como respostas de quem usa o paradigma procedural em seus projetos.

- __Paulo deve entrar em contato com alguém da equipe de analistas de negócio da empresa, para ele entender a regra e implementá-la.__
> Correto! Essa resposta indica que Paulo deve implementar novamente a regra, gerando mais um local caso a regra precise ser alterada. Tipicamente procedural.
- __Dependendo do módulo, Paulo deve perguntar ao responsável técnico do mesmo.__
> Correto! Essa resposta denota que a regra está implementada em vários lugares. Quem é o responsável por ela? Como diz o ditado popular "Cachorro que tem muitos donos acaba morrendo de fome". Tipicamente procedural.
- Basta que Paulo consuma uma classe que representa a informação a ser cadastrada pelo campo.
- __"Copie o código de validação que está no formulário ABCD."__
> Correto! Resposta típica de quem usa o paradigma procedural para não arriscar inserir erros em códigos que já estão funcionando ou em produção.

## Aula 2

1 - A partir do conhecimento adquirido de classes, leia as frases abaixo e responda a opção correta.
1.Uma classe é uma especificação de um tipo, definindo valores e comportamentos.
2.Um objeto é uma instância de uma classe onde podemos definir valores para seus atributos.
3.Para criar uma instância, é obrigatório preencher os valores de todos os atributos.
4.Uma boa analogia é considerar a classe como a receita para a criação de algum prato; por exemplo, um delicioso bolo de cenoura ;-)

- Todas as opções estão corretas.
- A opção 1 é a única correta.
- __A opção 3 é a única errada.__
- As opções 2 e 3 estão erradas.

2 - Em orientação a objetos, como chamamos as características de uma classe?

- Argumento.
- __Atributo.__
> Correto! Os atributos são as características que especificam uma classe.
- Variável.
- Parâmetro.

3 - Considere o código abaixo, que declara a classe Conta.
```py
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
```
Selecione a alternativa que cria um objeto Conta com valores para os atributos número, titular, saldo e limite.


- A
```py
conta = Conta()
```

- D
```py
conta = Conta()
conta.__init__(conta, 1, "Eric Clapton", 0.0, 500.0)
```

- __C__
```py
conta = Conta(1, "Eric Clapton", 0.0, 500.0)
```

## Aula 3

1 - Chalita decidiu aplicar o que aprendeu na aula sobre método em Python. Ele criou a classe Pessoa que recebe em seu "construtor" um nome e sobrenome e que declara o único método exibe_nome_e_sobrenome(). Vejamos o código que ele escreveu:
```py
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    exibe_nome_e_sobrenome():
        print("{0} {1}".format(self.nome, self.sobrenome))

pessoa = Pessoa("Chalita", "Steppat")
pessoa.exibe_nome_e_sobrenome()
```
Quantos erros há no código de Chalita?

- __2__
> Exato. Chalita não declarou o método com def, muito menos recebeu self como parâmetro.
- 1
- 3

2 - Fernanda criou a classe Jogo com o método incrementa() que, ao ser chamado, atualizará o valor do atributo self.contador:
```py
class Jogo:

    def incrementa(self):
        contador+=1
Então, ela realizou sem sucesso o seguinte teste:

jogo = Jogo()
jogo.incrementa()
print(jogo.contador)
```
Marque a opção que possui o código de Fernanda corrigido para que o seu teste funcione.

- A
```py
class Jogo:
    def __init__(self):
        self.contador = 0

    def incrementa(self):
        contador+=1
```

- __B__
```py
class Jogo:
    def __init__(self):
        self.contador = 0

    def incrementa(self):
        self.contador+=1
```

- C
```py
class Jogo:
    def __init__():
        self.contador = 0

    def incrementa(self):
        self.contador+=1
```

- D
```py
class Jogo:
    def __init__(self):
        contador = 0

    def incrementa(self):
        self.contador+=1
```

3 - Andreza declarou a classe Recibo que recebe em seu construtor um valor inicial. Vejamos a classe em uso:
```py
recibo1 = Recibo(50)
recibo2 = Recibo(100)
recibo3 = Recibo(200)
recibo4 = recibo3
recibo3 = None
recibo1 = recibo3
recibo4 = recibo1
recibo3 = recibo2
```
Depois que todas as instruções forem executadas, marque as opções verdadeiras à respeito do estado das variáveis:

- A variável recibo4 é diferente de None.
- __A variável recibo3 apontará para um objeto Recibo com valor 100.__
- __A variável recibo1 será None.__
- As variáveis recibo1, recibo2, e recibo3 serão None.

4 - Francisco precisa criar a classe chamada Sistema com os métodos le_entrada() e exibe_saida(). O primeiro, ao ser chamado, deve ler do teclado um texto qualquer e guardar internamente na propriedade texto. Já o segundo método, quando for chamado, deve exibir o valor de texto. Exemplo de uso:
```py
sistema = Sistema()
sistema.le_entrada()
sistema.exibe_saida()
```
Marque a única opção que materializa corretamente a classe.

- __A__
```py
class Sistema:
    def __init__(self):
        self.texto = ''

    def le_entrada(self):
        self.texto = input()

    def exibe_saida(self):
        print(self.texto)
```

- B
```py
class Sistema:
    def __init__(self):
        self.texto = ''

    def le_entrada(self):
        self.texto = input()

    def exibe_saida():
        print(self.texto)
```

- C
```py
class Sistema:
    def __init__(self):
        self.texto = ''

    def le_entrada(self):
        self.texto = input()

    def exibesaida(self):
        print(self.texto)
```

## Aula 4

### 1 - Ao usar o prefixo __ no nome do atributo o Python ...

A - ... automaticamente inicializa os atributos com os valores padrões para cada tipo.

__B__ - ... dá um nome diferente para o atributo da classe alterando em todos os lugares.
> Correto! Como vimos, o atributo recebe o nome da classe como prefixo.

C - ... apaga o atributo já que é usado internamente apenas.

D - ... transforma o atributo em métodos de acesso.

### 2 - Veja a classe Retangulo abaixo:

```py
class Retangulo:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area
```

Assumindo que a classe foi carregada corretamente, podemos executar o seguinte código:

```py
r = Retangulo(7,6)
r.area = 7
r.obter_area()
```

Qual é o resultado da execução? Se tiver com dúvida, faça o teste!

A - erro de execução

B - 7

C - 6

D - 42
> Correto! A classe Retangulo está correta e define os atributos __x, __y e __area, além do construtor e o método obter_area(). Nada impede então criar um objeto:
>
> ```py
> r = Retangulo(7,6)
> ```
>
> Agora, se você tenta acessar um atributo area, que na verdade não declaramos, o Python cria automaticamente um novo atributo e inicializa com o valor 7:
> 
> ```py
> r.area = 7
> ```
>
> Na linha em cima o objeto ganha um novo atributo com o nome area. Ou seja, temos um atributo __area E um novo com o nome area. No entanto, ao chamar r.obter_area(), continuamos acessar o atributo __area que foi inicializado com o produto de 7*6!

### 3 - Quais vantagens identificamos ao colocar a funcionalidade transferir na classe Conta?

__A__ - Melhoramos a legibilidade do nosso código.
> Correto! Repare que fica claro para quem lê o código qual é a nossa intenção:
>
> ```py
> conta_origem.transfere(300.0, conta_destino)
> ```
>
> A legibilidade é um ponto muito relevante pois, no dia a dia, o programador gasta muito mais tempo lendo código do que escrevendo!

__B__ - Facilitamos a manutenção pois a funcionalidade (o código) está encapsulado.
> Correto! O código dessa funcionalidade está dentro do método transfere. Dessa forma, se for preciso, basta alterar a implementação desse método.

__C__ - Melhoramos a organização do nosso código, pois as funcionalidades relacionadas à uma Conta estão dentro da classe.
> Correto! Isso é um ponto fundamental do paradigma OO. Concentramos as funcionalidades relacionadas à uma Conta dentro da classe Conta. Assim diminuímos a chance de criar código duplicado.

D - Melhoramos o desempenho pois estamos usando objetos e métodos.

## Aula 5

### 1 - Tenho alguns jogos e quero representá-los usando Python 3. Para isto já vimos que podemos criar uma classe representando este conceito do Jogo. Imagine que cada jogo tem um nome, e a quantidade de vezes que joguei o mesmo.

```py
class Jogo:
    def __init__(self, nome, vezes_que_joguei):
        self.__nome = nome
        self.__vezes_que_joguei = vezes_que_jogueiCOPIAR CÓDIGO
```

Apenas com este código, eu não consigo ver quantas vezes joguei um jogo criado. Como eu posso fazer para acessar esta informação?

__A__ - Criar um método para devolver o valor desejado.
> Correto! Sempre que eu quiser acessar algo do objeto, criarei um método.

B - Guardar o valor de quantas vezes joguei numa variável antes de passar para o construtor.

C - Criar uma função fora da classe para mostrar o valor.

D - Imprimir o valor no momento que eu criar meu objeto.

### 2 - Ainda trabalhando com a minha classe Jogo do exercício anterior, meu problema agora é alterar a quantidade de vezes que joguei o meu jogo e do jeito que criei meus atributos, o python não me aconselha a alterar diretamente o valor de __vezes_que_joguei, até porque criei os atributos privados. De que forma eu posso alterar o valor do atributo __vezes_que_joguei sem ferir o encapsulamento?

A - Definir o atributo como public, sem o __ na frente.

__B__ - Criar um método na classe para alterar o valor.
> Correto! Reforçando que tanto para acessar quanto para alterar características de um objeto precisamos criar métodos.

C - Acessar a variável disponibilizada pelo python Jogo__vezesque_joguei e alterar seu valor.

D - Criar outro objeto com o valor diferente.

### 3 - Já vimos que podemos criar getters e setters para acessar e alterar o valor de atributos privados. No python existe uma forma mais comum de criar estes getters e setters, diferente de Java, onde se coloca get ou set como prefixo de um método, usamos Propriedades. Escolha a opção que representa corretamente Propriedades para acessar dados no python.

A -
```py
@property
def prop_nome():
    return self.__nome
```

B -
```py
@property
def nome():
    return self.__nome
```

__C__ -
```py
@property
def nome(self):
    return self.__nome
```
> Correto! Esta é a forma correta de criar uma property.

D -
```py
@property
def nome():
    self.__nome
```

### 4 - Vimos no exercício anterior como podemos definir uma propriedade para acessar um atributo privado no python 3. E se quisermos alterar os atributos através de uma propriedade, qual o jeito correto de fazer?

A -
```py
@property.setter
def nome(self):
    self.__nome = nome
```

__B__ -
```py
@nome.setter
def nome(self, nome):
    self.__nome = nome
```
> Correto! Desta forma conseguimos implementar um setter no Python.

C -
```py
@property
def nome(self):
    self.__nome = nome
```

D -
```py
@property.setter
def nome(self, nome):
    return self.__nome
```

## Aula 6

### 1 - Paulo é o novo estagiário da Caelum. Em um dia de inspiração, encontrou o seguinte código em um projeto que, embora crítico, está funcionando sem nenhum bug relatado há anos:

```py
class Conta:

    def __init__(self, numero, saldo, limite ):
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
        self.__tarifaTransferencia = 8.0


    def saca(self,valor):

        if valor < (self.__saldo + self.__limite):
                self.__saldo -= valor
                print("Saque efetuado.")
        else:
                print("Saldo insuficiente.")



    def transfere(self, valor, destino):


            valorTotal = valor + self.__tarifaTransferencia

           if valorTotal < (self.__saldo + self.__limite):

                self.__saldo -= valorTotal
                destino.deposita(valor)

                print("Transferência efetuada.")
            else:
                print("Saldo insuficiente.")


    # outros métodos omitidos...COPIAR CÓDIGO
```

Como líder técnico da empresa, você precisa inspecionar as modificações que Paulo fez na classe anterior e ajudá-lo no desenvolvimento profissional. Analise o código do Paulo:

```py
class Conta:
    def __init__(self, numero, saldo, limite):
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
        self.__tarifaTransferencia = 8.0

    #NOVO MÉTODO AQUI
    def temSaldoDisponivelPara(self, valor):
        return valor < (self.__saldo + self.__limite)


    def saca(self, valor):

        if self.temSaldoDisponivelPara(valor):
            self.__saldo -= valor
            print("Saque efetuado.")
        else:
            print("Saldo insuficiente.")


    def transfere(self, valor, destino):


        valorTotal = valor + self.__tarifaTransferencia

        if self.temSaldoDisponivelPara(valorTotal):

            self.__saldo -= valorTotal
            destino.deposita(valor)

            print("Transferência efetuada.")
        else:
            print("Saldo insuficiente.")
```

A - Paulo criou mais complexidade ao projeto ao adicionar mais métodos na classe.

__B__ - Paulo pode melhorar ainda mais o código.
> Correto! Embora o método criado evite a duplicação de códigos, ele não será chamado por nenhuma outra classe do sistema. Logo, não faz sentido deixá-lo público e expô-lo na interface pública da classe.

C - Paulo não deveria mexer em código que já funciona.

D - Paulo fez uma modificação que não influenciou nem positivamente nem negativamente no projeto.

### 2 - Vimos que o Python segue uma convenção para deixar claro que um atributo ou método é considerado privado.

Referente a convenção, veja as seguintes afirmações.

Dentro de uma classe Conta ...

a) ... o atributo __saldo se torna _Conta__saldo.

b) ... o método __pode_sacar() se torna _Conta__pode_sacar().

c) ... o construtor init se torna __init__.

d) ... a referencia self se torna __self.

Quais das afirmativas estão corretas?

A - c) e d)

__B__ - a) e b)
> Correto! Usando __ alterar o nome do atributo ou método, colocando o nome da classe como prefixo.

C - a), b) e d)

D - b) e d)

### 3 - Um desenvolvedor Java acabou de conhecer Python e gostaria de saber como definir métodos privados nessa linguagem.

Assinale a alternativa que transforma o método a seguir em privado:

```py
def temSaldoDisponivelPara(self, valor):
    return valor < (self.__saldo + self.__limite)COPIAR 
```

A -
```py
def private temSaldoDisponivelPara(self, valor):
```

B -
```py
@private
def temSaldoDisponivelPara(self, valor):
```

C -
```py
def _temSaldoDisponivelPara(self, valor):
```

__D__ -
```py
def __temSaldoDisponivelPara(self, valor):
```
> Correto! A sintaxe é exatamente essa. Começando por dois underscores(_)

### 4 - Sabe-se que na classe Conta existe um método estático que pode ser visto abaixo:

```py
@staticmethod
def codigo_banco():
    return "001"
```

Qual das alternativas indica a forma de chamar esse método estático?

A -
```py
Conta(123,"Nico", 55.5, 1000.0).codigo_banco()
```

__B__ -
```py
Conta.codigo_banco()
```
> Correto! Quando definimos um método estático, ou seja, de classe, podemos chamá-lo sem a necessidade de criação de um objeto antes. Portanto a sintaxe para isso é bastante simples, bastando chamar um método depois do nome da classe.
>
> ```py
> Conta.codigo_banco()
> ```

C -
```py
Conta(self).codigo_banco()
```

D -
```py
Conta().codigo_banco()
```

### 5 - Um desenvolvedor acabou de aprender sobre métodos estáticos e está bastante entusiasmado com essa possibilidade. Das alternativas a seguir qual representa melhor as recomendações sobre uso desse recurso?

A - Métodos estáticos dizem respeito a métodos do objeto (instância) em vez de classe.

B - Métodos estáticos favorecem o reaproveitamento de código no sistema.

__C__ - Métodos estáticos devem ser usados com cautela caso contrário pode-se fugir do paradigma da orientação a objetos.
> Correto! Métodos estáticos tem um cheiro de linguagem procedural já que independe de um objeto para ser chamado e não manipula informações/atributos de objetos. Deve ser usado com bastante cautela!

D - Deve-se sempre preferir usar métodos estáticos a métodos não estáticos.
