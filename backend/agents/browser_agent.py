from playwright.sync_api import sync_playwright
from backend.services.search_service import SearchService
from backend.utils.selectors import *


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

    def search_google(self, query):

        print(f"[Browser Agent] Searching: {query}")

        self.page.goto(GOOGLE_URL)

        self.page.fill(SEARCH_BOX, query)

        self.page.keyboard.press("Enter")

        self.page.wait_for_load_state("networkidle")

        return SearchService.extract_results(self.page)

    def close_browser(self):

        self.browser.close()

        self.playwright.stop()

        print("[Browser Agent] Closed.")