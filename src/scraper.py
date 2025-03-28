import json

from scrapegraphai.graphs import SmartScraperGraph


class Scraper:
    def __init__(self, config):
        self.config = config

    def scrape(self, source, prompt) -> dict:
        smart_scraper_graph = SmartScraperGraph(
            prompt=prompt, source=source, config=self.config
        )
        result = smart_scraper_graph.run()
        if type(result) == str:
            result = json.loads(result)
        return result

    def aggregate(self, sources: list):
        scrape_result = []
        for source in sources:
            # Create the SmartScraperGraph instance
            smart_scraper_graph = SmartScraperGraph(
                prompt=source.get("scrape_prompt"),
                source=source.get("scrape_url"),
                config=self.config,
            )
            scrape_result.append(smart_scraper_graph.run())
        return scrape_result
