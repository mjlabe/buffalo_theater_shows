# Define the default configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192
    },
    "verbose": True,
    "headless": True,
    "base_url": "localhost:11434", # set ollama docker URL
}

sites = [
    {
        "theater_name": "Historic Palace Theater",
        "theater_url": "https://lockportpalacetheatre.org",
        "theater_logo_url": "https://lockportpalacetheatre.org/wp-content/uploads/2023/07/Palace-ClearPNG-New.png",
        "scrape_url": "https://historicpalaceinc.thundertix.com",
        "scrape_prompt": "Extract the show names, dates, times, and pictures for all the shows coming up at this theater",
    },
    {
        "theater_name": "Historic Palace Theater",
        "theater_url": "https://lockportpalacetheatre.org",
        "theater_logo_url": "https://lockportpalacetheatre.org/wp-content/uploads/2023/07/Palace-ClearPNG-New.png",
        "scrape_url": "https://historicpalaceinc.thundertix.com",
        "scrape_prompt": "Extract the show names, dates, times, and pictures for"
    },
]
