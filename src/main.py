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

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract the show names, dates, times, and urls to the shows pictures for all the shows coming up at this theater",
    source="https://historicpalaceinc.thundertix.com",
    config=graph_config
)


if __name__ == '__main__':
    # Run the pipeline
    result = smart_scraper_graph.run()

    print(json.dumps(result, indent=4))
