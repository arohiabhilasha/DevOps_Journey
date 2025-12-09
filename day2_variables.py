# Variables in Python

# Variables allow you to store and manage data in your code, like configuration settings or state information.
# You can use different types of variables depending on the kind of data:
# - String: For text (e.g., server names)
# - Integer: For whole numbers (e.g., port numbers, counts)
# - Boolean: For true/false values (e.g., status flags)

# Here are 3 mid-level challenges to practice working with variables:

# Challenge 1:
# Given a string variable representing a fully qualified domain name (FQDN),
# write code to extract and print just the hostname (the part before the first dot).
#
# Example:
fqdn = "app01.production.example.com"
# Your code here:
hostname = fqdn.split(".")[0]
print(hostname)


# Challenge 2:
# You have two integer variables: one for the number of available ports, and one for how many are in use.
# Calculate the percentage of used ports (as an integer) and print it.
#
# Example:
available_ports = 100
used_ports = 37
# Your code here:
used_percent = (used_ports / available_ports) * 100
print(used_percent)


# Challenge 3:
# Suppose you have a boolean variable that indicates if a backup was successful,
# and another boolean for whether the server is reachable.
# Write code that prints "All good" only if both are True, otherwise print "Check server/backup".
#
# Example:
backup_successful = True
server_reachable = False
# Your code here:
if backup_successful == True and server_reachable == True:
    print("All good")
else:
    print("Check server/backup")

    # Operators in Python

    # Operators are special symbols or keywords that perform operations on variables and values.
    # Some common types of operators in Python include:
    # - Arithmetic operators: +, -, *, /, %, **, //
    #   (used for mathematical calculations)
    # - Comparison operators: ==, !=, >, <, >=, <=
    #   (used to compare two values and return a boolean)
    # - Logical operators: and, or, not
    #   (used to combine conditional statements)

    # Challenge 4:
    # Given two integer variables, a and b, print True if a is a multiple of b, otherwise print False.
    #
    # Example:
    a = 15
    b = 5
    # Your code here:
    if a % b == 0:
        print(True)
    else:
        print(False)

    # Challenge 5:
    # Given two boolean variables, logged_in and is_admin, print "Access granted" if either variable is True.
    # Otherwise, print "Access denied".
    #
    # Example:
    logged_in = False
    is_admin = True
    # Your code here:
    if logged_in == True or is_admin == True:
        print("Access granted")
    else:
        print("Access denied")


## Challenge from Google AI
#  you are writing a safety check for a deployment.
#  Create a variable cpu_usage = 85.
#  Create a variable memory_usage = 70.
#  Write a print statement that prints True only if cpu_usage is greater than 80 AND memory_usage is greater than 60.

cpu_usage = 85
memory_usage = 70
if cpu_usage > 80 and memory_usage > 60:
    print(True)
else:
    print(False)

