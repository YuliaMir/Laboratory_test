from pages.MainPage import MainPage
from pages.InboxPage import InboxPage


def test_send_email(driver):
    main_page = MainPage(driver, True)
    main_page.open_login_popup()
    main_page.enter_credentials()

    inbox_page = InboxPage(driver)
    inbox_page.create_new_email()
    inbox_page.send_email()

