from DrissionPage import ChromiumPage, ChromiumOptions
import time

co = ChromiumOptions()
co.headless()
co.set_argument('--no-sandbox')
co.set_argument('--disable-gpu')
co.set_argument('--disable-blink-features=AutomationControlled')

page = ChromiumPage(co)
print("Navigating to https://hlib.cc/")
page.get("https://hlib.cc/")
print("Waiting 10 seconds...")
time.sleep(10)
print("Title:", page.title)

if "Just a moment" in page.title:
    print("Trying to bypass CF by clicking checkbox if present...")
    try:
        # CF usually has an iframe or shadow dom for the checkbox, it's hard to click headlessly
        ele = page.ele('tag:iframe', timeout=2)
        if ele:
            print("Found iframe, wait 5s...")
            time.sleep(5)
    except:
        pass
    print("Title after wait:", page.title)

page.quit()
