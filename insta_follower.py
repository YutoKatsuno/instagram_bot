import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:

    def __init__(self):
        driver_path = "/Users/katsunoyuutou/Development/chromedriver"
        chrome_service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(3)
        input_username = self.driver.find_element(By.NAME, "username")
        input_username.send_keys(username)
        input_password = self.driver.find_element(By.NAME, "password")
        input_password.send_keys(password, Keys.ENTER)

    def get_followers(self, account):
        self.driver.get(f"https://www.instagram.com/{account}")

        time.sleep(3)
        followers_button = self.driver.find_element(By.XPATH, '')
        followers_button.click()

    def follow(self):
        pass
