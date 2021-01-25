# Construtores com valores padrao

Imagine que uma conta bancária no banco AluraInvest geralmente é criada com limite de mil reais.

O código de criação de 3 objetos do tipo Conta fica assim:

```py
conta1 = Conta(1, "Fulano", 0.0, 1000.0)
conta2 = Conta(2, "Beltrano", 0.0, 1000.0)
conta3 = Conta(3, "Sicrano", 0.0, 2000.0)
```

Como podemos fazer no Python para economizar a escrita do código de criação de um objeto Conta? Neste caso podemos supor que apenas as contas com limites especiais precisariam passar tal argumento (no exemplo acima apenas conta3 tem um limite especial). Isso é feito colocando na declaração da função construtora __init__ um valor padrão para o limite.

Assim:

```py
class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
```

E o código de nossos 3 objetos ficaria assim:

```py
conta1 = Conta(1, "Fulano", 0.0)
conta2 = Conta(2, "Beltrano", 0.0)
conta3 = Conta(3, "Sicrano", 0.0, 2000.0)
```

# Para saber mais: SOLID

Falamos nessa aula sobre a coesão que é ligado ao principio de responsabilidade única. Aprendemos que uma classe deve ter apenas uma responsabilidade (ou deve ter apenas uma razão para existir). Em outras palavras, ela não deve assumir responsabilidades que não são delas.

Além desse princípio de responsabilidade única existem outras que foram definidos através do Robert C. Martin no início dos anos 2000 e são conhecidos pelo acrônimo SOLID:

- S - Single responsibility principle
- O - Open/closed principle
- L - Liskov substitution principle
- I - Interface segregation principle
- D - Dependency inversion principle

Na Alura temos cursos específicos sobre o SOLID, mas fique tranquilo, na medida que você avança no mundo OO esses princípios ficam mais claros e fáceis de se entender.

# Atributo estatico

Conhecemos nessa aula os métodos estáticos que podem ser chamados a partir da classe, sem ter um objeto criado. No exemplo abaixo criamos um classe Circulo que possui um método estático obter_pi():

```py
class Circulo:

    @staticmethod
    def obter_pi():
        return 3.14
```

E agora podemos usar esse método estático a partir da classe:

```py
Circulo.obter_pi()
3.14
```

Repare que o método existe apenas para devolver o valor do PI. Nada errado com isso, mas já que usamos um valor simples não bastaria usar um atributo simples? Em outras palavras, será que é preciso criar um método? A resposta é não pois podemos usar um atributo da classe. Veja como é simples:

```py
class Circulo:

    PI = 3.14
```

Repare que não usamos self e o atributo nem foi definido dentro do __init__. O atributo faz parte da classe, ou seja, é um atributo estático que pode ser usado sem ter criado um objeto. Veja como fica simples:

```py
Circulo.PI
3.14
```
