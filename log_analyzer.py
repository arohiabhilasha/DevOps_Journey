# Sure! Here is the algorithm you can follow to analyze the log file:
#
# 1. Define a function called analyze_logs that takes a filename as its argument.
# 2. Create a dictionary (e.g., log_counts) with keys for 'INFO', 'WARN', and 'ERROR', all set to 0.
# 3. Open the log file for reading.
# 4. Loop through each line in the file:
#     a. For each line, check if it contains 'INFO', 'WARN', or 'ERROR'.
#     b. When you find one, increment the respective value in the dictionary.
# 5. After processing all the lines, print a summary report using your dictionary.
#
# Example dictionary usage:
#     log_counts = {'INFO': 0, 'WARN': 0, 'ERROR': 0}
#
# This approach lets you easily keep track of each type of message and print out neat statistics at the end!

def analyze_logs(filename: str):
    logs_count = {
        'INFO': 0,
        'WARN': 0,
        'ERROR': 0
    }

    error_list = []

    with open(filename, 'r') as file:
        for line in file:
            if 'INFO' in line:
                logs_count['INFO'] += 1
            elif 'WARN' in line:
                logs_count['WARN'] += 1
            elif 'ERROR' in line:
                logs_count['ERROR'] += 1
                # Extract error message after [ERROR]
                if ']' in line:
                    error_text = line.split(']')[1].strip()
                    error_list.append(error_text)

    print(f"Log analysis complete. Summary:")
    print(f"INFO: {logs_count['INFO']}")
    print(f"WARN: {logs_count['WARN']}")
    print(f"ERROR: {logs_count['ERROR']}")
    
    return error_list

error_list = analyze_logs('DevOps_Journey/server.log')
print(f"\nList of error messages:")
for error in error_list:
    print(f"- {error}")


