from time import sleep
from typing import List

import streamlit as st
import pandas as pd

import settings

from scraper import Scraper


scraper = Scraper(
    config=settings.graph_config
)

@st.cache_data(ttl=60*60*24)    # ttl 24 hrs
def get_shows(source, prompt) -> List[dict]:
    shows = "Error"
    try:
        shows = scraper.scrape(source=source, prompt=prompt)
        sleep(20)   # avoid rate limit
        if len(shows["content"]) < 1:
            # st.cache_data.clear()
            pass
        return shows["content"]
    except Exception as error:
        print(error, shows)
        raise


def main():
    for site in settings.sites:
        theater_link = f"[{site["theater_name"]}](%s)" % site['theater_url']
        st.image(site["theater_logo_url"], width=150)
        st.write(theater_link)
        try:
            print(site["scrape_url"])
            print(site["scrape_prompt"])
            shows = get_shows(source=site["scrape_url"], prompt=site["scrape_prompt"])
            print(shows)
            df = pd.DataFrame(shows)
            df.columns = ['Show', 'Date(s)', 'Description', ]
            st.write(df.set_index(df.columns[0]))
        except Exception as e:
            print("ERROR", e)
            st.write(
                f"Hmmm... We can't seem to get the shows right now. Check out {theater_link} to see what they have."
            )


main()