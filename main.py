import time
from selenium import webdriver
import data
import helpers
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
def setup_class(cls):
    from selenium.webdriver import DesiredCapabilities
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
    cls.driver = webdriver.Chrome()
    if helpers.is_url_reachable(data.URBAN_ROUTES_URL)
        print("Connected to the Urban Routes server")
    else:
        print("Cannot connect to Urban Routes. Check the server is on and still running")
def test_set_route(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.set_route()
    == "label"

def test_select_plan(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
    routes_page.select_plan(data.SELECT_PLAN,)
        assert routes_page.select_plan()
    == "label"


def test_fill_phone_number(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
    routes_page.fill_phone_number(data.fill_phone_number)
        assert routes_page.fill_phone_number()
    == "label"

def test_fill_card(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    self.driver.get(data.URBAN_ROUTES_URL)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
    routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.fill_card()
    == "label"

def test_comment_for_driver(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
    routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
    routes_page.enter_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_message()
    == "label"

def test_order_blanket_and_handkerchiefs(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
    routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
    routes_page.enter_message_for_driver(data.MESSAGE_FOR_DRIVER)
    routes_page.order_blanket_and_handkerchiefs(data.ORDER_BLANKET_AND_HANDKERCHIEFS)
        assert routes_page.order_blanket_and_handkerchiefs()


def test_order_2_ice_creams(self):
    number_of_ice_cream = 2
    for ice_cream in range(2):
    self.driver.get(data.URBAN_ROUTES_URL)
    routes_page = UrbanRoutesPage(self.driver)
    routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
    routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
    routes_page.order_2_ice_creams(data.ORDER_2_ICE_CREAMS)
    time.sleep(2)
    assert routes_page.order_2_ice_creams()


@classmethod
def teardown_class(cls):
    cls.driver.quit()
