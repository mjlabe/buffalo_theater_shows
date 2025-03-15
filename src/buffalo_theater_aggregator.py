import streamlit as st
import pandas as pd

from src.scraper import Scraper

import settings


def format_sites_data(scraped_data):
    pass
    return []
    
    
def main():
    scraper = Scraper(
        config = settings.graph_config
    )
    scraped_sites_data = scraper.aggregate(sources=settings.sites)
    df = pd.DataFrame(format_sites_data(scraped_sites_data)
    st.write(df)


if __name__ == '__main__':
    main()