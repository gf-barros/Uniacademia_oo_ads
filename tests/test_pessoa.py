from codigo.pessoa import Pessoa

def test_envelhecer():
    pessoa = Pessoa()
    pessoa.set_idade(20)
    pessoa.envelhecer()
    assert pessoa.get_idade() == 21

def test_crescer_menor_de_21():
    pessoa = Pessoa()
    pessoa.set_idade(18)
    pessoa.set_altura(170)
    pessoa.crescer(5)
    assert pessoa.get_altura() == 175

def test_crescer_maior_de_21():
    pessoa = Pessoa()
    pessoa.set_idade(25)
    pessoa.set_altura(170)
    pessoa.crescer(5)
    assert pessoa.get_altura() == 170

def test_ganhar_peso():
    pessoa = Pessoa()
    pessoa.set_peso(60)
    pessoa.ganhar_peso(5)
    assert pessoa.get_peso() == 65

def test_perder_peso():
    pessoa = Pessoa()
    pessoa.set_peso(60)
    pessoa.perder_peso(5)
    assert pessoa.get_peso() == 55

def test_perder_peso_nao_fica_negativo():
    pessoa = Pessoa()
    pessoa.set_peso(3)
    pessoa.perder_peso(5)
    assert pessoa.get_peso() == 0
