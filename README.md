# Network Tool (Python) - Wi-Fi Scanner

This project is a simple Wi-Fi scanner built with Python and [Scapy](https://scapy.net/).  
It detects nearby Wi-Fi networks and displays details such as SSID, BSSID, and signal strength.  

**Disclaimer:** This tool is for research and educational purposes only. Unauthorized use on networks you do not own is illegal.

---

## Features
- Scans nearby Wi-Fi networks
- Displays SSID, MAC address (BSSID), and signal strength
- Saves results to `output.json` (ignored in GitHub for privacy)

---

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/behrambzkrr/network-tool-python.git
cd network-tool-python
pip install -r requirements.txt

Usage

1. Put your Wi-Fi adapter into monitor mode:

sudo airmon-ng start wlan0

2. Run the script:
sudo python scanner.py

3. Results will be printed in the terminal and also saved into output.json locally.

Project Structure:
network-tool-python/
│── scanner.py        # main scanner script
│── requirements.txt  # dependencies
│── .gitignore        # excludes output.json
│── README.md         # project documentation

License

This project is licensed under the MIT License.

