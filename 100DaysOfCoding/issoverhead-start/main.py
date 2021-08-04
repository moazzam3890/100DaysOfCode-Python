import smtplib
import time
from config import iss_position, sunset_sunrise


MY_EMAIL = "pythontesting786@gmail.com"
MY_PASSWORD = "abcxyz123789"


# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if iss_position() and sunset_sunrise():
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:ISS Overhead\n\nISS is Above you."
            )





