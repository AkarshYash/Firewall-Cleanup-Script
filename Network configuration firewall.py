from panos.firewall import Firewall

fw = Firewall("10.0.0.1", api_key="your_api_key")

# Check for unused service objects
unused_services = fw.services.unused()
if unused_services:
    print("Unused service objects found:")
    for unused_service in unused_services:
        print(unused_service)

# Check for unused address objects
unused_addresses = fw.addresses.unused()
if unused_addresses:
    print("Unused address objects found:")
    for unused_address in unused_addresses:
        print(unused_address)
        
        # Delete unused service objects
for unused_service in unused_services:
    fw.services.delete(unused_service)

# Delete unused address objects
for unused_address in unused_addresses:
    fw.addresses.delete(unused_address)