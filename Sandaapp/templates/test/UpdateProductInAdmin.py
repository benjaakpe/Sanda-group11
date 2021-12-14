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
        prod_price = "45.00"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin")
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[8]/th/a").click()
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[1]/div/div/div[1]/form/div[2]/table/tbody/tr["
                                      "1]/th/a").click()
        elem = driver.find_element(By.ID, "id_product_price")
        elem.send_keys(prod_price)
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[1]/div/form/div/div/input[1]").click()
        time.sleep(3)
        # assert "Logged in"
        try:
            # attempt to find the 'Logout' button - if found, logged in
            elem = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/a[3]")
            assert True
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False
        time.sleep(5)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
