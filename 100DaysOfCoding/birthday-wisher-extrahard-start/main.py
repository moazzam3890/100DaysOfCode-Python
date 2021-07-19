import datetime as dt
import smtplib
import pandas
import random

email = "pythontesting786@gmail.com"
password = "abcxyz123789"
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

# Dictionary Comprehension:
birthday_dict = {(row_of_data["month"], row_of_data["day"]): row_of_data for (index, row_of_data)
                 in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_path) as letter:
        content = letter.read()
        replaced_content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{replaced_content}"
        )
