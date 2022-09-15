import allure
import pytest
from selene import have, be
from selene.support import by
from selene.support.shared import browser

from helpers.main_page_menu import menu_solutions_open


# @allure.id('')
@allure.title('Проверка элементов главной страницы')
@allure.feature('Главная страница')
@allure.label('owner', 'chikov')
def test_main_page_open(browser_config):
    """
    Тест проверяет что главная страница открылась. Что на ней присутвтует логотип Интерфакс, он ведет по нужной ссылке
    и имеет корректную картинку.
    Проверяется набор элементов главного меню.
    """
    with allure.step('Проверка, что логотип компании – ссылка на https://group.interfax.ru/'):
        browser.element('.mainpage-interfax a').should(have.attribute('href')
                                                       .value('https://group.interfax.ru/'))
    with allure.step('Проверка, что логитип компании корректное изображение'):
        browser.element('.mainpage-interfax img') \
            .should(have.attribute('src')
                    .value('https://scan-interfax.ru/wp-content/themes/scan/images/interfax-logo.svg'))
    with allure.step('Проверка пунктов меню'):
        browser.element('.menu-header-container').all('li') \
            .should(have.texts('Решения', 'Обучение', 'Рейтинги', 'Блог'))
        browser.element('.header-right').element(by.text('Тестовый доступ')) \
            .should(be.visible)
        browser.element('.header-right').element(by.text('Вход')) \
            .should(be.visible)


# @allure.id('')
@allure.title('Проверка элементов меню "Решения" - Проверка котрагентов')
@allure.feature('Главная страница')
@allure.label('owner', 'chikov')
@pytest.mark.parametrize("locator, menu_text, link",
                         [('#menu-item-28', 'Мониторинг СМИ', 'https://scan-interfax.ru/media-monitoring/'),
                          ('#menu-item-27', 'Проверка контрагентов',
                           'https://scan-interfax.ru/counterparty-verification/'),
                          ('#menu-item-3267', 'Редакторский мониторинг',
                           'https://scan-interfax.ru/redactors-monitoring/'),
                          ])
def test_menu_solutions(locator, menu_text, link, browser_config):
    """
    Тест проверяет что в меню Решения есть пункт и пункт ведет по корректному урлу.
    """

    menu_solutions_open()

    with allure.step('Проверка пункта меню Мониторинг СМИ'):
        browser.element(locator).should(have.text(menu_text)).element('a') \
            .should(have.attribute('href').value(link))
