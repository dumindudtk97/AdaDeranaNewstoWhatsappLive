from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import test 
from test import send_msg
from test import scrape

def job_function():
    print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(scrape, 'interval', minutes=5)

sched.start()

