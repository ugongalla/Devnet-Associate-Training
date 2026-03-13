from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

def connect_to_device(host, username, password):
    """Connect to a Cisco device."""
    if not all([host, username, password]):
        raise ValueError("host, username, and password are required")
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password,
    }
    try:
        connection = ConnectHandler(**device)
        return connection
    except NetmikoAuthenticationException:
        print("Authentication failed. Check credentials.")
        raise
    except NetmikoTimeoutException:
        print("Connection timeout. Check host availability.")
        raise

def get_device_info(connection):
    """Retrieve device information."""
    try:
        output = connection.send_command('show version')
        return output
    except Exception as e:
        print(f"Error occurred while retrieving device info: {e}")
        raise
    

def main():
    """Main execution."""
    try:
        conn = connect_to_device('192.168.1.1', 'admin', 'password')
        info = get_device_info(conn)
        print(info)
        print("Device information retrieved successfully.")
        conn.disconnect()
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()