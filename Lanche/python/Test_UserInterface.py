from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order


def test_get_user_input():
    result = "2 5".split(" ")

    assert result[0].isnumeric() == True
    assert result[1].isnumeric() == True


def test_get_total_price():
    menu_repository = MenuRepository()
    lanche = Menu(2, "X-zr75",4.50)
    menu_repository.set_menu_item(lanche)

    order = Order(2, 4)
    assert (order.quantity * lanche.price) == 18
    

def test_get_total_price2():

    lanche = Menu(4, "risole", 2.00)
    order = Order(4, 5)

    assert (order.quantity * lanche.price) == 10    