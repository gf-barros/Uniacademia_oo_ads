class Veiculo:

    def __init__(self):
        self.__marca = ""
        self.__modelo = ""
        self.__ano = 2026
        self.__velocidade_atual = 0
        self.__ligado = True

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca 

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    def get_ligado(self):
        return self.__ligado

    def get_velocidade_atual(self):
        return self.__velocidade_atual

    def set_velocidade_atual(self, velocidade): 
        self.__velocidade_atual = velocidade

    def acelerar(self, velocidade):
        self.__velocidade_atual += velocidade

    def frear(self, velocidade):
        self.__velocidade_atual -= velocidade
        if self.__velocidade_atual <= 0:
            self.__velocidade_atual = 0


