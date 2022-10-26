from DestinoRepositorio import DestinoRepositorio

class InterfaceUsuario:
    def __init__(self, destino_repositorio : DestinoRepositorio) -> None:
        self.destino_repositorio = destino_repositorio

    def solicitar_input_usuario(self) -> int:
        resultado = int(input("Informe o DDD para procurar seu destino"))
        return resultado

    def exibir_destino(self):
        ddd = self.solicitar_input_usuario()

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20}\n"
        menu = formatText.format("DDD", "Name of city")

        for i in self.list_cities:
            menu += formatText.format(i.ddd, i.name_city)

        return menu       