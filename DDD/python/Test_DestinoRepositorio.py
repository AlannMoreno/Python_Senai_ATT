from Destino import Destino
from DestinoRepositorio import DestinoRepositorio


def test_adicionar_destino():

    destino_repositorio = DestinoRepositorio()
    destino_repositorio.lista_repositorio = []
    destino1 = Destino(71, "Salvador")


    destino_repositorio.adicionar_destino(Destino(31, "Belo Horizonte"))
    destino_repositorio.adicionar_destino(Destino(32, "Juiz de Fora"))
    destino_repositorio.adicionar_destino(Destino(19, "Campinas"))
    destino_repositorio.adicionar_destino(Destino(27, "Vitória"))


    assert len(destino_repositorio.lista_repositorio) == 4
    assert not destino1 in destino_repositorio.lista_repositorio
    assert type (destino_repositorio.lista_repositorio) == list


def Test_checa_se_destino_existe():

    destino_repositorio = DestinoRepositorio()

    
    destino_repositorio.adicionar_destino(Destino(21, "Rio de Janeiro"))
    resultadoOK = destino_repositorio.checa_se_destino_existe(21)
    resultado_not_ok = destino_repositorio.checa_se_destino_existe(6)


    assert len(destino_repositorio.lista_repositorio) == 1
    assert resultadoOK == True
    assert resultado_not_ok == False  


def test_obter_destino_pelo_ddd():

    destino_repositorio = DestinoRepositorio()
    

    destino_repositorio.adicionar_destino(Destino(21, "Rio de Janeiro"))
    resultado = destino_repositorio.obter_destino_pelo_ddd(21)

    assert len(destino_repositorio.lista_repositorio) == 1
    assert resultado == "Rio de Janeiro"



