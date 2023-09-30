import csv
import os
from datetime import datetime

def save_logs(hum, temp, hum_threshold, temp_threshold, last_fan, profile, hardware_hum):
    # Define the file path
    file_path = "logs.csv"

    # Check if the file exists, and if not, create it with the header
    file_exists = os.path.exists(file_path)
    with open(file_path, mode="a", newline='') as log_file:
        fieldnames = ["date", "time", "hum", "hum_max", "hum_min", "temp", "temp_max", "temp_min", "fan_action", "last_fan", "hardware_hum"]
        writer = csv.DictWriter(log_file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        # Determine fan_action based on hum 
        if hum > hum_threshold[1]:
            fan_action = "on"
        elif hum < hum_threshold[0]:
            fan_action = "off"
        #put down "shutdown" in case of emergency shutdown due to humidity
        elif hardware_hum > 70:
            fan_action = "shutdown"
        else:
            fan_action = "none"

        # Determine x_comment
        hum_comment = "high" if hum > hum_threshold[1] else "low" if hum < hum_threshold[0] else "normal"
        temp_comment = "high" if temp > temp_threshold[1] else "low" if temp < temp_threshold[0] else "normal"

        # Get the current date and time
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        time_str = now.strftime("%H:%M")

        # Write the log entry to the CSV file
        writer.writerow({
            "date": date_str,
            "time": time_str,
            "hum": hum,
            "hum_max": hum_threshold[1],
            "hum_min": hum_threshold[0],
            "temp": temp,
            "temp_max": temp_threshold[1],
            "temp_min": temp_threshold[0],
            "fan_action": fan_action,
            "last_fan": last_fan,
            "hardware_hum": hardware_hum
        })

# Example usage:
hum = 65.5
temp = 25.3
hum_threshold = [30, 70]  # Example threshold values
temp_threshold = [20, 30]  # Example threshold values
last_fan = 2
hardware_hum = 60.0

#save_logs(hum, temp, hum_threshold, temp_threshold, last_fan, hardware_hum)
