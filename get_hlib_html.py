from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--disable-blink-features=AutomationControlled'])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        page.goto("https://hlib.cc/", timeout=30000, wait_until="domcontentloaded")
        page.wait_for_timeout(10000)
        
        with open('hlib_home.html', 'w', encoding='utf-8') as f:
            f.write(page.content())
            
        print("HTML saved to hlib_home.html")
        browser.close()

run()
