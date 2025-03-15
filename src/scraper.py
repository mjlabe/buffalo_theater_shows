import json
import os
from pathlib import Path

from scrapegraphai.graphs import SmartScraperGraph

from src.settings import settings


settings_file_path = os.environ.get("DS9_SETTINGS_MODULE", Path("src", "settings", "default"))


class Scraper:
    @staticmethod
    def scrape(self):
        scrape_result = []
        for site in settings().get("sites"):
            # Create the SmartScraperGraph instance
            smart_scraper_graph = SmartScraperGraph(
                prompt=site.get("prompt"),
                source=site.get("url"),
                config=settings().get("graph_config")
            )
            scrape_result.append(smart_scraper_graph.run())
        return result


if __name__ == '__main__':
    # Run the pipeline
    scrape_urls = settings().get("scrape_urls")
    scraper = Scraper()
    result = scraper.scrape(scrape_urls)

    print(json.dumps(result, indent=4))
