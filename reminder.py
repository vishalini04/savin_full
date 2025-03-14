import sqlite3
import datetime
import time
import threading
from speakListen import speak, hear

# Initialize the database
def init_db():
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reminders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        task TEXT,
                        date TEXT,
                        time TEXT)''')
    conn.commit()
    conn.close()

# Add a reminder
def add_reminder(task, date, time):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reminders (task, date, time) VALUES (?, ?, ?)", (task, date, time))
    conn.commit()
    conn.close()
    speak(f"Reminder set for {task} on {date} at {time}.")

# Fetch reminders
def get_reminders(date=None):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    
    if date:
        cursor.execute("SELECT id, task, time FROM reminders WHERE date = ?", (date,))
    else:
        cursor.execute("SELECT id, task, date, time FROM reminders")
    
    reminders = cursor.fetchall()
    conn.close()
    return reminders

# Check reminders for today
def check_today_reminders():
    today = datetime.date.today().strftime("%Y-%m-%d")
    reminders = get_reminders(today)
    
    if reminders:
        speak("You have the following reminders for today:")
        for reminder in reminders:
            speak(f"{reminder[1]} at {reminder[2]}.")
    else:
        speak("You have no reminders for today.")

# Edit a reminder
def edit_reminder(reminder_id, new_task=None, new_date=None, new_time=None):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    
    if new_task:
        cursor.execute("UPDATE reminders SET task = ? WHERE id = ?", (new_task, reminder_id))
    if new_date:
        cursor.execute("UPDATE reminders SET date = ? WHERE id = ?", (new_date, reminder_id))
    if new_time:
        cursor.execute("UPDATE reminders SET time = ? WHERE id = ?", (new_time, reminder_id))
    
    conn.commit()
    conn.close()
    speak("Reminder updated successfully.")

# Delete a reminder
def delete_reminder(reminder_id):
    conn = sqlite3.connect("reminders.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
    conn.commit()
    conn.close()
    speak("Reminder deleted successfully.")

# Function to handle user input and set reminders
def set_reminder_voice():
    speak("What would you like to be reminded about?")
    task = hear()
    speak("On what date? Say the date in YYYY-MM-DD format.")
    date = hear()
    speak("At what time? Say the time in HH:MM format.")
    time = hear()
    
    add_reminder(task, date, time)

# Automatic reminder alerts
def reminder_alerts():
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        conn = sqlite3.connect("reminders.db")
        cursor = conn.cursor()
        cursor.execute("SELECT task FROM reminders WHERE date || ' ' || time = ?", (now,))
        reminders = cursor.fetchall()
        conn.close()
        
        for reminder in reminders:
            speak(f"Reminder alert: {reminder[0]}")
        
        time.sleep(60)  # Check every minute

# Initialize database on first run
init_db()

# Start reminder alerts in a separate thread
reminder_thread = threading.Thread(target=reminder_alerts, daemon=True)
reminder_thread.start()

# Uncomment below to test the reminder system
# set_reminder_voice()
# check_today_reminders()
# edit_reminder(reminder_id, new_task, new_date, new_time)
# delete_reminder(reminder_id)
