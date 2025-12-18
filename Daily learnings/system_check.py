import datetime
import shutil
import os

def main():
    print("Hello Future Architect!")

    # Show current date and time
    now = datetime.datetime.now()
    print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

    # Get disk usage statistics for root directory
    total, used, free = shutil.disk_usage("/")

    # Convert bytes to GB for readability
    free_gb = free / (1024 ** 3)
    print(f"Free disk space on your Mac: {free_gb:.2f} GB")

if __name__ == "__main__":
    main()
