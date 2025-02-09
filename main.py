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
    urban_routes_page = UrbanRoutesPage(self.driver)
    urban_routes_page.enter_from_location(data.ADDRESS_FROM)
    urban_routes_page.enter_to_location(data.ADDRESS_TO)
    urban_routes_page.click_call_a_taxi_button()
    actual_value = urban_routes_page.check_taxi_selector()
    expected_value = 'Call a taxi'
    assert actual_value == expected_value

def test_select_plan(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    urban_routes_page = UrbanRoutesPage(self.driver)
    urban_routes_page.enter_from_location(data.ADDRESS_FROM)
    urban_routes_page.enter_to_location(data.ADDRESS_TO)
    urban_routes_page.click_custom_option()
    urban_routes_page.click_taxi_option()
    urban_routes_page.click_call_taxi_button()
    urban_routes_page.click_supportive_option()
    time.sleep(2)
    assert urban_routes_page.get_supportive_option()


def test_fill_phone_number(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    urban_routes_page = UrbanRoutesPage(self.driver)
    urban_routes_page.enter_from_location(data.ADDRESS_FROM)
    urban_routes_page.enter_to_location(data.ADDRESS_TO)
    urban_routes_page.click_custom_option()
    urban_routes_page.click_taxi_option()
    urban_routes_page.click_call_taxi_button()
    urban_routes_page.click_supportive_option()
    time.sleep(2)
    assert urban_routes_page.get_supportive_option()

def test_fill_card(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    urban_routes_page = UrbanRoutesPage(self.driver)
    urban_routes_page.enter_from_location(data.ADDRESS_FROM)
    urban_routes_page.enter_to_location(data.ADDRESS_TO)
    urban_routes_page.click_custom_option()
    urban_routes_page.click_taxi_option()
    urban_routes_page.click_call_taxi_button()
    urban_routes_page.click_supportive_option()
    time.sleep(2)
    assert urban_routes_page.get_supportive_option()

def test_comment_for_driver(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    urban_routes_page = UrbanRoutesPage(self.driver)
    urban_routes_page.enter_from_location(data.ADDRESS_FROM)
    urban_routes_page.enter_to_location(data.ADDRESS_TO)
    urban_routes_page.click_custom_option()
    urban_routes_page.click_taxi_option()
    urban_routes_page.click_call_taxi_button()
    urban_routes_page.click_supportive_option()
    time.sleep(2)
    assert urban_routes_page.get_supportive_option()

def test_order_blanket_and_handkerchiefs(self):
    self.driver.get(data.URBAN_ROUTES_URL)
    urban_routes_page = UrbanRoutesPage(self.driver)
    urban_routes_page.enter_from_location(data.ADDRESS_FROM)
    urban_routes_page.enter_to_location(data.ADDRESS_TO)
    urban_routes_page.click_custom_option()
    urban_routes_page.click_taxi_option()
    urban_routes_page.click_call_taxi_button()
    urban_routes_page.click_supportive_option()
    time.sleep(2)
    assert urban_routes_page.get_supportive_option()


def test_order_2_ice_creams(self):
    number_of_ice_cream = 2
    for ice_cream in range(2):
    self.driver.get(data.URBAN_ROUTES_URL)
    urban_routes_page = UrbanRoutesPage(self.driver)
    urban_routes_page.enter_from_location(data.ADDRESS_FROM)
    urban_routes_page.enter_to_location(data.ADDRESS_TO)
    urban_routes_page.click_custom_option()
    urban_routes_page.click_taxi_option()
    urban_routes_page.click_call_taxi_button()
    urban_routes_page.click_supportive_option()
    time.sleep(2)
    assert urban_routes_page.get_supportive_option()


@classmethod
def teardown_class(cls):
    cls.driver.quit()
