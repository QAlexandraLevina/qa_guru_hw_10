from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s(".search-input").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#actions-tab").click()

    s(by.partial_text("#281")).should(be.visible)
