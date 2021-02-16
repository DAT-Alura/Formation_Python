# Aula 1

Fomos chamados para verificar os dados das pessoas que fizeram o curso de data science e machine learning, com a finalidade de filtrar se estão assistindo um curso apenas ou ambos. Então vamos analisar o seguinte conjunto:

```py
usuarios_data_science = {15, 23, 43, 56}

usuarios_machine_learning = {13, 23, 56, 42}
```

Como podemos fazer a verificação dos dados?

__A__ - Utilizando o & para verificar quais usuários estão em ambos os conjuntos.
> Quando utilizamos o & pegamos os números que estão em ambos conjuntos e mostramos.

B - Utilizamos o - para juntar os conjuntos, assim a separação é feita automaticamente.

C - Utilizando o | para remover os números repetidos.

# Aula 2

Marcela está desenvolvendo um ecommerce que contém apenas 6 usuários cadastrados. Portanto, como não há repetição de números dentro de um conjunto, ela criou um conjunto de dados e cadastrou os usuários conforme o ID.

```py
usuarios = {1,5,76,34,52,13}
```

Então foi solicitado para que Marcela adicione um novo usuário com o ID 7, neste conjunto.

Como ela pode fazer isto?

A - Usando a função adicionarID para adicionar o ID 7 ao seu conjunto.

B - Usando a função append para adicionar o ID 7 ao seu conjunto.

__C__ - Usando a função add para adicionar o ID 7 ao seu conjunto.
> A função add é nativa do Python para utilizar com conjuntos, sendo podemos usar ela para inserir o ID ao conjunto.

# Aula 3

Sérgio precisa implementar um dicionário que tenha o nome e a idade de seus clientes, para saber a faixa etária deles. Esta implementação terá mil registros. Após fazer isto, ele deve verificar alguns clientes.

Como ele pode fazer isto?

__A__ - Ele pode utilizar a função get para verificar os clientes.
> Utilizar a função GET, verificando se o cliente está contido no dicionário.

B - Ele pode utilizar a função keys para ver os valores do dicionário.

C - Ele pode utilizar a função dict para fazer a filtragem desses clientes.

# Aula 4

Conforme aprendemos em aula, é possível fazer a contagem de palavras, utilizando o default dict e o Counter para contar valores.

Como podemos contar as aparições de cada palavra da seguinte frase?

```py
texto = "Bem vindo meu nome é Elias irei falar sobre os meus gostos eu gosto muito de cachorros e gatos eu gosto também de beber café"

texto = texto.lower()
```

A - Atribuímos o texto em uma lista e percorremos a lista para mostrar os valores

B - Utilizando o default dict para fazer a contagem dos valores.

__C__ - Ele vai utilizar utilizar o seguinte aparicoes = Counter(texto.split()) , para fazer a contagem das aparições.
> Assim nós estamos separando as letras e fazendo a contagem dos valores.

# Aula 5

Nós estamos implementando uma nova funcionalidade (feature) no sistema de uma livraria. Este setor está inserindo uma função para contar a frequência de cada letra nos textos cadastrados. Temos então o seguinte código:

```py
def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  print("{} => {:.2f}%".format(caractere, proporcao * 100))
```

Mas isso ainda não é o suficiente, queremos também mostrar as dez letras mais frequentes.

De qual maneira nós podemos implementar isto?

__A__ -
Temos que usar a função most_common(10) para pegar as dez letras mais frequentes, fazer a atribuição dele em uma variável e percorrê-la, vendo a proporção e os caracteres.

```py
mais_comuns = proporcoes.most_common(10)
 for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))
```
> Usando ```most_common``` passamos por parâmetro o número de elementos que queremos, no nosso caso foi 10. Ele vai nos retornar uma lista de tuplas com os elementos e suas devidas proporções.

B -
Usando a função keys para fazer a contagem das chaves que temos assim ela vai nos retornar as dez primeiras chaves.

C -
Usando a função values para fazer a contagem dos valores que temos.