from selenium import webdriver
import pytest


class Test_SignIn():
    @pytest.fixture()
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/theda/PycharmProjects/Framework/drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()

        yield
        driver.close()
        driver.quit()
        print("Test Completed")

        #Please follow the link to watch the video tutorial too: https://youtu.be/c0yZAT7Z1fc

    def test_GoFundMeLogin_1(self, test_setUp):
        driver.get("https://gofundme.com")
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_id("email").send_keys("codingandtestingdaily@gmail.com")
        driver.find_element_by_name("password").send_keys("abcd1234")
        driver.find_element_by_tag_name("button").click()

        x = driver.title
        print(x)
        assert x == "Sign In | GoFundMe"

    def test_GoFundMeLogin_2(self, test_setUp):
        driver.get("https://gofundme.com")
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_id("email").send_keys("codingandtestingdaily@gmail.com")
        driver.find_element_by_name("password").send_keys("abcd1234")
        driver.find_element_by_tag_name("button").click()

        x = driver.title
        print(x)
        assert x == "Sign in | GoFundMe"


    # def test_tearDown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")

