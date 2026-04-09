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
        page.wait_for_timeout(5000)
        print("Title:", page.title())
        
        # Check links
        print("Looking for login link...")
        login_link = None
        for a in page.locator("a").all():
            text = a.inner_text().strip()
            href = a.get_attribute("href")
            if "登录" in text or "login" in str(href).lower():
                print(f"Found login link: {text} -> {href}")
                login_link = href
                
        if login_link:
            print("Navigating to login link:", login_link)
            if login_link.startswith('/'):
                login_link = 'https://hlib.cc' + login_link
            elif not login_link.startswith('http'):
                login_link = 'https://hlib.cc/' + login_link
                
            page.goto(login_link, timeout=30000, wait_until="domcontentloaded")
            page.wait_for_timeout(3000)
            print("Login Page Title:", page.title())
            
            # Fill form
            # Assuming standard input names like username, email, account, password
            print("Filling form...")
            # Try to find input type email or text
            email_input = page.locator("input[type='email'], input[name='username'], input[name='email'], input[name='account']")
            pwd_input = page.locator("input[type='password'], input[name='password'], input[name='pwd']")
            
            if email_input.count() > 0 and pwd_input.count() > 0:
                email_input.first.fill("onoaoa@qq.com")
                pwd_input.first.fill("a123321a")
                print("Filled credentials. Submitting...")
                
                # Click submit button
                submit_btn = page.locator("button[type='submit'], input[type='submit'], button:has-text('登录'), a:has-text('登录')")
                if submit_btn.count() > 0:
                    submit_btn.first.click()
                    page.wait_for_timeout(5000)
                    print("After submit title:", page.title())
                else:
                    print("No submit button found.")
            else:
                print("Could not find email/pwd inputs.")
                print(page.content())
        else:
            print("No login link found.")
            print(page.content())
            
        # Get cookies to use later
        cookies = context.cookies()
        with open('hlib_cookies.txt', 'w') as f:
            f.write(str(cookies))
            
        browser.close()

run()
