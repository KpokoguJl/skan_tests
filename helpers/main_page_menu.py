import allure
from selene.support import by
from selene.support.shared import browser


@allure.step('Кликаю на пункт меню "Решения"')
def menu_solutions_open():
    browser.element('#primary-menu').element(by.text('Решения')).click()
