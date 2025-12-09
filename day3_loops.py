# Python Lists and For Loops

# A Python list is a way to store multiple values in a single variable. Lists are ordered, changeable, and allow duplicate values.
# For example, you might keep a list of server names or HTTP status codes:
status_codes = [200, 200, 500, 200, 404]
target_error_code = 500

# To perform actions for each item in a list, you use a 'for loop'.
# The syntax is:
# for item in list:
#     # do something with item

# Let's use a for loop to process our list of server status codes.
for code in status_codes:
    if code == 200:
        print("Server OK")
    elif code == 500: 
        print("CRITICAL ERROR: Restarting")
        break;
    elif code == 404:
        print("Page Not Found")
