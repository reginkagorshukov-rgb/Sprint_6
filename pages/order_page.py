from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
import time
from ..locators.cookie_locators import Cookie
from ..locators.order_locators import Order

class Order:
    TOP_ORDER_BUTTON = Order.TOP_ORDER_BUTTON
    BOTTOM_ORDER_BUTTON = Order.BOTTOM_ORDER_BUTTON
    COOKIE = Cookie.COOKIE
    NAME_INPUT = Order.NAME_INPUT
    SURNAME_INPUT = Order.SURNAME_INPUT
    ADDRESS_INPUT = Order.ADDRESS_INPUT
    METRO_INPUT = Order.METRO_INPUT
    TELEPHON_INPUT = Order.TELEPHON_INPUT
    NEXT_BUTTON = Order.NEXT_BUTTON
    DROPDOWN_METRO = Order.DROPDOWN_METRO
    DELIVERY_DATE = Order.DELIVERY_DATE
    RENTAL_PERIOD = Order.RENTAL_PERIOD
    DROPDOWN_RENTAL_PERIOD = Order.DROPDOWN_RENTAL_PERIOD
    COMMENT_INPUT = Order.COMMENT_INPUT
    FORMA_ORDER_BUTTON = Order.FORMA_ORDER_BUTTON
    YES_BUTTON = Order.YES_BUTTON
    ORDER_DECORATED = Order.ORDER_DECORATED
    STATUS_BUTTON = Order.STATUS_BUTTON
    SCOOTER_LOGO = Order.SCOOTER_LOGO
    YANDEX_LOGO = Order.YANDEX_LOGO


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Принять куки")
    def click_cookie(self):
        self.driver.find_element(*self.COOKIE).click()

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_order_top(self):
        self.driver.find_element(*self.TOP_ORDER_BUTTON).click()

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_bottom(self):
        self.driver.find_element(*self.BOTTOM_ORDER_BUTTON).click()

    @allure.step("Заполнить поле 'Имя'")
    def set_name(self, name):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    @allure.step("Заполнить поле 'Фамилия'")
    def set_surname(self, surname):
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)

    @allure.step("Заполнить поле 'Адрес'")
    def set_address(self, address):
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
    
    @allure.step("Заполнить поле 'Станция метро'")
    def set_metro(self, metro):
        self.driver.find_element(*self.METRO_INPUT).click()
        self.driver.find_element(*self.METRO_INPUT).send_keys(metro)
        self.driver.find_element(*self.DROPDOWN_METRO).click()

    @allure.step("Заполнить поле 'Телефон'")
    def set_telephon(self, telephon):
        self.driver.find_element(*self.TELEPHON_INPUT).send_keys(telephon)

    @allure.step("Нажать на кнопку 'Далее'")
    def click_next(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    
    def forma_order1(self, name, surname, address, metro, telephon):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_telephon(telephon)
        self.click_next()
        self.wait.until(EC.presence_of_element_located(self.DELIVERY_DATE))

    @allure.step("Заполнить поле 'Когда привезт самокат'")
    def set_delivery(self, delivery):
        self.driver.find_element(*self.DELIVERY_DATE).send_keys(delivery)
        self.driver.find_element(*self.DELIVERY_DATE).send_keys('\n')
        self.driver.find_element(By.TAG_NAME, 'body').click()

    @allure.step("Заполнить поле 'Срок аренды'")
    def set_period(self, period):
        self.driver.find_element(*self.RENTAL_PERIOD).click()
        time.sleep(0.5)
        self.driver.find_element(*period).click()

    @allure.step("Заполнить поле 'Комментарий'")
    def set_comment(self, comment):
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)
    
    @allure.step("Заполнить поле 'Цвет самоката'")
    def set_color(self, color):
        self.driver.find_element(*color).click()

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_forma(self):
        self.driver.find_element(*self.FORMA_ORDER_BUTTON).click()


    def forma_order2(self, delivery, period, color, comment):
        self.set_delivery(delivery)
        self.set_period(period)
        self.set_color(color)
        self.set_comment(comment)
        self.click_order_forma()

    @allure.step("Нажать кнопку 'Да'")
    def click_yes(self):
        self.driver.find_element(*self.YES_BUTTON).click()

    def order_decorated(self):
        return self.wait.until(EC.visibility_of_element_located(self.ORDER_DECORATED)).is_displayed()
    def order_decorated1(self):
        return self.wait.until(EC.visibility_of_element_located(self.ORDER_DECORATED)) is not None
 
    def click_status(self):
        self.driver.find_element(*self.STATUS_BUTTON).click()
    
    @allure.step("Нажать логип самокат")
    def click_scooter(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()
    @allure.step("Нажать логип яндекс")
    def click_yandex(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()