import json
import os

# File Path
print("🔍 Searching for settings.json file...")
json_file_path = r"C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config\settings.json"

import time
import pyautogui
import pygetwindow as gw
import subprocess

# Step 1: Open the Agent application (if needed)
# subprocess.Popen(r"C:\Path\To\Agent.exe")  # Uncomment if Agent is not already running

# New Values to Update
new_values = {
    "panayaUrl": "https://emea.panaya.com/",
    "systemUid": "_4d710da2_19536b42a4f_3fab",
    "userName": "xy@lambdatest.com",
    "apiToken": "xy"
}

# Read JSON File
with open(json_file_path, 'r') as file:
    data = json.load(file)
    print("Previous JSON Data:")
    print(json.dumps(data, indent=4))

# Update JSON Values
for key, value in new_values.items():
    if key in data:
        data[key] = value

# Write Updated JSON
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("✅ JSON File Updated Successfully")

print("Updated JSON Data:")
print(json.dumps(data, indent=4))

# Restart Agent
print("Restarting Agent...")
os.system(r"type C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config\settings.json") 
exe_path = r"C:\Program Files\Panaya\Agent\Agent.exe"
args = ["--start"]

subprocess.Popen([exe_path] + args, creationflags=subprocess.DETACHED_PROCESS)

print("🔥 Panaya Agent Restarted")

