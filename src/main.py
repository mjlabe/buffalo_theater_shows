import logging
from time import sleep
from typing import List

import streamlit as st
import pandas as pd

import settings

from scraper import Scraper


logger = logging.getLogger(__name__)

scraper = Scraper(
    config=settings.graph_config
)

@st.cache_data(ttl=60*60*24)    # ttl 24 hrs
def get_shows(source, prompt) -> List[dict]:
    sleep(10)   # avoid rate limit
    logger.info("Fetching theater listings from %s", source)
    shows = scraper.scrape(source=source, prompt=prompt)
    if not shows:
        # st.cache_data.clear()
        raise ValueError("Scraper returned no upcoming shows")
    return shows


def main():
    for site in settings.sites:
        theater_link = f"[{site["theater_name"]}](%s)" % site['theater_url']
        st.image(site["theater_logo_url"], width=150)
        st.write(theater_link)
        try:
            shows = get_shows(source=site["scrape_url"], prompt=site["scrape_prompt"])
            df = pd.DataFrame(shows, columns=['Show', 'Date(s)', 'Description'])
            df["Description"] = df["Description"].fillna("")
            st.dataframe(df.set_index('Show'), use_container_width=True)
        except Exception:
            logger.exception(
                "Failed to load listings for theater %s from %s",
                site["theater_name"],
                site["scrape_url"],
            )
            st.write(
                f"Hmmm... We can't seem to get the shows right now. Check out {theater_link} to see what they have."
            )


main()