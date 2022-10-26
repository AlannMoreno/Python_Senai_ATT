from Destino import Destino

class DestinoRepositorio:
    lista_repositorio: Destino = []

    def __init__(self) -> None:
        pass
    
    def adicionar_destino(self, destino: Destino) -> None:
        self.lista_repositorio.append(destino)

    def checa_se_destino_existe(self, ddd: int) -> bool:
        for i in self.lista_repositorio:
            if(ddd == i.ddd):
                return True 
        
        return False

    def obter_destino_pelo_ddd(self, ddd: int) -> str:
        for i in self.lista_repositorio:
            if(ddd == i.ddd):
                return i.nome_destino

        return "Cidade não encontrada....."           