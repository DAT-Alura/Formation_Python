# Aula 1

Nesta aula aprendemos como retirar partes de uma string utilizando slice (fatiamento). Com esse conhecimento veja o código abaixo:

```py
texto = “Izuku Midoriya”
texto[0:10]
texto2 = texto[:4]
print( texto2)
print(texto)
```

Qual será a Saída deste código?

A -
```py
Izuk
Izuku Mido
```

B -
```py
Iuzuku
Izuku Midoriya
```

__C__ -
```py
Izuk
Izuku Midoriya
```
> Correta! Uma string não é modificada quando fazemos qualquer fatiamento nela, e além disso o segundo índice é exclusor.

---

Vimos nessa aula que o método find ajuda a capturar valores de uma forma mais dinâmica dentro de uma string qualquer. Analise o código abaixo:

```py
celular = "(41)96574-1728"
indiceInicialCodigoArea = x
indiceFinalCodigoArea   = y

print (celular[indiceInicialCodigoArea:indiceFinalCodigoArea])
```

Com o objetivo de retirar o código de área sem os “()”, os valores de x e y podem ser substituídos por:

__A__ -
```py
Termo x = celular.find("(") + 1
Termo y = celular.find(")")
```
> Correto! É preciso colocar um + 1 no termo x para poder pegar o índice após o (.

B -
```py
Termo x = celular.find("(")
Termo y = celular.find(")")
```

C -
```py
Termo x = celular.find("(") + 1
Termo y = celular.find(")") + 1
```
