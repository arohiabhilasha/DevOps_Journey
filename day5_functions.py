def get_server_status(ip: str) -> str:
    """
    Simulates the server status check.
    Arguments:
    ip: str --> The IP address of the server
    Returns:
    str --> The status of the server
    """
    if ip=="10.0.0.1":
        return "Online"
    else:
        return "Offline"

servers = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

for server in servers:
    print(get_server_status(server))