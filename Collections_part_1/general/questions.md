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
