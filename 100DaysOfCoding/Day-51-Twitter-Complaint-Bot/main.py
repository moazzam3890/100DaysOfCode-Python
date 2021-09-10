from internet_speed_bot import InternetSpeedTwitterBot
import time

PROMISED_DOWN = 150.0
PROMISED_UP = 10.0
CHROME_PATH_URL = "/snap/bin/chromium.chromedriver"
TWITTER_EMAIL = "Your Twitter Email"
TWITTER_PASSWORD = "Your Twitter Password"

bot = InternetSpeedTwitterBot(CHROME_PATH_URL)

bot.get_internet_speed()
time.sleep(1)
if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)

