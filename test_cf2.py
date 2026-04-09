from curl_cffi import requests
session = requests.Session(impersonate="chrome110")
res = session.get("https://hlib.cc/", timeout=15)
print("Status:", res.status_code)
if "Just a moment" in res.text:
    print("CF challenge.")
else:
    print("Bypassed!")
