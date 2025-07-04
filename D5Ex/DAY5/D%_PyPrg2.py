def is_private_ip(ip_str):
    """
    Check if a given IP address string is a private (LAN) IP address.
    """
    try:
        ip = ipaddress.ip_address(ip_str)
        ip.
        return ip.is_private_ip
    except ValueError:
        return False # Not a valid IP address
    
    def check_lan_presence():
        """
        Check if the script is running on a machine conncted to a LAN 
        by examining its local IP adresses.
        """
        local_ips = get_local_ip_addresses()
