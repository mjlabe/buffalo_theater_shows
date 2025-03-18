import os

# # Define the default configuration for the scraping pipeline
# graph_config = {
#     "llm": {
#         "model": "ollama/llama3.2",
#         "model_tokens": 8192
#     },
#     "verbose": True,
#     "headless": True,
#     "base_url": "localhost:11434", # set ollama docker URL
# }

graph_config = {
    "llm": {
        "api_key": os.environ.get("OPENAI_API_KEY"),
        "model": "openai/gpt-4o-mini",
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
        "scrape_prompt": "Extract the show names, performance date range and description for all the shows coming up at this theater",
    },
    {
        "theater_name": "Alleyway Theater",
        "theater_url": "https://www.alleyway.com",
        "theater_logo_url": "https://theatreallianceofbuffalo.com/wp-content/uploads/2023/08/e80ea4b25f92badeff119c0c9c1eb040_f1245.jpg",
        "scrape_url": "https://www.alleyway.com",
        "scrape_prompt": "Extract the show names, performance date range and description for all the shows coming up at this theater",
    },
    {
        "theater_name": "Road Less Travelled Theater",
        "theater_url": "https://www.roadlesstraveledproductions.org/",
        "theater_logo_url": "https://americantheatrewing.org/wp-content/uploads/2017/10/Road-Less-Travelled-Productions-Logo.jpg",
        "scrape_url": "https://www3.erie.gov/cultural/arts/road-less-traveled-productions",
        "scrape_prompt": "Extract the show names, performance date range and description for all the shows coming up at this theater",
    },
    {
        "theater_name": "O'Connell & Company",
        "theater_url": "https://www.oconnellandcompany.com",
        "theater_logo_url": "https://static.wixstatic.com/media/bfd37b_046daf048f424673a124abba03e860c7~mv2.png",
        "scrape_url": "https://www.oconnellandcompany.com",
        "scrape_prompt": "Extract the show names, performance date range and description for all the shows coming up at this theater",
    },
    {
        "theater_name": "Shea's Buffalo",
        "theater_url": "https://www.sheas.org/buffalo-theatre/",
        "theater_logo_url": "https://www.wnyfamilymagazine.com/downloads/5357/download/Shea%27s%20Logo.jpg?cb=27033d2d34f3609e6134226ea738181d",
        "scrape_url": "https://www.sheas.org/buffalo-theatre/",
        "scrape_prompt": "Extract the show names, performance date range and description for all the shows coming up at this theater",
    },
    {
        "theater_name": "Shea's 710",
        "theater_url": "https://www.sheas.org/710-theatre/",
        "theater_logo_url": "https://www.sheas.org/wp-content/uploads/2019/03/sheas-building-icon-sketches-sheas-710-PORTRAIT-SIZE.jpg",
        "scrape_url": "https://www.sheas.org/710-theatre/",
        "scrape_prompt": "Extract the show names, performance date range and description for all the shows coming up at this theater",
    },
    {
        "theater_name": "Shea's Smith",
        "theater_url": "https://www.sheas.org/smith-theatre/",
        "theater_logo_url": "https://www.sheas.org/wp-content/uploads/2019/03/sheas-building-icon-sketches-sheas-smith-PORTRAIT-SIZE.jpg",
        "scrape_url": "https://www.sheas.org/smith-theatre/",
        "scrape_prompt": "Extract the show names, performance date range and description for all the shows coming up at this theater",
    },
]
