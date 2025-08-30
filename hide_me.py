import requests
from stem import Signal
from stem.control import Controller

# Define Tor proxy settings
TOR_SOCKS_PROXY = "socks5h://localhost:9050"
CONTROL_PORT = 9051
CONTROL_PASSWORD = ""  # For future password setting


# Get current IP via Tor
def get_ip():
    proxies = {
        "http": TOR_SOCKS_PROXY,
        "https": TOR_SOCKS_PROXY,
    }
    try:
        # Send a GET request through Tor
        response = requests.get("https://api.ipify.org", proxies=proxies, timeout=10)
        print("Current IP:", response.text)
    except requests.RequestException as e:
        print("Error fetching IP:", e)


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
            controller.signal(Signal.NEWNYM)  # Request new Tor circuit
            print("Requested new Tor circuit (new IP).")
    except Exception as e:
        print("Error rotating IP:", e)


if __name__ == "__main__":
    print("Checking IP before rotation:")
    get_ip()

    # Optional: rotate IP
    # rotate_ip()

    print("Checking IP after rotation:")
    get_ip()

    print("Checking detailed IP info via Tor:")
    get_ip_info()
