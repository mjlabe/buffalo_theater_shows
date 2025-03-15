import json
from scrapegraphai.graphs import SmartScraperGraph


# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192
    },
    "verbose": True,
    "headless": True,
}


def theater_scraper(url):
    # Create the SmartScraperGraph instance
    smart_scraper_graph = SmartScraperGraph(
        prompt="Extract the show names, dates, times, and urls to the shows pictures for all the shows coming up at this theater",
        source=url,
        config=graph_config
    )
    result = smart_scraper_graph.run()
    return result


if __name__ == '__main__':
    # Run the pipeline
    url = ""
    result = theater_scraper(url):

    print(json.dumps(result, indent=4))
