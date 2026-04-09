from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=['--disable-blink-features=AutomationControlled'])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        print("Going to https://hlib.cc/ ...")
        page.goto("https://hlib.cc/", timeout=30000, wait_until="domcontentloaded")
        page.wait_for_timeout(10000)
        print("Home Title:", page.title())
        
        # Look for login link and click it
        login_link = page.locator("a:has-text('登录'), a:has-text('Login')").first
        if login_link.count() > 0:
            print("Clicking login link...")
            login_link.click()
            page.wait_for_timeout(10000)
            print("Login Page Title:", page.title())
            
            # Fill form
            email_input = page.locator("input[type='email'], input[name='username'], input[name='email'], input[name='account']")
            pwd_input = page.locator("input[type='password'], input[name='password'], input[name='pwd']")
            
            if email_input.count() > 0 and pwd_input.count() > 0:
                email_input.first.fill("onoaoa@qq.com")
                pwd_input.first.fill("a123321a")
                print("Filled credentials. Submitting...")
                
                submit_btn = page.locator("button[type='submit'], input[type='submit'], button:has-text('登录'), a:has-text('登录')")
                if submit_btn.count() > 0:
                    submit_btn.first.click()
                    page.wait_for_timeout(5000)
                    print("After submit title:", page.title())
                    
                    # Dump cookies
                    cookies = context.cookies()
                    with open('hlib_cookies.txt', 'w') as f:
                        f.write(str(cookies))
                else:
                    print("No submit button found.")
            else:
                print("Could not find email/pwd inputs. Dumping content...")
                print(page.title())
        else:
            print("No login link found.")
            
        browser.close()

run()
