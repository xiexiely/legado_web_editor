from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.on("console", lambda msg: print(f"CONSOLE [{msg.type}]: {msg.text}"))
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
        
        print("Navigating to http://localhost:8081")
        page.goto('http://localhost:8081')
        
        # wait a bit to see if there are any errors
        page.wait_for_timeout(3000)
        
        print("Page title:", page.title())
        content = page.content()
        print("Body content length:", len(content))
        browser.close()

if __name__ == '__main__':
    run()