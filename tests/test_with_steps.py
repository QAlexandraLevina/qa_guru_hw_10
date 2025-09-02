import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открытие главной страницы GitHub"):
        browser.open("https://github.com")

    with allure.step("Поиск репозитория"):
        s(".search-input").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переход в репозиторий"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Переход во вкладку 'Actions'"):
        s("#actions-tab").click()

    with allure.step("Проверка наличия 'Actions' под номером '281'"):
        s(by.partial_text("#281")).should(be.visible)
