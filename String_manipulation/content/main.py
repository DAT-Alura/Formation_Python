from extrator_argumentos_url import ExtratorArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=700"
objeto = ExtratorArgumentosUrl(url)
print(objeto.retorna_moedas())
