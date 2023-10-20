
import json
import requests
import logging
import schedule
import random
from plyer import notification

# Configuration
def read_config():
    with open("config.json", "r") as f:
        config = json.load(f)
    return config

config = read_config()
interval = config.get('interval', 15)

# Logging setup
logging.basicConfig(filename='app.log', level=logging.INFO)

# Fetching facts
def fetch_online_facts(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.splitlines()
    except:
        return None

def read_local_facts(file_path='physics_facts.txt'):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

physics_facts = fetch_online_facts("https://some-url.com/facts") or read_local_facts()

# Sending Notifications
def send_notification(fact):
    notification.notify(
        title='Interesting Physics Fact',
        message=fact,
        app_name='PhysicsFacts',
        timeout=10
    )

# Scheduling
def job():
    fact = random.choice(physics_facts)
    send_notification(fact)
    logging.info(f"Sent fact: {fact}")

schedule.every(interval).seconds.do(job)

while True:
    schedule.run_pending()
