from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException I
import datetime as dt


class InternetSpeedTwitterBot:
    def __init__(self, chrome_path):
        self.driver = webdriver.Chrome(chrome_path)
        self.up = 0
        self.down = 0
        self.time = self.time_now()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        test_speed = self.driver.find_element_by_css_selector(".start-button a")
        test_speed.click()
        time.sleep(50)
        try:
            self.down = float(self.driver.find_element_by_css_selector(".result-item .result-data .download-speed").text)
            self.up = float(self.driver.find_element_by_css_selector(".result-item .result-data .upload-speed").text)
        except NoSuchElementException:
            print("Speed Not Found")

    def tweet_at_provider(self, email, password):
        self.driver.get("https://twitter.com/")
        try:
            time.sleep(2)
            sign_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span')
            sign_in.click()
            time.sleep(2)
            login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a')
            login.click()
            time.sleep(1)
        except NoSuchElementException:
            print("Page Changed.")
        time.sleep(8)
        username = self.driver.find_element_by_name("session[username_or_email]")
        username.send_keys(email)
        passwords = self.driver.find_element_by_name("session[password]")
        passwords.send_keys(password)
        login_in_2 = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        login_in_2.click()
        time.sleep(4)
        content = self.driver.find_element_by_css_selector(".DraftEditor-root .DraftEditor-editorContainer .public-DraftStyleDefault-block")
        content.send_keys(f"Hey Internet Provider, Why is my internet Speed is {self.down}down/{self.up}up when I pay for 150down/10up?\n{self.time}")
        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()

    def time_now(self):
        now = dt.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M")
