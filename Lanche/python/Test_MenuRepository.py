from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order


def test_set_menu_item():
    # Arrange
    
    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Teste one", 10)
    menu2 = Menu(2, "Teste two", 5)
    menu3 = Menu(3, "Teste tree", 2)

    # Act

    menu_repository.set_menu_item(menu1)
    menu_repository.set_menu_item(menu2)

    # Assert

    assert len(menu_repository.menu_itens) == 2
    assert not menu3 in menu_repository.menu_itens
    assert type(menu_repository.menu_itens) == list


def test_check_if_itens_exists():
    # Arrange

    menu_repository = MenuRepository()
    menu_repository.menu_itens = []
    menu1 = Menu(1, "Teste one", 10)

    # Act

    menu_repository.set_menu_item(menu1)
    resultOK = menu_repository.check_if_itens_exists(Order(1,1))
    resultNOK = menu_repository.check_if_itens_exists(Order(2,2))

    # Assert

    assert len(menu_repository.menu_itens) == 1
    assert resultNOK == False
    assert resultOK == True
    