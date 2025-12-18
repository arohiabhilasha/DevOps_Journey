# Dictionaries in Python

# A dictionary in Python is a collection of "key-value pairs". Each key is unique and is used to access its corresponding value.
# This makes dictionaries ideal for representing structured data, like metadata for cloud resources.

# Example: Create a dictionary to represent an AWS EC2 instance.
ec2_instance = {
    "InstanceId": "i-1234567890abcdef0",
    "Type": "t2.micro",
    "State": "running",
    "PublicIP": "54.123.45.67"
}

# Accessing a value: 
# To get the public IP of this EC2 instance, use the key 'PublicIP':
public_ip = ec2_instance["PublicIP"]
print("EC2 Public IP:", public_ip)

# Adding a new key-value pair:
# Let's add a 'Tags' field to our dictionary
ec2_instance["Tags"] = {"Name": "WebServer", "Environment": "Production"}
print("With Tags:", ec2_instance)

# Why are dictionaries called "key-value pairs"?
# Each item in a dictionary is a pair: the 'key' (e.g., "InstanceId") and its 'value' (e.g., "i-1234567890abcdef0").
# These pairs let you quickly look up a value based on its unique key, much like looking up a word in a glossary.

# Exercise to print  asentence "My name is [Name] and I am aiming for [Target_Salary]."

myself = {
    "Name": "Abhilasha Arohi",
    "Current_Salary": "100000",
    "Target_Salary": "150000",
    "Role": "DevOps Engineer"
}

print(f"My name is {myself['Name']} and I'm a {myself['Role']} and I'm aiming for {myself['Target_Salary']}")


# Removing a value from teh dictionary
del myself["Current_Salary"]
print(f"My details: {myself}")

del_value = myself.pop("Role")
print(f"My Details now: {myself}")
print(f"Popped value: {del_value}")

myself["Goal"] = "To become a Senior DevOps Engineer"
print(f"My details now: {myself}")