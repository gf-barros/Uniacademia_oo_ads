class Livro:

    def __init__(self):
        self.__titulo = ""
        self.__autor = ""
        self.__ano_publicacao = 0
        self.__numero_paginas = 0
        self.__genero = ""
        self.__pagina_atual = 1
        self.__livro_aberto = False

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_ano_publicacao(self):
        return self.__ano_publicacao

    def set_ano_publicacao(self, ano_publicacao):
        self.__ano_publicacao = ano_publicacao

    def get_numero_paginas(self):
        return self.__numero_paginas

    def set_numero_paginas(self, numero_paginas):
        self.__numero_paginas = numero_paginas

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_pagina_atual(self):
        return self.__pagina_atual

    def set_pagina_atual(self, pagina_atual):
        self.__pagina_atual = pagina_atual

    def get_livro_aberto(self):
        return self.__livro_aberto

    def set_livro_aberto(self, aberto):
        self.__livro_aberto = aberto

    def abrir(self):
        self.__livro_aberto = True
        print("O livro foi aberto.")

    def fechar(self):
        self.__livro_aberto = False
        print("O livro foi fechado.")

    def marcar_pagina(self, pagina):
        self.__pagina_atual = pagina

    def avancar_pagina(self):
        if self.__pagina_atual < self.__numero_paginas:
            self.__pagina_atual += 1

    def retroceder_pagina(self):
        if self.__pagina_atual > 1:
            self.__pagina_atual -= 1
