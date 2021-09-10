from selenium import webdriver
import time

# Setup of Selenium:
chrome_driver_url = "/snap/bin/chromium.chromedriver"
driver = webdriver.Chrome(chrome_driver_url)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# finding cookie:
cookie_element = driver.find_element_by_id("cookie")
# cookie_element.click()

# getting item id's:
items = driver.find_elements_by_css_selector("#store div")
items_ids = [item.get_attribute("id") for item in items]
items_ids.pop()
items_ids.reverse()
print(items_ids)

# Wait 1 secs and remove cookie popup:
time.sleep(1)
cc_banner = driver.find_element_by_css_selector("div.cc_container a")
cc_banner.click()

game_on = True
check = time.time() + 5
game_end = time.time() + (60*5)

while game_on:
    cookie_element.click()
    if time.time() > check:
        # getting prices of items:
        items_price_elements = driver.find_elements_by_css_selector("#store b")
        items_price_elements.pop()
        items_price_elements.reverse()
        items_prices = [int(element_text.text.split("-")[1].strip().replace(",", "")) for element_text in items_price_elements]
        # print(items_prices)
        try:
            # finding money we have:
            money = str(driver.find_element_by_id("money").text)
            if "," in money:
                money.replace(",", "")
            print(money)
            cookie_count = int(money)
            print(cookie_count)
        except ValueError:
            pass
        try:
            for n in range(len(items_prices)-1):
                if cookie_count > items_prices[n]:
                    buy = driver.find_element_by_id(items_ids[n])
                    # print(buy)
                    buy.click()
        except Exception:
            pass
        check += 5

    if time.time() > game_end:
        cookies_per_second = driver.find_element_by_id("cps")
        print(f"Cookies/Second: {cookies_per_second.text.split()[2]}")
        game_on = False
