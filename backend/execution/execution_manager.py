from backend.agents.browser_agent import BrowserAgent


def execute_plan(goal):

    browser = BrowserAgent()

    browser.open_browser()

    results = browser.search_google(goal)

    browser.close_browser()

    return results