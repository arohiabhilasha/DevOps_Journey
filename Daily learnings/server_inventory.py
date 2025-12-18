servers = {
    "web-01": ["192.168.1.100", "running"],
    "web-02": ["192.168.1.101", "running"],
    "web-03": ["192.168.1.102", "not running"],
    "web-04": ["192.168.1.103", "not running"],
    "web-05": ["192.168.1.104", "running"],
    "web-06": ["192.168.1.105", "running"],
    "web-07": ["192.168.1.106", "not running"],
    "web-08": ["192.168.1.107", "running"],
    "web-09": ["192.168.1.108", "running"],
    "web-10": ["192.168.1.109", "running"],
}

name = input("Enter the server name to get the status: ")
count = 0;
for server_name in servers:
    if name == server_name:
        print(f"The IP of {name} is {servers[name][0]} and the status is {servers[name][1]}");
        count = 1;
        break;
    else:
        continue;

if count == 0:
    print("Server not found");