from codigo.livro import Livro

def test_abrir():
    livro = Livro()
    livro.abrir()
    assert livro.get_livro_aberto == True

def test_fechar():
    livro = Livro()
    livro.fechar()
    assert livro.get_livro_aberto == False

def test_marcar_pagina():
    livro = Livro()
    livro.set_numero_paginas(100)
    livro.marcar_pagina(50)
    assert livro.get_pagina_atual() == 50

def test_avancar_pagina():
    livro = Livro()
    livro.set_numero_paginas(100)
    livro.avancar_pagina()
    assert livro.get_pagina_atual() == 2

def test_avancar_pagina_na_ultima():
    livro = Livro()
    livro.set_numero_paginas(10)
    livro.marcar_pagina(10)
    livro.avancar_pagina()
    assert livro.get_pagina_atual() == 10

def test_retroceder_pagina():
    livro = Livro()
    livro.marcar_pagina(5)
    livro.retroceder_pagina()
    assert livro.get_pagina_atual() == 4

def test_retroceder_pagina_na_primeira():
    livro = Livro()
    livro.retroceder_pagina()
    assert livro.get_pagina_atual() == 1
