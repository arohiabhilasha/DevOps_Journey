import os
import json
import sys

# Check if config.json exists before trying to open it
config_file = 'DevOps_Journey/config.json'
db_pass = os.getenv("DB_PASSWORD")
print(f"The secret password is: {db_pass}")

if os.path.exists(config_file):
    try:
        # Open and parse the JSON file
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        print(f"Connecting to {config.get('db_host')} on port {config.get('db_port')}...")
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in {config_file}")
        print(f"Details: {e}")
    except Exception as e:
        print(f"Error: Failed to read {config_file}")
        print(f"Details: {e}")
else:
    print(f"CRITICAL ERROR: Config file missing!")
    sys.exit(1)
