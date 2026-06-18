from playwright.sync_api import sync_playwright


class BrowserAgent:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def open_browser(self):
        print("[Browser Agent] Launching browser...")

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.page = self.browser.new_page()

        print("[Browser Agent] Browser launched successfully.")

    def open_google(self):
        print("[Browser Agent] Opening Google...")

        self.page.goto("https://www.google.com")

        print("[Browser Agent] Google opened.")

    def close_browser(self):
        print("[Browser Agent] Closing browser...")

        self.browser.close()
        self.playwright.stop()

        print("[Browser Agent] Browser closed.")