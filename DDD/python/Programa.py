from Destino import Destino
from DestinoRepositorio import DestinoRepositorio
from InterfaceUsuario import InterfaceUsario

destino_repositorio = DestinoRepositorio()
destino_repositorio.adicionar_destino(Destino(71, "Salvador"))
destino_repositorio.adicionar_destino(Destino(21, "Rio de Janeiro"))
destino_repositorio.adicionar_destino(Destino(32, "Juiz de Fora"))
destino_repositorio.adicionar_destino(Destino(19, "Campinas"))
destino_repositorio.adicionar_destino(Destino(27, "Vitória"))
destino_repositorio.adicionar_destino(Destino(11, "São Paulo"))
destino_repositorio.adicionar_destino(Destino(31, "Belo Horizonte"))
destino_repositorio.adicionar_destino(Destino(61, "Brasília"))

print(destino_repositorio)

interface_usuario = InterfaceUsario(destino_repositorio)

while True:
    resultado = self.obter_destino_pelo_ddd

    if (resultado == "Cidade não encontrada....."):
        print(resultado)
        break
    else:
        print(resultado)
