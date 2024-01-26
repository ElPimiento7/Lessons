import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz


def meme():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://9gag.com/top")
    first_meme = driver.find_element(By.CLASS_NAME, "badge-evt")
    first_meme_url = first_meme.get_attribute("href")

    # with open("meme.txt", "w") as meme_file:
    #     meme_file.write(first_meme_url)

    token = "6984990599:AAEtH2IiB3tyymOyV_BzrSOjLao6uYOnp0o"
    chat_ids = [270756677, 362800141]

    for chat_id in chat_ids:
        data = json.dumps({
            "chat_id": chat_id,
            "text": first_meme_url
        })
        headers = {
            "Content-Type": "application/json"
        }

        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data=data, headers=headers)


my_tz = pytz.timezone('Europe/Madrid')

scheduler = BlockingScheduler()
scheduler.add_job(meme, "interval", seconds=3)
# scheduler.add_job(name, 'cron', year="*", month="*", day="*", hour="17", minute="30", second="00", timezone=my_tz)
scheduler.start()