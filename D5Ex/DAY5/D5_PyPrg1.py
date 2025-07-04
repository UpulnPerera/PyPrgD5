import ipaddress
ip_addr_list =["192.168.2.25","350.200.1.80"]
valid_list = []
invalid_list = []

def validate_ip_address(ip_string):
    """
    Validates an IP address string using the ipaddress module.

    Args:
        ip_string (str): The IP address string to validate.

    Returns:
        tuple: A tuple containing (True, ip_object) if valid,
               or (False, error_message) if invalid.
    """
    try:
        ip_object = ipaddress.ip_address(ip_string)
        return True, ip_object
        print({ip_object})
    except ValueError as e:
        return False, str(e)

# --- Examples ---
    
for addr in ip_addr_list:
    is_valid, result = validate_ip_address(addr)
    if is_valid:
        valid_list.append(addr)
    #print(f"'{ip1}' is a valid IP address. Version: {result.version}")
    else:
        invalid_list.append(addr)
    #print(f"'{ip1}' is not a valid IP address. Error: {result}")


# Valid IPv4 address
ip1 = "192.168.1.1"
is_valid, result = validate_ip_address(ip1)
if is_valid:
    #print(f"'{ip1}' is a valid IP address. Version: {result.version}")
else:
    print(f"'{ip1}' is not a valid IP address. Error: {result}")

# Valid IPv6 address
ip2 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
is_valid, result = validate_ip_address(ip2)
if is_valid:
    print(f"'{ip2}' is a valid IP address. Version: {result.version}")
else:
    print(f"'{ip2}' is not a valid IP address. Error: {result}")

# Shortened valid IPv6 address
ip3 = "::1" # Loopback address
is_valid, result = validate_ip_address(ip3)
if is_valid:
    print(f"'{ip3}' is a valid IP address. Version: {result.version}")
else:
    print(f"'{ip3}' is not a valid IP address. Error: {result}")

# Invalid IPv4 address (octet out of range)
ip4 = "256.0.0.1"
is_valid, result = validate_ip_address(ip4)
if is_valid:
    print(f"'{ip4}' is a valid IP address. Version: {result.version}")
else:
    print(f"'{ip4}' is not a valid IP address. Error: {result}")

# Invalid IP address (malformed)
ip5 = "not an ip"
is_valid, result = validate_ip_address(ip5)
if is_valid:
    print(f"'{ip5}' is a valid IP address. Version: {result.version}")
else:
    print(f"'{ip5}' is not a valid IP address. Error: {result}")

# IPv4 with leading zeros (not tolerated by default in strict mode)
ip6 = "192.168.0.01"
is_valid, result = validate_ip_address(ip6)
if is_valid:
    print(f"'{ip6}' is a valid IP address. Version: {result.version}")
else:
    print(f"'{ip6}' is not a valid IP address. Error: {result}")

# Valid IPv4 with network prefix (it will be treated as an interface, not just an address)
ip7 = "192.168.1.1/24"
try:
    ip_interface_object = ipaddress.ip_interface(ip7)
    print(f"'{ip7}' is a valid IP interface. Address: {ip_interface_object.ip}, Network: {ip_interface_object.network}")
except ValueError as e:
    print(f"'{ip7}' is not a valid IP address or interface. Error: {e}")