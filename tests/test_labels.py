import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_labels_with_steps():
    allure.dynamic.tag("Web")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Действия в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может настроить автоматизацию процессов в репозитории")
    allure.dynamic.link("https://github.com", name='Testing')

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


# def test_dynamic_labels():
#     allure.dynamic.tag("web")
#     allure.dynamic.severity(Severity.CRITICAL)
#     allure.dynamic.feature("Действия в репозитории")
#     allure.dynamic.story("Неавторизованный пользователь не может настроить автоматизацию процессов в репозитории")
#     allure.dynamic.link("https://github.com", name='Testing')
#     pass


# @allure.tag("web")
# @allure.severity(Severity.CRITICAL)
# @allure.label("owner", "eroshenkoam")
# @allure.feature("Действия в репозитории")
# @allure.story("Авторизованный пользователь может настроить автоматизацию процессов в репозитории")
# @allure.link("https://github.com", name='Testing')
# def test_decorator_labels():
#     pass