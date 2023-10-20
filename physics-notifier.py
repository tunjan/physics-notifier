
import schedule
import random
from plyer import notification

# Data Management
try:
    with open('physics_facts.txt', 'r') as f:
        physics_facts = f.readlines()
except FileNotFoundError:
    print("File not found. Exiting.")
    exit()

# Notification Function
def send_notification(fact):
    try:
        notification.notify(
            title='Interesting Physics Fact',
            message=fact,
            app_name='PhysicsFacts',
            timeout=60,
            app_icon='icon_path.ico'
        )
    except Exception as e:
        print(f"An error occurred: {e}")

# Randomization Logic
last_fact = ""

def job():
    global last_fact
    fact = random.choice(physics_facts)
    while fact == last_fact:
        fact = random.choice(physics_facts)
    last_fact = fact
    send_notification(fact)

# Scheduling
schedule.every(3).seconds.do(job)

# Main Loop
while True:
    schedule.run_pending()

