import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_actions_tab()
    should_see_actions_with_number("#281")


@allure.step("Открытие главной страницы GitHub")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Поиск репозитория {repo}")
def search_for_repository(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()


@allure.step("Переход в репозиторий")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Переход во вкладку 'Actions'")
def open_actions_tab():
    s("#actions-tab").click()


@allure.step("Проверка наличия 'Actions' под номером {number}")
def should_see_actions_with_number(number):
    s(by.partial_text(number)).should(be.visible)