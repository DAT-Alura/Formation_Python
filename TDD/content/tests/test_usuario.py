import pytest

from leilao.dominio import Usuario, Leilao

@pytest.fixture()
def daniel():
    return Usuario("Daniel", 100.0)

@pytest.fixture()
def leilao():
    return Leilao("Celular")

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(daniel, leilao):
    daniel.propoe_lance(leilao, 50.0)

    assert daniel.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(daniel, leilao):
    daniel.propoe_lance(leilao, 1.0)

    assert daniel.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(daniel, leilao):
    daniel.propoe_lance(leilao, 100.0)

    assert daniel.carteira == 0

def test_nao_deve_permitir_propor_lance_com_um_valor_maior_do_que_o_da_carteira(daniel, leilao):
    with pytest.raises(ValueError):
        daniel.propoe_lance(leilao, 200.0)
