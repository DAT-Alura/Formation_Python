# Aula 1

Nesta aula construímos uma classe que verifica se o CPF inserido pelo usuário é valido ou não. Inicialmente, o documento foi validado somente pela quantidade de caracteres e, em seguida, por meio de um pacote que baixamos no PyPi(Python Packege Index). A classe abaixo deve verificar o CPF inserido no momento que é instanciada:

```py
class ValidaCpf:
    def __init__(self, documento):
        self.analisa_cpf(documento)

    def analisa_cpf(self, documento):
        if len(documento) == 11:
            valida_cpf = CPF()
            if valida_cpf.validate(documento):
                self.cpf = documento
                print('CPF salvo')
            else:
                print('CPF inserido não é valido')
        else:
            print('Número de digitos incorreto')

cpf_um = 1235436791
cpf_dois = 12354367912
cpf_tres = '12354367996'

objeto_cpf_um = ValidaCpf(cpf_um )
objeto_cpf_dois = ValidaCpf(cpf_dois )
objeto_cpf_tres = ValidaCpf(cpf_tres )
```

Com base no que vimos durante a aula indique qual dos objetos acima retorna CPF salvo

A - objeto_cpf_dois

B - objeto_cpf_tres
> Correto! A variável cpf_tres possui 11 caracteres e é do tipo str.

C - objeto_cpf_um

# Aula 2

Durante esta aula construímos uma factory que decidia entre instanciar uma classe responsável por CPFs e outra por CNPJs. Uma das vantagens de usar esse padrão de projeto é facilitar o crescimento do código.

Avalie as afirmativas abaixo sobre as alterações necessárias, no caso de inserirmos um documento novo, e indique qual é a verdadeira.

A - É preciso criar um método novo dentro da Factory.

__B__ - A nova classe precisará ter todos os métodos com os mesmos nomes das outras classes filhas.
> Correto! Para conseguirmos usar qualquer instância retornada pelo Factory livremente, os métodos das classes filhas precisam ser iguais.

C - Não é possível inserir mais um documento, pois esse padrão de projeto só pode decidir entre instanciar no máximo duas classes diferentes.

D - Será preciso passar mais um argumento quando chamarmos a Factory.
