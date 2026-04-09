from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        print("Navigating to https://hlib.cc/")
        try:
            page.goto('https://hlib.cc/', timeout=15000)
            page.wait_for_load_state('networkidle')
            print("Page title:", page.title())
            content = page.content()
            with open('hlib_home.html', 'w', encoding='utf-8') as f:
                f.write(content)
            print("Homepage saved to hlib_home.html")
            
            # Try to find a search form
            search_forms = page.locator('form').all()
            print(f"Found {len(search_forms)} forms")
            for i, form in enumerate(search_forms):
                action = form.get_attribute('action')
                method = form.get_attribute('method')
                print(f"Form {i}: action={action}, method={method}")
                
            # Click the first link to a book (just an example to see info page)
            # Find an anchor that looks like a book link
            links = page.locator('a').all()
            book_links = []
            for link in links:
                href = link.get_attribute('href')
                if href and ('/book/' in href or '/info/' in href or '.html' in href):
                    book_links.append(href)
            print(f"Found {len(book_links)} potential book links.")
            if book_links:
                print(f"Sample book links: {book_links[:5]}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == '__main__':
    run()