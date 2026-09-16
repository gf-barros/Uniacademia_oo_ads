from codigo.conta_bancaria import ContaBancaria

def test_depositar():
    conta = ContaBancaria()
    conta.depositar(100)
    assert conta.get_saldo() == 100

def test_sacar_com_saldo_suficiente():
    conta = ContaBancaria()
    conta.depositar(100)
    conta.sacar(40)
    assert conta.get_saldo() == 60

def test_sacar_sem_saldo_suficiente():
    conta = ContaBancaria()
    conta.depositar(30)
    conta.sacar(50)
    assert conta.get_saldo() == 30
