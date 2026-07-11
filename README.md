# Web Directory Buster (Recon Tool)

A lightweight, automated web reconnaissance script written in Python. It is designed for penetration testers, bug bounty hunters, and ethical hackers to discover hidden paths, files, and directories on a target web server using a dictionary-based brute-force approach.

## ✨ Features
- **HTTP Status Auditing:** Dynamically detects and alerts on `200 OK` (accessible paths) and `403 Forbidden` (restricted/protected directories).
- **Clean Terminal UI:** Suppresses disruptive SSL/TLS warnings (`InsecureRequestWarning`) for a noise-free auditing experience.
- **Resilient & Safe Scanning:** Implements connection timeouts and structured pacing delays (`time.sleep`) to prevent target server flooding or script hanging.
- **Cross-Platform Compatibility:** Runs flawlessly across Linux, macOS, Windows Terminals, and Android mobile environments (via Termux).

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Web-Directory-Buster
   ```

2. **Install dependencies:**
   Make sure you have the `requests` library installed.
   ```bash
   pip install requests
   ```

3. **Run the script:**
   ```bash
   python dir_buster.py
   ```

4. **Input the Target:**
   When prompted, enter your target domain (e.g., `example.com` or `google.com`).

## ⚙️ How it Works
The script takes a target URL and appends directory names from a built-in cryptographic wordlist (e.g., `admin`, `.env`, `backup`). It fires structured HTTP requests to each path. By evaluating the server's response headers, it immediately highlights active or hidden resources that developers might have mistakenly left exposed to the public web.

## ⚠️ Disclaimer
This tool is strictly intended for educational and authorized security auditing purposes only. Do not scan websites or targets without explicit legal permission from the owner. The developer assumes no liability for misuse or unauthorized actions.

## 🛡️ License
This project is open-source and available under the [MIT License](LICENSE).
