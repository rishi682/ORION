from backend.agents.browser_agent import BrowserAgent


def execute_plan(plan):

    logs = []

    browser = BrowserAgent()

    browser.open_browser()

    for step in plan:

        log = f"Executing: {step}"
        print(log)
        logs.append(log)

    browser.open_google()

    input("\nPress Enter to close the browser...")

    browser.close_browser()

    return logs