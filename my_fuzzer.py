import requests
import sys

target_url = input("Enter URL: ").strip()

print("\n--- Starting Fuzzing ---")

for word in sys.stdin:
    word = word.strip()
    if not word:
        continue
        
    full_url = f"{target_url}/{word}"
    
    try:
        response = requests.get(full_url)
        r = (f"[{response.status_code}] -> {full_url}")
        print(r.json)

    except requests.exceptions.RequestException as e:
        a = (f"[ERROR] Could not connect to {full_url}: {e}")
        print(a.json())
