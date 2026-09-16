class Funcionario:

    def __init__(self):
        self.__nome = ""
        self.__cargo = ""
        self.__salario = 0
        self.__departamento = ""

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def get_departamento(self):
        return self.__departamento

    def set_departamento(self, departamento):
        self.__departamento = departamento

    def receber_aumento(self, percentual):
        self.__salario += self.__salario * percentual / 100

    def mudar_departamento(self, novo_departamento):
        self.__departamento = novo_departamento

    def exibir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Cargo: {self.__cargo}")
        print(f"Salário: {self.__salario}")
        print(f"Departamento: {self.__departamento}")
