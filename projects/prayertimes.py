import tkinter as tk
from tkinter import ttk, messagebox
import requests
from datetime import datetime

def fetch_prayer_times():
    latitude = "40.7128"  # NYC latitude
    longitude = "-74.0060"  # NYC longitude
    year = datetime.now().year
    month = datetime.now().month
    method = "2"  # Islamic Society of North America

    # Make API request
    api_url = f"http://api.aladhan.com/v1/calendar/{year}/{month}"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "method": method
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        prayer_times = data['data'][0]['timings']
        # Filter only the five daily prayer times
        daily_prayer_times = {prayer: time for prayer, time in prayer_times.items() if prayer in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']}
        display_prayer_times(daily_prayer_times)
    else:
        messagebox.showerror("Error", "Failed to fetch prayer times. Please check your input and try again.")

def convert_to_regular_time(time):
    # Remove any additional information like (EDT)
    time = time.split('(')[0].strip()
    # Split the time into hours and minutes
    hours, minutes = map(int, time.split(':'))
    # Convert 24-hour format to 12-hour format
    if hours >= 12:
        meridian = 'PM'
        if hours > 12:
            hours -= 12
    else:
        meridian = 'AM'
        if hours == 0:
            hours = 12
    # Format the time in regular format
    regular_time = f"{hours:02d}:{minutes:02d} {meridian}"
    return regular_time

def display_prayer_times(prayer_times):
    prayer_times_str = "\n".join([f"{prayer}: {convert_to_regular_time(time)}" for prayer, time in prayer_times.items()])
    
    # Custom message box
    custom_box = tk.Toplevel()
    custom_box.title("Prayer Times")
    custom_box.geometry("300x150")

    label = tk.Label(custom_box, text=prayer_times_str, font=('Helvetica', 12), anchor="w", justify="left")
    label.pack(expand=True, fill="both", padx=20, pady=20)

# Create the main window
root = tk.Tk()
root.title("Muslim Prayer Times")

# Style for the button
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), foreground='#ffffff', background='#007bff', padding=10)

# Create a button to fetch and display prayer times
fetch_button = ttk.Button(root, text="Fetch Prayer Times", command=fetch_prayer_times)
fetch_button.pack(pady=20)

# Run the application
root.mainloop()
