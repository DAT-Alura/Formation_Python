# Aula 1

Gabriel é programador e trabalha em uma escola dando aula de matemática. No fim do semestre, Gabriel passa as notas dos alunos para uma lista feita em Python que o ajuda no controle das notas. Um dia, acidentalmente, Gabriel duplicou as notas e precisava remover as duplicadas.

```py
notas = [2, 2, 3, 5]
```

Como essa duplicidade pode ser removida?

A - Utilizando a função append para remover as notas duplicadas, o Python remove os elementos que estão por último no lista.

__B__ - Utilizando a função`remove()´ e passando como parâmetro a nota duplicada para ser excluída. Essa função vai retirar a primeira aparição da nota, resolvendo a duplicidade.
> Exatamente! Quando usamos a função `remove()´ ela vai percorrer nosso array e remover a primeira aparição do elemento que passamos como parâmetro.

C - Refazendo a lista e removendo os elementos manualmente, pois o Python não permite que sejam removidos elementos de uma lista.

# Aula 2

Estamos estudando tuplas e listas. Temos um conjunto de dados que nos foi dado e precisamos adicionar cada conjunto em seu devido lugar. Os dados desses conjuntos são o saldo e agência bancária (o valor de agência bancária é imutável):

```py
agencia = [10, 22, 33, 44]

saldo =  [1000, 2000, 3000, 4000]
```

Qual a melhor forma de declarar cada um desses valores?

A - Utilizando tupla para ambos agencia = (10,22,33,44) saldo= (1000,2000,3000,4000)

__B__ - Utilizando tupla e lista agencia = (10,22,33,44) saldo = [1000,2000,3000,4000]
> Usando a tupla para que o valor da nossa agência seja imutável. E deixar o saldo como lista pois podemos ter aumento ou diminuição do saldo ao longo do tempo.

C - Utilizando lista e tupla agencia = [10,22,33,44] saldo= (1000,2000,3000,4000)

D - Utilizando lista para ambos agencia = [10,22,33,44] saldo = [1000,2000,3000,4000]

# Aula 3

Mayra é do setor de desenvolvimento de uma empresa. Foi pedido para que ela fizesse um array numérico em Python, utilizando a biblioteca arr, para guardar as notas dadas pelos clientes no aplicativo da empresa, mas Mayra não sabe quais são as características do arr do Python para criação de array.

Quais seriam as características de criação deste array no Python?

__A__ - Para que o array do Python funcione, temos que passar o tipo dele.
> Precisamos passar o tipo do Array para que ele fique mais eficiente.

B - Podemos passar qualquer tipo de valor no array.

C - Não precisamos passar o tipo do array para o Python, pois ele detecta de maneira automática.

# Aula 4

No banco onde Guilherme trabalha está acontecendo um problema: está acontecendo a comparação de duas contas com os mesmos atributos. Observe o seguinte código:

```py
conta_do_gui = ContaCorrente(15)

conta_da_dani = ContaCorrente(15)

if(conta_do_gui == conta_da_dani):
    print(“São iguais”)
else:
    print(“São diferentes”)
```

Quando fazemos a comparação com o __if__, está retornando False, quando deveria retornar True.

O que Guilherme pode fazer para que o retorno seja True?

A - Ele precisa fazer com que ambas as contas tenham o mesmo nome de instância.

B - Ele precisa fazer a instância de ambas as contas na mesma hora.

__C__ - Implementar o método eq, onde comparamos o que está vindo como parâmetro ao invés do objeto inteiro.
> Com o método eq podemos fazer a comparação que desejamos.

# Aula 5

Gabriela está revisando um código em Python que contém uma lista de idade, que está percorrendo esta lista e mostrando o índice e a idade:

```py
idades = [15,87,37,45,56,32,49,37]
for i in range(len(idades)):
    print(i,idades[i])
```

Este código faz a numeração da idade e a põe um index ao lado de cada idade, mas isto é muito trabalhoso de se fazer.

Como o código pode ser melhorado, de modo a facilitar a implementação ?

A - Utilizando a função de extends.

__B__ - Utilizando o enumerate para percorrer nossa lista e numerar cada valor.
> Quando utilizamos o enumerate, ele faz a enumeração dos valores automaticamente, assim evitaremos código a mais.

C - Temos que fazer uma lista auxiliar e percorrer ambas para que a numeração seja feita.

# Aula 6

Conforme foi passado na aula, aprendemos a ordenar a lista usando idades.sort(). Porém, podemos não querer alterar a lista original, mas visualizar os valores da lista em ordem crescente.

```py
idades = [12,90,1,8,10,25,32,31,40,50]
```

Como podemos fazer isso com Python?

A - Utilizaremos o reversed para reverter a lista em uma lista ordenada list(reversed(idades)).

__B__ - Utilizaremos o sorted para retornar uma nova lista ordenada: sorted(idades).
> Exatamente! Caso utilizássemos o idades.sort(), a lista original seria alterada, pois esse comando, além de ordenar, atribui o valor à lista original.

C - Utilizaremos o sort mesmo para deixar a lista ordenada, pois ele já faz a atribuição automaticamente: idades.sort().

# Aula 7

Estamos desenvolvendo um projeto para o banco digital Bytebank que trabalha com contas salário. Na nossa classe de conta salário, implementamos os seguintes métodos :

```py
class ContaSalario:
  def __init__(self,codigo):
    self._codigo = codigo
    self._saldo = 0

  def __eq__(self,outro):
    if(type(outro) != ContaSalario):
      return False
    return self._codigo == outro._codigo and self._saldo == outro._saldo

  def deposita(self, valor):
    self._saldo += valor
  def __str__(self):
    return "[>>> codigo: {} Saldo: {}]".format(self._codigo, self._saldo)
```

Nenhum desses métodos retorna o saldo da conta salário e sabemos que, para manter as boas práticas, não podemos acessar diretamente o atributo da classe para obter o saldo que precisamos.

Qual é a melhor maneira para se obter o saldo?

__A__ - Temos que importar o attrgetter e passar o valor do saldo por parâmetro key=attrgetter("_saldo").
> Quando importamos o attrgetter, temos que passar a chave do valor que queremos, pois assim não acessamos o atributo diretamente.

B - Temos que fazer uma função def extrai_saldo(conta), que retorna o saldo da conta. def extrai_saldo(conta): return conta._saldo

C - Temos que implementar na função \_\_init__ dentro dela vamos retornar o saldo da conta def \_\_init__(self,codigo): self._codigo = codigo self._saldo = 0 return “saldo:self._saldo”.

# Aula 8

Uma empresa está desenvolvendo um sistema para conta de bancos fazendo a implementação lógica em um dos modelos de conta salário.

```py
class ContaSalario:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False

    return self._codigo == outro._codigo and self._saldo == outro._saldo

  def __lt__(self, outro):
    if self._saldo != outro._saldo:
      return self._saldo < outro._saldo

    return self._codigo < outro._codigo
```

Até agora foram implementados os métodos \_\_eq__() e \_\_lt__() , que comparam valores dos salários, então foram criadas três contas para teste de comparação entre elas.

```py
conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)
```

O banco quer comparar se o valor contido na conta do cliente é maior ou igual ou menor ou igual de outro cliente.

Como podemos fazer isto?

A - Temos que criar str para pode fazer este tipo de comparações.

__B__ - Podemos fazer uma anotação e fazer a importação da biblioteca total_ordering.
> Com isto não implementamos métodos de comparação, mas temos que ter os métodos eq e o lt.

C - Temos que fazer vários métodos para fazer as comparações.
