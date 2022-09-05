from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_data

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_data,'interval',minutes=15)
    #scheduler.add_job(status,'interval',seconds=1)
    scheduler.start()