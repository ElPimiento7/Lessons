from apscheduler.schedulers.blocking import BlockingScheduler
import pytz


def hello():
    print("Hello")


my_tz = pytz.timezone('Europe/Madrid')


scheduler = BlockingScheduler()
scheduler.add_job(hello, "interval", seconds=3)
# scheduler.add_job(hello, 'cron', year="*", month="*", day="*", hour="17", minute="30", second="00", timezone=my_tz)
scheduler.start()