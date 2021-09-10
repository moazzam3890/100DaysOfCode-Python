from selenium import webdriver

chrome_driver_path = "/snap/bin/chromium.chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
number = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(number.text)
driver.quit()
