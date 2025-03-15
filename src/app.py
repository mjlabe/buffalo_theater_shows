import streamlit as st

import pandas as pd

from scrapers import theater_scraper

from settings import theaters


for theater in theaters:
    shows = theater_scraper(theater.get("shows_url"))
    theater_names.append(theater.get("name"))
    show_data = pd.DataFrame({
        "theater": theater_names,
        "shows": shows
    })
    
st.write("Here's our first attempt at using data to create a table:")
st.write(show_data)