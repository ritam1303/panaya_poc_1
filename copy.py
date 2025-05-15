import os
import shutil

# Define the source and destination paths
source_path = "settings.json"
destination_dir = r"C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config"
destination_path = os.path.join(destination_dir, "settings.json")

# Check if the target directory exists, create it if not
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Move the settings.json file
if os.path.exists(source_path):
    shutil.move(source_path, destination_path)
    print(f"settings.json has been moved to {destination_path}")
else:
    print(f"Error: {source_path} does not exist.")
    
source_path1="settingsTool.json"
destination_dir = r"C:\Users\ltuser.ghtestVM\AppData\Local\Agent\config"
destination_path = os.path.join(destination_dir, "settings.json")

# Check if the target directory exists, create it if not
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Move the settings.json file
if os.path.exists(source_path):
    shutil.move(source_path, destination_path)
    print(f"settings.json has been moved to {destination_path}")
else:
    print(f"Error: {source_path} does not exist.")