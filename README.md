
<div align="center">
  <img src="https://img.icons8.com/3d-fluency/94/firewall.png" width="100" alt="Firewall Icon"/>
  <h1>🧹 PAN-OS Unused Object Cleanup Tool</h1>
  <p><strong>Effortlessly detect & delete unused Address and Service objects from your Palo Alto Firewall</strong></p>
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Palo%20Alto-API%20Automation-red?style=flat&logo=palantir&logoColor=white"/>
</div>

---

### 📦 Project Level: `Intermediate to Advanced`
### 🛠️ Tech Stack:
- **Language:** Python 🐍
- **Libs:** `pan-os-python`, `argparse`, `csv`, `datetime`, `os`, `sys`
- **Platform:** Palo Alto Networks PAN-OS

---

## ✨ Features

🚀 **Fast & Reliable PAN-OS Cleanup**  
🔍 Detects unused **Address** and **Service** objects  
🗑️ Deletes unused objects **only with confirmation**  
🧾 Generates detailed **log and CSV reports**  
🧪 Supports **preview-only mode** (no changes, just inspection)  
🛡️ Uses **API key authentication** for secure access  
🗃️ Logs everything under timestamped `logs/` folder  
✅ Exception handling with clear 🔥 error messages

---

## 📸 Demo Output (CLI)

```bash
🚀 Connecting to firewall at 192.168.1.1
🔍 Checking unused service objects...
Found 3 unused service object(s):
  - svc-udp-1337
  - svc-tcp-3389
✅ Deleted service: svc-tcp-3389
🔍 Checking unused address objects...
Found 2 unused address object(s):
  - addr-test-1
  - addr-test-2
✅ Deleted address: addr-test-1

📦 Report saved to logs/cleanup_report_2025-07-03_14-32-10.csv
🧾 Log file saved to logs/cleanup_log_2025-07-03_14-32-10.txt
````

---

## 🧠 How It Works

1. Connects to the PAN-OS firewall using IP and API key
2. Pulls all **service and address objects**
3. Finds which ones are **unused**
4. If `--preview` is set: it **prints them only**
5. If `--confirm` is set: it **deletes them** and logs each action
6. CSV and log files are saved in a `logs/` directory

---

## ⚙️ Usage

### 1️⃣ Get your API key from PAN-OS

```bash
curl -k -X GET 'https://<FIREWALL-IP>/api/?type=keygen&user=admin&password=yourpass'
```

### 2️⃣ Run the script

#### 🔍 Preview only (no deletions):

```bash
python cleanup.py --host 192.168.1.1 --api-key YOUR_API_KEY --preview
```

#### 🗑️ Actual deletion:

```bash
python cleanup.py --host 192.168.1.1 --api-key YOUR_API_KEY --confirm
```

---

## 🔐 Safety

✅ Will **never delete** anything unless `--confirm` flag is added
⚠️ Running with only `--preview` is 100% safe and recommended before any deletion
💾 All activity gets logged and saved

---

## 📁 Output Files

| Type       | Location                    | Format                 |
| ---------- | --------------------------- | ---------------------- |
| Log File   | `logs/cleanup_log_*.txt`    | Human-readable text    |
| CSV Report | `logs/cleanup_report_*.csv` | Table of deleted items |

---

## 📦 Install Requirements

```bash
pip install pan-os-python
```

---

## 🤖 Inspired For

* Network Engineers automating cleanups
* CyberSec teams improving hygiene
* DevOps folks managing infra-as-code
* PAN-OS admins doing routine audits

---

## 🧊 3D ASCII FLAVOR

```
 _______  _______  __    _  _______  _______ 
|       ||       ||  |  | ||       ||       |
|    _  ||   _   ||   |_| ||    ___||    ___|
|   |_| ||  | |  ||       ||   |___ |   |___ 
|    ___||  |_|  ||  _    ||    ___||    ___|
|   |    |       || | |   ||   |___ |   |___ 
|___|    |_______||_|  |__||_______||_______|
```

---

## 🙌 Contribution

Pull requests are welcome! Got a new feature in mind? Let’s collab.

---

## 🧠 Author

Made with ❤️ by [Kalki Akarsh](https://github.com/AkarshYash)
🔗 [TryHackMe](https://tryhackme.com/p/Kalki.Akarsh.18) • 🌐 [Portfolio](https://akarshyash.github.io/Akarsh_Portfolio/) • 🛡️ Cybersecurity Dev

---

## 🪪 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

