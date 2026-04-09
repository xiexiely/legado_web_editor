from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print("Navigating to http://localhost:8080")
        page.goto('http://localhost:8080')
        page.wait_for_load_state('networkidle')
        print("Page loaded, taking screenshot")
        page.screenshot(path='screenshot.png', full_page=True)
        print("Screenshot saved to screenshot.png")
        print("Page title:", page.title())
        browser.close()

if __name__ == '__main__':
    run()