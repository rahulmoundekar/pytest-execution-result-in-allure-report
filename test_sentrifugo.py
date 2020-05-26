import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import time

baseURL = "http://demo.sentrifugo.com/"


@allure.severity(allure.severity_level.NORMAL)
class TestSentrifugoHrms:

    @pytest.fixture()
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="E:/OnlyForPython/SELENIUM/drivers/chromedriver_win32/chromedriver.exe")
        self.driver.get(baseURL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @allure.severity(allure.severity_level.MINOR)
    def test_homeTitle(self, setUp):
        if self.driver.title == "Sentrifugo - Open Source":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testTitleScreen",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self, setUp):
        self.driver.find_element_by_id("username").send_keys("em01")
        self.driver.find_element_by_id("password").send_keys("sentrifugo")
        self.driver.find_element_by_id("loginsubmit").click()
        time.sleep(5)
        self.driver.find_element_by_id("logoutbutton").click()
        self.driver.find_element_by_link_text("Logout").click()

    @allure.severity(allure.severity_level.BLOCKER)
    def test_dashboard(self):
        pytest.skip("we will define later")
