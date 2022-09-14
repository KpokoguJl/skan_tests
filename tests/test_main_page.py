import allure
from selene import have, be
from selene.support import by
from selene.support.shared import browser


# @allure.id('')
@allure.title('Проверка элементов главной страницы')
@allure.feature('Главная страница')
@allure.label('owner', 'chikov')
def test_main_page_open(browser_config):

    with allure.step('Проверка, что логотип компании – ссылка на https://group.interfax.ru/'):
        browser.element('.mainpage-interfax a').should(have.attribute('href')
                                                       .value('https://group.interfax.ru/'))
    with allure.step('Проверка, что логитип компании корректное изображение'):
        browser.element('.mainpage-interfax img')\
            .should(have.attribute('src')
                    .value('https://scan-interfax.ru/wp-content/themes/scan/images/interfax-logo.svg'))
    with allure.step('Проверка пунктов меню'):
        browser.element('.menu-header-container').all('li')\
            .should(have.texts('Решения', 'Обучение', 'Рейтинги', 'Блог'))
        browser.element('.header-right').element(by.text('Тестовый доступ'))\
            .should(be.visible)
        browser.element('.header-right').element(by.text('Вход')) \
            .should(be.visible)


# @allure.id('')
@allure.title('Проверка элементов меню "Решения"')
@allure.feature('Главная страница')
@allure.label('owner', 'chikov')
def test_menu_solutions(browser_config):

    with allure.step('Кликаю на пункт меню "Решения"'):
        browser.element('#primary-menu').element(by.text('Решения')).click()

    with allure.step('Проверка, что пункты меню корректные'):
        browser.element('.mainpage-interfax img')\
            .should(have.attribute('src')
                    .value('https://scan-interfax.ru/wp-content/themes/scan/images/interfax-logo.svg'))
    with allure.step('Проверка пунктов меню'):
        browser.element('.menu-header-container').all('li')\
            .should(have.texts('Решения', 'Обучение', 'Рейтинги', 'Блог'))
        browser.element('.header-right').element(by.text('Тестовый доступ'))\
            .should(be.visible)
        browser.element('.header-right').element(by.text('Вход')) \
            .should(be.visible)