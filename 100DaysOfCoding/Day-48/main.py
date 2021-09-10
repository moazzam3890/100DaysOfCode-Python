from selenium import webdriver


chrome_driver_path = "/snap/bin/chromium.chromedriver"
upcoming_events = {}
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")
dates_and_times = driver.find_elements_by_css_selector(".shrubbery .menu li time")
links_texts = driver.find_elements_by_css_selector(".event-widget .shrubbery .menu li a")

for number in range(5):
    dictionary = {
            "time": dates_and_times[number].text,
            "name": links_texts[number].text
        }
    upcoming_events[number] = dictionary
print(upcoming_events)

driver.quit()
