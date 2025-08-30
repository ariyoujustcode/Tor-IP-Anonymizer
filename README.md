# Tor IP Anonymizer Script

## Overview
This Python script allows you to **hide your real IP address** by routing HTTP requests through the Tor network. It uses a SOCKS5 proxy to send requests anonymously and can optionally rotate Tor circuits for a new IP (requires Tor control port authentication).

The script is a practical tool for learning **networking, Python scripting, and cybersecurity concepts**, and can be used to fetch your current public IP and approximate location safely.

## Features
- Sends HTTP requests through Tor to hide your real IP.
- Retrieves your current public IP as seen through Tor.
- Fetches approximate geolocation of the Tor exit node.
- Optional Tor circuit rotation for new IPs (future feature with control password).

## Requirements
- Python 3.9+  
- Tor installed and running on your system  
- Python libraries: `requests[socks]`, `stem`  
- Virtual environment recommended

## Installation
1. Activate your virtual environment:  
```bash
source venv/bin/activate
```

## Install Python packages
```bash
pip install "requests[socks]" stem
```

## Run Tor
```bash
tor
```

## Run Script
```bash
python hide_me.py
```
