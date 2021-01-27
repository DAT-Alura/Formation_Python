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
