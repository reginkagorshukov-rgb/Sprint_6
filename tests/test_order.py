import allure
import pytest
from ..user_data import UserData
from ..pages.order_page import Orders

@allure.feature("Заказы")
class TestOrder:
    @allure.title("Проверка верхней кнопки Заказать")
    @pytest.mark.parametrize("user_data", [UserData.USER1])
    def test_order_top(self, driver, user_data):
        order1 = Orders(driver)
        order1.click_cookie()
        order1.click_order_top()
        
        order1.forma_order1(**user_data["order1"])
        order1.forma_order2(**user_data["order2"])

        order1.click_yes()
        order1.order_decorated()
        order1.order_decorated1()
        order1.click_status()
        order1.click_scooter()
        order1.click_yandex()

    @allure.title("Проверка нижней кнопки Заказать")
    @pytest.mark.parametrize("user_data", [UserData.USER2])
    def test_order_bottom(self, driver, user_data):
        order2 = Orders(driver)
        order2.click_cookie()
        order2.click_order_bottom()

        order2.forma_order1(**user_data["order1"])
        order2.forma_order2(**user_data["order2"])

        order2.click_yes()
        order2.order_decorated()
        order2.order_decorated1()
        order2.click_status()
        order2.click_scooter()
        order2.click_yandex()
        