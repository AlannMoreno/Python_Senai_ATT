from pytest import MonkeyPatch
from InterfaceUsuario import InterfaceUsuario
from DestinoRepositorio import DestinoRepositorio


def test_solicitar_input_usuario(monkeypatch: MonkeyPatch):
    destino_repositorio = DestinoRepositorio()
    interface_usuario = InterfaceUsuario(destino_repositorio)

    monkeypatch.setattr("builtins.input", lambda _: "21")
    resultado = interface_usuario.solicitar_input_usuario()

    assert resultado == 21
    assert type(resultado) == int

