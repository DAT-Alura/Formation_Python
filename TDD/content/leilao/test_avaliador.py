from unittest import TestCase

from leilao.dominio import Lance, Leilao, Usuario


# python -m unittest leilao/test_avaliador.py
class TestAvaliador(TestCase):

    def setUp(self):
        self.daniel = Usuario("Daniel")
        self.lance_do_daniel = Lance(self.daniel, 100.0)
        self.leilao = Leilao("Celular")
    
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        akio = Usuario("Akio")
        lance_do_akio = Lance(akio, 150.0)
        
        self.leilao.propoe(self.lance_do_daniel)
        self.leilao.propoe(lance_do_akio)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        akio = Usuario("Akio")
        lance_do_akio = Lance(akio, 150.0)
        
        self.leilao.propoe(lance_do_akio)
        self.leilao.propoe(self.lance_do_daniel)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_daniel)

        valor_esperado = 100.0

        self.assertEqual(valor_esperado, self.leilao.menor_lance)
        self.assertEqual(valor_esperado, self.leilao.maior_lance)

    def teste_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        akio = Usuario("Akio")
        lance_do_akio = Lance(akio, 150.0)
        
        teixeira = Usuario("Teixeira")
        lance_do_teixeira = Lance(teixeira, 200.0)

        self.leilao.propoe(self.lance_do_daniel)
        self.leilao.propoe(lance_do_akio)
        self.leilao.propoe(lance_do_teixeira)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
