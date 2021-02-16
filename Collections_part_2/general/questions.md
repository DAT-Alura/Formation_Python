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
