import argparse
import csv
import sys
import os
from datetime import datetime
from panos.firewall import Firewall
from panos.errors import PanDeviceError

# 🛠️ Setup log file
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_path = os.path.join(log_dir, f"cleanup_log_{timestamp}.txt")
csv_file_path = os.path.join(log_dir, f"cleanup_report_{timestamp}.csv")

def log(msg):
    print(msg)
    with open(log_file_path, "a") as f:
        f.write(msg + "\n")

def write_csv(report_data):
    with open(csv_file_path, mode="w", newline="") as csvfile:
        fieldnames = ["Type", "Object Name"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in report_data:
            writer.writerow(row)

def cleanup(fw, preview=False, confirm=False):
    report = []

    try:
        log("🔍 Checking unused service objects...")
        unused_services = fw.services.unused()
        if unused_services:
            log(f"Found {len(unused_services)} unused service object(s):")
            for svc in unused_services:
                log(f"  - {svc.name}")
                report.append({"Type": "Service", "Object Name": svc.name})

            if not preview and confirm:
                for svc in unused_services:
                    try:
                        fw.services.delete(svc)
                        log(f"✅ Deleted service: {svc.name}")
                    except PanDeviceError as e:
                        log(f"❌ Error deleting service {svc.name}: {e}")

        log("🔍 Checking unused address objects...")
        unused_addresses = fw.addresses.unused()
        if unused_addresses:
            log(f"Found {len(unused_addresses)} unused address object(s):")
            for addr in unused_addresses:
                log(f"  - {addr.name}")
                report.append({"Type": "Address", "Object Name": addr.name})

            if not preview and confirm:
                for addr in unused_addresses:
                    try:
                        fw.addresses.delete(addr)
                        log(f"✅ Deleted address: {addr.name}")
                    except PanDeviceError as e:
                        log(f"❌ Error deleting address {addr.name}: {e}")

    except PanDeviceError as e:
        log(f"🔥 PAN-OS API Error: {e}")
        sys.exit(1)

    write_csv(report)
    log(f"\n📦 Report saved to {csv_file_path}")
    log(f"🧾 Log file saved to {log_file_path}")

def main():
    parser = argparse.ArgumentParser(description="🔧 Palo Alto Unused Object Cleanup Tool")
    parser.add_argument("--host", required=True, help="Firewall IP address (e.g., 10.0.0.1)")
    parser.add_argument("--api-key", required=True, help="API key for firewall access")
    parser.add_argument("--preview", action="store_true", help="Preview unused objects without deleting")
    parser.add_argument("--confirm", action="store_true", help="Confirm deletion of unused objects")

    args = parser.parse_args()

    if not args.preview and not args.confirm:
        log("⚠️ Use --preview to see unused objects, or --confirm to actually delete them.")
        sys.exit(0)

    log(f"🚀 Connecting to firewall at {args.host}")
    fw = Firewall(args.host, api_key=args.api_key)

    cleanup(fw, preview=args.preview, confirm=args.confirm)

if __name__ == "__main__":
    main()
