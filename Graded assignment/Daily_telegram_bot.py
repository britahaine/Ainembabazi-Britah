import requests
import schedule
import time
import datetime

# actual Telegram bot token and my chat ID.
BOT_TOKEN = '7735491223:AAEnynwGXw10VlNGc_fe7gpvz4wRnNK9e_U'  # my bot token
CHAT_ID = '7994918859'  #my actual chat ID


#  Function to return a motivational message based on the day of the week
def get_daily_message():
    
    day = datetime.datetime.today().strftime('%A')# Gets the current day, e.g. "Monday"
    
# Dictionary of motivational messages for each day of the week
    messages = {
        "Monday": "🌅 Happy Monday! Time to crush a new week!",
        "Tuesday": "💡 It's Tuesday! Stay focused and keep building.",
        "Wednesday": "🐫 Midweek check-in! You're doing great.",
        "Thursday": "🚀 Almost Friday! Keep the momentum going.",
        "Friday": "🎉 Happy Friday! Finish strong!",
        "Saturday": "☀️ Saturday vibes! Relax or learn something new.",
        "Sunday": "😌 Sunday rest. Recharge for the week ahead!"
    }

    return messages.get(day, f" Today is {day}. Stay consistent and keep growing!")#Return the message for today or a default if something goes wrong


#  Function to send a message to your Telegram chat using Telegram Bot API
def send_telegram_message(message):
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage" # Telegram API endpoint
    payload = {"chat_id": CHAT_ID, "text": message}
    
    response = requests.post(url, data=payload)# Send the POST request to Telegram

 # Check response status
    if response.status_code == 200:
        print(f"✅ Message sent: {message}")
    else:
        print(f"❌ Failed to send: {response.text}")
        
#  Main scheduled job: Generates the message and sends it
def daily_job():

    message = get_daily_message()# Get today's message
    send_telegram_message(message)# Send the message via Telegram

# Schedule the job to run every day at 9:00 AM 
schedule.every().day.at("09:00").do(daily_job) 

print("🤖 Daily Telegram bot is running. Waiting for the scheduled time...")# Initial message printed when the bot starts

 
# 🔁 Infinite loop: Continuously checks for scheduled tasks and runs them
while True:
    schedule.run_pending()# Executes jobs that are due
    time.sleep(1)
