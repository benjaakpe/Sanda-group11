import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ll_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "anguyen63"
        pwd = "Morning@123"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        driver.find_element(By.XPATH, "/html/body/nav/div/div/div/a[4]").click()
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/customer_details")
        time.sleep(3)
        # assert "Logged in"
        try:
            # attempt to find the 'Logout' button - if found, logged in
            elem = driver.find_element(By.XPATH, "/html/body/nav/form/a")
            assert True
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False
        time.sleep(5)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()