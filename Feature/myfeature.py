from netmiko import ConnectHandler

def connect_to_device(host, username, password):
    """Connect to a Cisco device."""
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password,
    }
    connection = ConnectHandler(**device)
    return connection

def get_device_info(connection):
    """Retrieve device information."""
    output = connection.send_command('show version')
    return output

def main():
    """Main execution."""
    conn = connect_to_device('192.168.1.1', 'admin', 'password')
    info = get_device_info(conn)
    print(info)
    conn.disconnect()

if __name__ == "__main__":
    main()