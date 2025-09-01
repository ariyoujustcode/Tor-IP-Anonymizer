import time
import requests
from stem import Signal
from bs4 import BeautifulSoup
from stem.control import Controller

# Define Tor proxy settings
TOR_SOCKS_PROXY = "socks5h://localhost:9050"
CONTROL_PORT = 9051
CONTROL_PASSWORD = "REMOVED"  # Password

proxies = {
    "http": TOR_SOCKS_PROXY,
    "https": TOR_SOCKS_PROXY,
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/116.0.5845.188 Safari/537.36"
}
target_url = "https://en.wikipedia.org/wiki/Radio_Nacional_de_Espa%C3%B1a"


# Get current IP via Tor
def get_ip():
    try:
        response = requests.get("https://api.ipify.org", proxies=proxies, timeout=10)
        return response.text
    except requests.RequestException as e:
        print("Error fetching IP:", e)
        return None


def get_ip_info():
    proxies = {
        "http": TOR_SOCKS_PROXY,
        "https": TOR_SOCKS_PROXY,
    }
    try:
        # Request IP info through Tor
        response = requests.get("https://ipapi.co/json", proxies=proxies, timeout=10)
        data = response.json()  # Parse JSON response
        print("Tor IP Info:")
        print("IP:", data.get("ip"))
        print("City:", data.get("city"))
        print("Region:", data.get("region"))
        print("Country:", data.get("country_name"))
    except requests.RequestException as e:
        print("Error fetching IP info:", e)


# Request a new Tor IP (new circuit for future implementation)
def rotate_ip():
    try:
        with Controller.from_port(port=CONTROL_PORT) as controller:
            controller.authenticate(password=CONTROL_PASSWORD)
            controller.signal(Signal.NEWNYM)
            print("Rotated Tor IP")
    except Exception as e:
        print("Error rotating IP:", e)


if __name__ == "__main__":
    while True:
        # Check current IP
        ip = get_ip()
        print(f"Current Tor IP: {ip}")
        get_ip_info()

        time.sleep(5)
        # Visit target site
        try:
            response = requests.get(
                target_url, proxies=proxies, headers=headers, timeout=15
            )
            print(f"Visited {target_url} with IP {ip}, Status: {response.status_code}")

            # Extract readable text
            soup = BeautifulSoup(response.text, "html.parser")
            page_text = soup.get_text(separator="\n", strip=True)
            print(page_text[:500])  # preview first 500 chars
        except requests.RequestException as e:
            print("Error visiting site:", e)

        # Rotate IP
        rotate_ip()
        print("Sleeping 30 seconds before next rotation...\n")
        time.sleep(30)
