# Firewall Cleanup Script

This script automates the cleanup of unused service and address objects in a Palo Alto Networks firewall. By leveraging the `pan-os-python` library, it identifies and deletes unused objects to help maintain an optimized and efficient configuration.

---

## Features
- **Detect Unused Objects:** Identifies unused service and address objects on the firewall.
- **Automated Cleanup:** Deletes unused objects to streamline the firewall's configuration.
- **Efficient API Integration:** Uses the `pan-os-python` library for seamless interaction with the firewall.

---

## Prerequisites
### 1. Python Installation
Ensure Python 3.6 or higher is installed on your system.

### 2. Install Required Library
The script uses the `pan-os-python` library for interaction with the firewall. Install it using pip:
```bash
pip install pan-os-python
```

### 3. API Access
- Ensure you have API access enabled on your Palo Alto Networks firewall.
- Replace `your_api_key` in the script with your actual API key.

---

## Usage

### Script Configuration
1. Replace `10.0.0.1` with the IP address of your firewall.
2. Replace `your_api_key` with a valid API key.

### Running the Script
Run the script with Python:
```bash
python cleanup_script.py
```

### Script Output
- Lists all unused service and address objects.
- Deletes the unused objects and provides feedback on the cleanup process.

---

## Code Walkthrough

### Importing the Library
The `panos.firewall.Firewall` class is used to connect to and manage the firewall.

### Connecting to the Firewall
```python
fw = Firewall("10.0.0.1", api_key="your_api_key")
```
Connects to the firewall using the specified IP address and API key.

### Checking for Unused Objects
```python
unused_services = fw.services.unused()
unused_addresses = fw.addresses.unused()
```
Retrieves unused service and address objects.

### Deleting Unused Objects
```python
for unused_service in unused_services:
    fw.services.delete(unused_service)

for unused_address in unused_addresses:
    fw.addresses.delete(unused_address)
```
Deletes unused service and address objects from the firewall.

---

## Example Output
```plaintext
Unused service objects found:
- tcp_8080
- udp_1234

Unused address objects found:
- server_old
- client_temp

Deleting unused service objects...
tcp_8080 deleted.
udp_1234 deleted.

Deleting unused address objects...
server_old deleted.
client_temp deleted.
```

---

## Benefits
- Simplifies firewall management by cleaning up unused objects.
- Reduces clutter in the firewall configuration.
- Improves firewall performance and maintainability.

---

## Known Limitations
1. **API Key Security:** Ensure your API key is stored securely and not hard-coded in production environments.
2. **Object Dependencies:** Objects in use by other configurations may cause errors during deletion. Handle dependencies before running the script.

---

## Author
This script is a demonstration of Palo Alto Networks firewall automation using the `pan-os-python` library. Contributions and enhancements are welcome.

---

## License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

