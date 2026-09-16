from codigo.produto import Produto

def test_adicionar_estoque():
    produto = Produto()
    produto.adicionar_estoque(10)
    assert produto.get_quantidade_estoque() == 10

def test_remover_estoque_com_quantidade_suficiente():
    produto = Produto()
    produto.adicionar_estoque(10)
    produto.remover_estoque(4)
    assert produto.get_quantidade_estoque() == 6

def test_remover_estoque_sem_quantidade_suficiente():
    produto = Produto()
    produto.adicionar_estoque(3)
    produto.remover_estoque(5)
    assert produto.get_quantidade_estoque() == 3

def test_aplicar_desconto():
    produto = Produto()
    produto.set_preco(100)
    produto.aplicar_desconto(10)
    assert produto.get_preco() == 90
