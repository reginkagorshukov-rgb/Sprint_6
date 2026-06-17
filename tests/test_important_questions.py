import allure
from ..pages.important_questions_page import FaqQuestions

@allure.feature("Вопросы о важном")
class TestFAQ:
    
    @allure.title("Проверка открытия первого ответа на вопрос FAQ")
    @allure.description("При клике на вопрос должен открываться соответствующий текст ответа")
   
    def test_faq_questions1(self, driver):

        faq1 = FaqQuestions(driver)
        faq1.click_cookie()
        faq1.click_questions1_in_button()
        answer1_text = faq1.answer1()
        assert answer1_text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
   
    @allure.title("Проверка открытия второго ответа на вопрос FAQ")
    def test_faq_questions2(self, driver):

        faq2 = FaqQuestions(driver)
        faq2.click_cookie()
        faq2.click_questions2_in_button()
        answer2_text = faq2.answer2()
        assert answer2_text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    
    @allure.title("Проверка открытия третьяго ответа на вопрос FAQ")
    def test_faq_questions3(self, driver):

        faq3 = FaqQuestions(driver)
        faq3.click_cookie()
        faq3.click_questions3_in_button()
        answer3_text = faq3.answer3()
        assert answer3_text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title("Проверка открытия четвертого ответа на вопрос FAQ")
    def test_faq_questions4(self, driver):

        faq4 = FaqQuestions(driver)
        faq4.click_cookie()
        faq4.click_questions4_in_button()
        answer4_text = faq4.answer4()
        assert answer4_text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title("Проверка открытия пятого ответа на вопрос FAQ")
    def test_faq_questions5(self, driver):

        faq5 = FaqQuestions(driver)
        faq5.click_cookie()
        faq5.click_questions5_in_button()
        answer5_text = faq5.answer5()
        assert answer5_text =="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    @allure.title("Проверка открытия шестого ответа на вопрос FAQ")
    def test_faq_questions6(self, driver):

        faq6 = FaqQuestions(driver)
        faq6.click_cookie()
        faq6.click_questions6_in_button()
        answer6_text = faq6.answer6()
        assert answer6_text == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    @allure.title("Проверка открытия седьмго ответа на вопрос FAQ")
    def test_faq_questions7(self, driver):

        faq7 = FaqQuestions(driver)
        faq7.click_cookie()
        faq7.click_questions7_in_button()
        answer7_text = faq7.answer7()
        assert answer7_text == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    @allure.title("Проверка открытия восьмого ответа на вопрос FAQ")
    def test_faq_questions8(self, driver):

        faq8 = FaqQuestions(driver)
        faq8.click_cookie()
        faq8.click_questions8_in_button()
        answer8_text = faq8.answer8()
        assert answer8_text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."