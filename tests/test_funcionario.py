from codigo.funcionario import Funcionario

def test_receber_aumento():
    funcionario = Funcionario()
    funcionario.set_salario(1000)
    funcionario.receber_aumento(10)
    assert funcionario.get_salario() == 1100

def test_mudar_departamento():
    funcionario = Funcionario()
    funcionario.mudar_departamento("Vendas")
    assert funcionario.get_departamento() == "Vendas"

