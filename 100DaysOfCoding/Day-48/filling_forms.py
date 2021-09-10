from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/snap/bin/chromium.chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element_by_name("fName")
l_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
f_name.send_keys("Moazzam")
l_name.send_keys("Khan")
email.send_keys("aaaa@ggg.com")
sign_up_btn = driver.find_element_by_class_name("btn")
sign_up_btn.send_keys(Keys.ENTER)
