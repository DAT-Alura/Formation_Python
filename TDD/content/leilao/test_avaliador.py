from unittest import TestCase

from leilao.dominio import Lance, Leilao, Usuario, Avaliador


# python -m unittest leilao/test_avaliador.py
class TestAvaliador(TestCase):

    def setUp(self):
        self.daniel = Usuario("Daniel")
        self.lance_do_daniel = Lance(self.daniel, 100.0)
        self.leilao = Leilao("Celular")
    
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        akio = Usuario("Akio")
        lance_do_akio = Lance(akio, 150.0)
        
        self.leilao.lances.append(self.lance_do_daniel)
        self.leilao.lances.append(lance_do_akio)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        akio = Usuario("Akio")
        lance_do_akio = Lance(akio, 150.0)
        
        self.leilao.lances.append(lance_do_akio)
        self.leilao.lances.append(self.lance_do_daniel)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.lances.append(self.lance_do_daniel)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        valor_esperado = 100.0

        self.assertEqual(valor_esperado, avaliador.menor_lance)
        self.assertEqual(valor_esperado, avaliador.maior_lance)

    def teste_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        akio = Usuario("Akio")
        lance_do_akio = Lance(akio, 150.0)
        
        teixeira = Usuario("Teixeira")
        lance_do_teixeira = Lance(teixeira, 200.0)


        self.leilao.lances.append(self.lance_do_daniel)
        self.leilao.lances.append(lance_do_akio)
        self.leilao.lances.append(lance_do_teixeira)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
