# RAKSHA SAFETY - AI SUBAH COACH
import datetime

print("--- RAKSHA SAFETY STARTED ---")

# 1. YE HAMARA NAKLI DATABASE HAI. ASLI ME YE GOOGLE SHEET SE AAYEGA
users = {
    "6201234567": {"name": "Chandan", "wake_time": "6:00 AM", "status": "Late Uthta hai"},
    "6209876543": {"name": "Rahul", "wake_time": "5:30 AM", "status": "Time par uth jata hai"}
}

# 2. YE FUNCTION MOBILE NO CHECK KAREGA
def send_morning_alert(mobile_no):
    today = datetime.date.today()
    
    if mobile_no in users:
        user = users[mobile_no]
        message = f"Good Morning {user['name']}! ⏰\nAaj ka target: {user['wake_time']} par uthna hai.\nNote: {user['status']}\n\n- Raksha Safety AI"
        print(f"📱 {mobile_no} ko WhatsApp bheja gaya:")
        print(message)
        print(f"Date: {today}\n")
    else:
        print(f"📱 {mobile_no} - Ye number database me nahi hai. Pehle Google Form bharwao.")

# 3. TEST KARO - APNA NO YAHAN DAALO
print("Test 1: Apna No")
send_morning_alert("7739285002")

print("Test 2: Dusra No")
send_morning_alert("9031721575")

print("Test 3: Naya No")
send_morning_alert("6201167980")
