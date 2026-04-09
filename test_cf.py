from curl_cffi import requests
from bs4 import BeautifulSoup

session = requests.Session(impersonate="chrome120")
res = session.get("https://hlib.cc/", timeout=15)
print("Status:", res.status_code)
print("Title:", BeautifulSoup(res.text, "html.parser").title.string if BeautifulSoup(res.text, "html.parser").title else "No Title")

links = BeautifulSoup(res.text, "html.parser").find_all("a")
for a in links:
    if a.string and "登录" in a.string:
        print("Login link:", a.get("href"))
