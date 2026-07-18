import pandas as pd
from datetime import datetime

print("RAKSHA SAFETY - 10 USERS MVP REPORT")
print("="*50)

# STEP 1: YAHAN SIRF 10 MOBILE NO DAAL DO
users_data = [
    {"name": "Chandan", "number": "6201234567", "habit": "Late Uthta hai"},
    {"name": "seema", "number": "9876543210", "habit": "Time par sota hai"},
    {"name": "sweta", "number": "9123456780", "habit": "Exam ki tension"},
    {"name": "sucheta", "number": "9988776655", "habit": "Job interview hai"},
    {"name":  "pinky ", "number": "9012345678", "habit": "Health ka dhyan nahi"},
    {"name": "Mona", "number": "7890123456", "habit": "Subah padhai karta hai"},
    {"name": "Barsha", "number": "7654321098", "habit": "Late soti hai"},
    {"name": "Naina", "number": "6543210987", "habit": "Gym jata hai"},
    {"name": "Durga", "number": "5432109876", "habit": "Competition ki taiyari"},
    {"name": "Dolly", "number": "4321098765", "habit": "Kisan ka beta"}
]

# STEP 2: AI LOGIC - Har ek ko message bhejo
report = []
for user in users_data:
    time_now = datetime.now().strftime("%H:%M")
    message = f"Good Morning {user['name']}! ⏰\nAaj ka target: 6:00 AM par uthna hai.\nNote: {user['habit']}"
    
    print(f"\nTo: {user['number']}")
    print(f"Message: {message}")
    print("-"*30)
    
    report.append([user['name'], user['number'], user['habit'], "Message Sent", time_now])

# STEP 3: MVP REPORT CSV BAN GAYI
df = pd.DataFrame(report, columns=["Name", "Number", "Habit", "Status", "Time"])
df.to_csv("mvp_report_10_users.csv", index=False)

print("\n✅ MVP REPORT READY: mvp_report_10_users.csv")
print("✅ 10 LOGON KO MESSAGE SIMULATE HO GAYA")
