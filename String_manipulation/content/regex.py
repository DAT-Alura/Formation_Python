import re

padrao = "[0-9]{4,5}-?[0-9]{4}"
texto =  "Meu número para contato é 26335723"
retorno = re.findall(padrao,texto)
print(retorno)
