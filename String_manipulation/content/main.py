from extrator_argumentos_url import ExtratorArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = cambio.retorna_moedas()
valor = cambio.retorna_valor()
print(moeda_origem, moeda_destino, valor)

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"
cambio = ExtratorArgumentosUrl(url)
print(cambio)
moeda_origem, moeda_destino = cambio.retorna_moedas()
valor = cambio.retorna_valor()
print(moeda_origem, moeda_destino, valor)

