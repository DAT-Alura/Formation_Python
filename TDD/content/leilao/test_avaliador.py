from unittest import TestCase

from leilao.dominio import Lance, Leilao, Usuario, Avaliador


# python -m unittest leilao/test_avaliador.py
class TestAvaliador(TestCase):
    
    def test_avalia(self):
        daniel = Usuario("Daniel")
        akio = Usuario("Akio")

        lance_do_daniel = Lance(daniel, 100.0)
        lance_do_akio = Lance(akio, 150.0)

        leilao = Leilao("Celular")

        leilao.lances.append(lance_do_daniel)
        leilao.lances.append(lance_do_akio)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
