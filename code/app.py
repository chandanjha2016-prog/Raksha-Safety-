
# RAKSHA SAFETY - MVP CODE
import datetime

# 1. YE LIST HAI USERS KI
users = [
    {"name": "Raju", "sleep_time": "11 PM", "wake_time": "5 AM"},
    {"name": "Amit", "sleep_time": "10 PM", "wake_time": "6 AM"}
]

# 2. YE FUNCTION HAI ALARM BHEJNE KA
def send_good_morning(user):
    print(f"Good Morning {user['name']}! Uth jao. Aaj ka time: {user['wake_time']}")

# 3. YE CHALAO TO SABKO MSG JAYEGA
print("--- RAKSHA SAFETY STARTED ---")
for user in users:
    send_good_morning(user)
