import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch():
    try:
        r = requests.get("https://hlib.cc/", headers=headers, timeout=10)
        r.encoding = r.apparent_encoding or 'utf-8'
        print("Status code:", r.status_code)
        
        soup = BeautifulSoup(r.text, 'lxml')
        print("Title:", soup.title.string if soup.title else "No title")
        
        # Look for search form
        forms = soup.find_all('form')
        for form in forms:
            print("Form action:", form.get('action'), "method:", form.get('method'))
            inputs = form.find_all('input')
            for inp in inputs:
                print("  Input:", inp.get('name'), inp.get('type'))
                
        # Look for typical book links
        links = soup.find_all('a', href=True)
        for link in links[:20]:
            print("Link:", link.get('href'), link.text.strip())
            
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    fetch()