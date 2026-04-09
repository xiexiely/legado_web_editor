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
        try:
            page.goto("https://hlib.cc/", timeout=30000, wait_until="domcontentloaded")
        except Exception as e:
            print("Goto timeout:", e)
            
        print("Wait 10s for CF...")
        page.wait_for_timeout(10000)
        print("Title:", page.title())
        
        # Take a screenshot to see what's going on
        page.screenshot(path="cf_screenshot.png")
        
        # Check if there is an iframe for CF challenge
        if "Just a moment" in page.title():
            print("Still in CF. Try to find checkbox.")
            try:
                frames = page.frames
                for f in frames:
                    print("Frame url:", f.url)
            except Exception as e:
                print("Frame error:", e)
                
        print("Done.")
        browser.close()

run()
