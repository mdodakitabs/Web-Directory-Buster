import sys
import time
import requests

# ANSI Escape Codes for Terminal coloring
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_RESET = "\033[0m"

# Default trial wordlist for directory brute-forcing
DEFAULT_WORDLIST = [
    "admin",
    "login",
    "dashboard",
    "backup",
    "config",
    "secret",
    "db",
    "uploads",
    "api",
    "test",
    "v1",
    "robots.txt",
    ".env",
]


def dir_buster(target_url, wordlist):
    # Ensure the target URL is formatted properly
    if not target_url.startswith("http://") and not target_url.startswith(
        "https://"
    ):
        target_url = "http://" + target_url

    # Strip the trailing slash if present to prevent double slashes
    if target_url.endswith("/"):
        target_url = target_url[:-1]

    print(f"{COLOR_GREEN}[*] Starting scan on target: {target_url}{COLOR_RESET}")
    print(
        f"{COLOR_GREEN}[*] Total words in target list: {len(wordlist)}{COLOR_RESET}\n"
    )

    for word in wordlist:
        # Construct the full URL path to test
        test_url = f"{target_url}/{word}"

        try:
            # Send HTTP request with 3-second timeout and ignore SSL verification warnings
            response = requests.get(test_url, timeout=3, verify=False)

            # Check if the directory/file exists and is accessible
            if response.status_code == 200:
                print(
                    f"{COLOR_GREEN}[+][200 OK] Found directory: {test_url}{COLOR_RESET}"
                )
            # Check if the path exists but access is restricted
            elif response.status_code == 403:
                print(
                    f"{COLOR_YELLOW}[![403 Forbidden] Protected path: {test_url}{COLOR_RESET}"
                )

        except requests.exceptions.RequestException:
            # Skip common network errors, timeouts, or connection failures
            continue

        # Short delay to prevent crashing or triggering aggressive rate limits
        time.sleep(0.1)

    print(f"\n{COLOR_GREEN}[+] Security scan completed.{COLOR_RESET}")


if __name__ == "__main__":
    try:
        print(
            f"{COLOR_GREEN}=== Web Directory Buster (Recon Tool) ==={COLOR_RESET}"
        )
        target = input("Enter target URL (e.g., google.com): ").strip()

        if target:
            dir_buster(target, DEFAULT_WORDLIST)
        else:
            print(f"{COLOR_RED}[-] Error: No target URL entered.{COLOR_RESET}")
    except KeyboardInterrupt:
        print(f"\n{COLOR_YELLOW}[-] Scan stopped by user.{COLOR_RESET}")

