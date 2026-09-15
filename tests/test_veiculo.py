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