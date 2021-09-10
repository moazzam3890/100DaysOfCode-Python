from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


MY_EMAIL = "moazzamadilkhan3890@gmail.com"
MY_PASSWORD = "zafarsupari123"
MY_NUMBER = "3218322229"
CHROME_PATH = "/snap/bin/chromium.chromedriver"
WEBSITE = "https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Kar%C4%81chi%2C%20Sindh%2C%20Pakistan&locationId=&geoId=105451800&sortBy=R&f_TPR=&distance=25&f_E=2&position=1&pageNum=0"

driver = webdriver.Chrome(CHROME_PATH)
driver.get(WEBSITE)

time.sleep(4)
try:
    sing_in = driver.find_element_by_xpath('/html/body/div[3]/a[1]')
    sing_in.click()
except NoSuchElementException:
    pass

time.sleep(1)
username = driver.find_element_by_id("username")
username.send_keys(MY_EMAIL)

password = driver.find_element_by_id("password")
password.send_keys(MY_PASSWORD)

login = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login.click()

time.sleep(6)
# drop_down = driver.find_element_by_xpath('//*[@id="ember194"]')
# drop_down.click()
#
# time.sleep(2)
try:
    apply_now = driver.find_element_by_css_selector(".display-flex .jobs-s-apply .jobs-apply-button--top-card .jobs-apply-button")
    apply_now.click()
except NoSuchElementException:
    pass

time.sleep(2)
mobile_number = driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2713739251,34180051,phoneNumber~nationalNumber)"]')
mobile_number.send_keys(MY_NUMBER)

time.sleep(1)
next_button_1 = driver.find_element_by_css_selector("footer .display-flex button")
next_button_1.click()

time.sleep(1)
next_button_2 = driver.find_element_by_css_selector("footer .display-flex button:last-child")
next_button_2.click()




