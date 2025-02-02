# Firewall_IP_Blocker

## Overview
This script automates IP blocking and allowlisting using UFW (Uncomplicated Firewall). It enables users to:

- Block malicious IPs by adding them to a `malicious_ips.txt` file.
- Remove specific IPs from the blocklist.
- Allow specific IPs to access designated ports.
- Revoke previously set firewall rules.

The script helps enhance server security by preventing unauthorized access while maintaining necessary connectivity.

## Precautions
- **Run as root:** The script requires `sudo` privileges to modify firewall rules.
- **Ensure `malicious_ips.txt` exists:** This file is necessary to track blocked IPs. The script will create it if absent.
- **Use with caution:** Improper use may block critical IPs, leading to connectivity issues.
- **Test before deployment:** Always verify changes in a controlled environment before applying them to production systems.

## Requirements
- **Python 3.x**
- **UFW (Uncomplicated Firewall)** installed and enabled
- **sudo/root access** to apply firewall rules

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/cyb2rS2c/Firewall_IP_Blocker.git
   cd Firewall_IP_Blocker
   ```
2. Ensure Python is installed and updated.

## Usage
1. Add malicious IPs to `malicious_ips.txt`.
2. Run the script:
   ```sh
   python3 prevent_malicious_ips_ufw.py
   ```
3. Follow the menu prompts to add, remove, or modify firewall rules.

Ensure that you have the necessary privileges and that UFW is correctly configured before running the script.

