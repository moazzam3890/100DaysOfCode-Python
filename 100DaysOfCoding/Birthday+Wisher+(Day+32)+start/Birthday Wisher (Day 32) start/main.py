# import smtplib
#
# my_yahoo_email = "pythontesting786@yahoo.com"
# my_yahoo_password = "spuyicudqgavusft"
# my_gmail_email = "pythontesting786@gmail.com"
# my_gmail_password = "abcxyz123789"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_yahoo_email, password=my_yahoo_password)
#     connection.sendmail(from_addr=my_yahoo_email,
#                         to_addrs=my_gmail_email,
#                         msg="Subject:Sending from Python yahoo\n\nHello,\nTea pilo.")
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_gmail_email,
#                      password=my_gmail_password)
#     connection.sendmail(from_addr=my_gmail_email,
#                         to_addrs=my_yahoo_email,
#                         msg="Subject:Sending from Python Gmail\n\nHello,\nTea Pilo.")
#


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# micro = now.microsecond
# print(micro)
#
# date_of_birth = dt.datetime(year=1990, month=8, day=3, hour=23, minute=29)
# print(date_of_birth)

import smtplib
import datetime as dt
import random


quotes = []
my_email = "pythontesting786@gmail.com"
my_password = "abcxyz123789"


now = dt.datetime.now()
weekday = now.weekday()


with open("quotes.txt") as data:
    for quote in data:
        quotes.append(quote)


random_quote = random.choice(quotes)

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="pythontesting786@yahoo.com",
                            msg=f"Subject:Motivational Quotes\n\n{random_quote}")
