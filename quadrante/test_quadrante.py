from Cordenadas import Cordenadas
from Quadrante import Quadrante

def test_caso1():

    x = 5
    y = 8

    cordenadas = Cordenadas(x, y)
    quadrante = Quadrante(cordenadas)


    resultado = quadrante.obter_cordenadas_quadrante()


    assert resultado == "Primeiro"

def test_caso2():

    x = -5
    y = 9

    cordenadas = Cordenadas(x, y)
    quadrante = Quadrante(cordenadas)


    resultado = quadrante.obter_cordenadas_quadrante()


    assert resultado == "Segundo"

def test_caso3():

    x = -15
    y = -7

    cordenadas = Cordenadas(x, y)
    quadrante = Quadrante(cordenadas)


    resultado = quadrante.obter_cordenadas_quadrante()


    assert resultado == "Terceiro"

def test_caso4():

    x = 10
    y = -5

    cordenadas = Cordenadas(x, y)
    quadrante = Quadrante(cordenadas)


    resultado = quadrante.obter_cordenadas_quadrante()


    assert resultado == "Quarto"

def test_caso_nuloX():

    x = 0
    y = 30

    cordenadas= Cordenadas(x, y)
    quadrante = Quadrante(cordenadas)

    resultado = quadrante.obter_cordenadas_quadrante()

    assert resultado == ""

def test_caso_nuloY():

    x = -3
    y = 0

    cordenadas= Cordenadas(x, y)
    quadrante = Quadrante(cordenadas)

    resultado = quadrante.obter_cordenadas_quadrante()

    assert resultado == ""

def test_caso_error():

    x = 2
    y = 5

    cordenadas = Cordenadas(x, y)
    quadrante = Quadrante(cordenadas)

    resultado = quadrante.obter_cordenadas_quadrante()

    assert resultado == "Segundo"
