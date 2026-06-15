from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
import time
from ..locators.cookie_locators import Cookie
from ..locators.faq_locators import FAQ

class FaqQuestions:

    TITLE = FAQ.TITLE
    COOKIE = Cookie.COOKIE
    QUESTION_1 = FAQ.QUESTION_1
    ANSWER_1 = FAQ.ANSWER_1
    QUESTION_2 = FAQ.QUESTION_2
    ANSWER_2 = FAQ.ANSWER_2
    QUESTION_3 = FAQ.QUESTION_3
    ANSWER_3 = FAQ.ANSWER_3
    QUESTION_4 = FAQ.QUESTION_4
    ANSWER_4 = FAQ.ANSWER_4
    QUESTION_5 = FAQ.QUESTION_5
    ANSWER_5 = FAQ.ANSWER_5
    QUESTION_6 = FAQ.QUESTION_6
    ANSWER_6 = FAQ.ANSWER_6
    QUESTION_7 = FAQ.QUESTION_7
    ANSWER_7 = FAQ.ANSWER_7
    QUESTION_8 = FAQ.QUESTION_8
    ANSWER_8 = FAQ.ANSWER_8


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    
    def click_cookie(self):
        self.driver.find_element(*self.COOKIE).click()

    def scroll_to_element(self, element_locator):
        element = self.wait.until(EC.visibility_of_element_located(element_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)

    def _click_question(self, question_locator, answer_locator):
        self.scroll_to_element(question_locator)
        question = self.wait.until(EC.element_to_be_clickable(question_locator))
        question.click()
        self.wait.until(EC.visibility_of_element_located(answer_locator))
        time.sleep(0.3)

    def get_answer_text(self, answer_locator):
        element = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return element.text

    @allure.step("Раскрытие первого вопроса")
    def click_questions1_in_button(self):
        self._click_question(self.QUESTION_1, self.ANSWER_1)

    def answer1(self):
        return self.get_answer_text(self.ANSWER_1)
    @allure.step("Раскрытие второго вопроса")
    def click_questions2_in_button(self):
        self._click_question(self.QUESTION_2, self.ANSWER_2)

    def answer2(self):
        return self.get_answer_text(self.ANSWER_2)
    
    @allure.step("Раскрытие третьяго вопроса")
    def click_questions3_in_button(self):
        self._click_question(self.QUESTION_3, self.ANSWER_3)

    def answer3(self):
        return self.get_answer_text(self.ANSWER_3)
    
    @allure.step("Раскрытие четвертого вопроса")
    def click_questions4_in_button(self):
        self._click_question(self.QUESTION_4, self.ANSWER_4)

    def answer4(self):
        return self.get_answer_text(self.ANSWER_4)
    
    @allure.step("Раскрытие пятого вопроса")
    def click_questions5_in_button(self):
        self._click_question(self.QUESTION_5, self.ANSWER_5)

    def answer5(self):
        return self.get_answer_text(self.ANSWER_5)
    @allure.step("Раскрытие шестого вопроса")
    def click_questions6_in_button(self):
        self._click_question(self.QUESTION_6, self.ANSWER_6)

    def answer6(self):
        return self.get_answer_text(self.ANSWER_6)
    @allure.step("Раскрытие седьмого вопроса")
    def click_questions7_in_button(self):
        self._click_question(self.QUESTION_7, self.ANSWER_7)

    def answer7(self):
        return self.get_answer_text(self.ANSWER_7)
    @allure.step("Раскрытие восьмого вопроса")
    def click_questions8_in_button(self):
        self._click_question(self.QUESTION_8, self.ANSWER_8)

    def answer8(self):
        return self.get_answer_text(self.ANSWER_8)