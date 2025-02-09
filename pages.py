import time
from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    ADDRESS_FROM_LOCATOR = (By.ID, 'from')
    ADDRESS_TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_LOCATOR = (By.XPATH, "//button[@class='button round']")
    PHONE_NUMBER_LOCATOR = (By.CLASS_NAME, 'number-picker')
    CARD_NUMBER_LOCATOR = (By.CLASS_NAME, 'number-picker')
    CARD_CODE_LOCATOR = (By.CLASS_NAME, 'number-picker')
    MESSAGE_FOR_DRIVER = (By.XPATH, "//button[@class='button round']")
    CLICK_CALL_TAXI_BUTTON = (By.XPATH, "//button[@class='button round']")
    CLICK_TAXI_OPTION = (By.XPATH, "//button[@class='button round']")
    CLICK_SUPPORTIVE_OPTION = (By.XPATH, "//button[@class='button round']")

    def __init__(selfself, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_LOCATOR).click()

    def enter_phone_number(self, phone_number_text):
        self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).send_keys(phone_number_text)
