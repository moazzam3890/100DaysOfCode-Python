import requests
from bs4 import BeautifulSoup
import smtplib


MY_EMAIL = "Your Email"
MY_PASSWORD = "Your Password"
SITE_URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

headers = {
    "Accept-Language": "en-US",
    "User-Agent": "Chrome/92.0.4515.159"
}

response = requests.get(url=SITE_URL, headers=headers).text
soup = BeautifulSoup(response, "html.parser")
price_with_dollar = soup.find(name="span", id="priceblock_ourprice").string
price = price_with_dollar.split("$")[1]


if int(float(price)) < 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=MY_PASSWORD
        )
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="Reciever Email",
            msg=f"Subject:Amazon price Alert!\n\n{soup.find(name='span', id='productTitle').string} is now available in just ${price}.\n{SITE_URL}".encode("utf-8")
        )
