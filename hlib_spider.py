from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--disable-blink-features=AutomationControlled'])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        print("Visiting https://hlib.cc/")
        try:
            page.goto('https://hlib.cc/', timeout=15000)
            page.wait_for_timeout(5000)  # Wait for CF challenge
            print("Home Title:", page.title())
            
            print("Visiting login page...")
            page.goto('https://hlib.cc/login.php', timeout=15000)
            page.wait_for_timeout(3000)
            print("Login Title:", page.title())
            
            with open('hlib_login.html', 'w', encoding='utf-8') as f:
                f.write(page.content())
                
        except Exception as e:
            print("Error:", e)
        finally:
            browser.close()

if __name__ == '__main__':
    run()