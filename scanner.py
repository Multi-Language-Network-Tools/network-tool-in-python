from scapy.all import *
import json

networks = {}

def callback(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet.info.decode(errors="ignore")
        bssid = packet.addr2
        try:
            signal_strength = packet.dBm_AntSignal
        except:
            signal_strength = "N/A"

        networks[bssid] = {
            "SSID": ssid,
            "Signal": signal_strength
        }

def scan(duration=10):
    print(f"[i] {duration} saniye boyunca tarama yapılıyor...")

    sniff(prn=callback, iface="wlan0mon", timeout=duration, store=0)

    print(f"\n[i] {len(networks)} ağ bulundu.\n")

    # Terminal çıktısı
    for bssid, info in networks.items():
        print(f"📶 {info['SSID']} | BSSID: {bssid} | Güç: {info['Signal']} dBm")

    # JSON kaydet
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(networks, f, indent=4, ensure_ascii=False)

    print("\n[✔] Sonuçlar output.json dosyasına kaydedildi (GitHub'a yüklenmeyecek).")

if __name__ == "__main__":
    scan(15)
