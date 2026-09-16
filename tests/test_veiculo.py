from codigo.veiculo import Veiculo

def test_alterar_velocidade():
    veiculo = Veiculo()
    veiculo.set_velocidade_atual(200)
    assert veiculo.get_velocidade_atual() == 200

def test_frear():
    veiculo = Veiculo()
    veiculo.set_velocidade_atual(200)
    veiculo.frear(200)
    assert veiculo.get_velocidade_atual() == 0

def test_frear_nao_deixa_velocidade_negativa():
    veiculo = Veiculo()
    veiculo.set_velocidade_atual(50)
    veiculo.frear(80)
    assert veiculo.get_velocidade_atual() == 0

def test_ligar():
    veiculo = Veiculo()
    veiculo.desligar()
    veiculo.ligar()
    assert veiculo.get_ligado() is True

def test_desligar():
    veiculo = Veiculo()
    veiculo.set_velocidade_atual(100)
    veiculo.desligar()
    assert veiculo.get_ligado() is False
    assert veiculo.get_velocidade_atual() == 0
