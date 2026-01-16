import os
import subprocess
from art import create_ascii_text

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_ip(ip_list, ips_to_block):
    """Add IPs to the file and apply UFW deny rules."""
    with open(ip_list, 'a') as file:
        for ip in ips_to_block:
            file.write(f"{ip}\n")
            print(f"Added {ip} to {ip_list}.")
            apply_ufw_rule(ip, "deny")

def remove_ip(ip_list, ip_to_remove):
    """Remove an IP from the file and revoke UFW deny rule."""
    if not os.path.exists(ip_list):
        print(f"{ip_list} does not exist.")
        return
    
    # Read current IPs
    with open(ip_list, 'r') as file:
        ips = file.readlines()

    # Write back only those that are not the IP to remove
    with open(ip_list, 'w') as file:
        removed = False
        for ip in ips:
            ip = ip.strip()
            if ip == ip_to_remove:
                print(f"Removing {ip_to_remove} from {ip_list}.")
                revoke_ufw_rule(ip_to_remove)
                removed = True
            else:
                file.write(f"{ip}\n")
    
    if not removed:
        print(f"IP {ip_to_remove} not found in {ip_list}.")

def apply_ufw_rule(ip, action, port=None):
    """Apply UFW rule to deny or allow traffic from a specific IP, optionally for a specific port."""
    command = f"sudo ufw {action} from {ip}"
    if port:
        command += f" to any port {port}"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully applied rule to {action} IP: {ip} {'on port ' + str(port) if port else ''}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to apply rule for IP: {ip}. Error: {e}")

def revoke_ufw_rule(ip, port=None):
    """Revoke UFW rule that denies or allows traffic from a specific IP, optionally for a specific port."""
    apply_ufw_rule(ip, "delete deny", port)
    apply_ufw_rule(ip, "delete allow", port)

def allow_ip_port(ips, ports):
    """Allow traffic from specific IPs to specific ports."""
    for ip in ips:
        for port in ports:
            apply_ufw_rule(ip, "allow", port)

def revoke_specific_rule(ips, ports):
    """Revoke specific UFW rule that allows traffic from specific IPs to specific ports."""
    for ip in ips:
        for port in ports:
            revoke_ufw_rule(ip, port)

def main():
    # Path to the file containing the list of malicious IPs
    ip_list = 'malicious_ips.txt'#must exist

    # Ensure the file exists
    if not os.path.exists(ip_list):
        open(ip_list, 'w').close()
        print(f"{ip_list} created.")

    # Prompt the user for action
    print("What would you like to do?")
    print("1. Add IP(s) to block")
    print("2. Remove IP from block list")
    print("3. Remove specific rule for IP(s) and port(s) (e.g., allow port 22)")
    print("4. Allow IP(s) for specific port(s)")
    action = input("Enter the number of your choice: ")

    if action == "1":
        print("Enter the IP addresses you wish to block (separate multiple IPs with commas):")
        user_input = input()
        ips_to_block = [ip.strip() for ip in user_input.split(",") if ip.strip()]
        add_ip(ip_list, ips_to_block)
    elif action == "2":
        print("Enter the IP address you wish to unblock:")
        ip_to_remove = input().strip()
        remove_ip(ip_list, ip_to_remove)
    elif action == "3":
        print("Enter the IP addresses for which you want to remove specific rules (separate multiple IPs with commas):")
        ips_to_remove = [ip.strip() for ip in input().split(",") if ip.strip()]
        print("Enter the port numbers for the rules (separate multiple ports with commas, leave empty if not port-specific):")
        ports_to_remove = [port.strip() for port in input().split(",") if port.strip()]
        revoke_specific_rule(ips_to_remove, ports_to_remove or [None])
    elif action == "4":
        print("Enter the IP addresses you wish to allow (separate multiple IPs with commas):")
        ips_to_allow = [ip.strip() for ip in input().split(",") if ip.strip()]
        print("Enter the port numbers you wish to allow (separate multiple ports with commas):")
        ports_to_allow = [port.strip() for port in input().split(",") if port.strip()]
        allow_ip_port(ips_to_allow, ports_to_allow)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    try:
        create_ascii_text()
        main()
    except KeyboardInterrupt:
        clear()
