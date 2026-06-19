from backend.utils.selectors import *


class SearchService:

    @staticmethod
    def extract_results(page):

        data = []

        results = page.query_selector_all(RESULTS)

        for result in results[:5]:

            try:

                title = result.query_selector(TITLE)

                link = result.query_selector(LINK)

                snippet = result.query_selector(SNIPPET)

                data.append({
                    "title": title.inner_text() if title else "",
                    "url": link.get_attribute("href") if link else "",
                    "snippet": snippet.inner_text() if snippet else ""
                })

            except Exception:
                continue

        return data