from typing import List

import streamlit as st
import pandas as pd

import settings

from scraper import Scraper

scraper = Scraper(
    config=settings.graph_config
)


def normalize_array_lengths(data_dict, fill_value=None):
    """
    Normalize all arrays in a dictionary to have the same length as the longest array.
    Args:
        data_dict (dict): Dictionary containing arrays
        fill_value: Value to use for padding shorter arrays (default: None)
    Returns:
        dict: New dictionary with normalized array lengths
    """
    # Find the maximum length among all arrays
    max_length = max(len(arr) for arr in data_dict.values())

    # Create a new dictionary with padded arrays
    normalized = {}
    for key, arr in data_dict.items():
        # Convert to list if it's not already
        arr_list = list(arr)
        # Pad with fill_value if array is shorter than max_length
        if len(arr_list) < max_length:
            arr_list.extend([fill_value] * (max_length - len(arr_list)))
        normalized[key] = arr_list

    return normalized


@st.cache_data(ttl=60*60*24)    # ttl 24 hrs
def get_shows(site) -> List[dict]:
    shows = "Error"
    try:
        shows = scraper.scrape(source=site["scrape_url"], prompt=site["scrape_prompt"])
        if len(shows["content"]) < 1:
            st.cache_data.clear()
        return shows["content"]
    except Exception as error:
        print(error, shows)
        raise


def main():
    st.set_page_config(layout="wide")

    for site in settings.sites:
        theater_link = f"[{site["theater_name"]}](%s)" % site['theater_url']
        st.image(site["theater_logo_url"], width=150)
        st.write(theater_link)
        try:
            shows = get_shows(site)
            print(shows)
            df = pd.DataFrame(shows)
            df.columns = ['Show', 'Date(s)', 'Description', ]
            st.write(df.set_index(df.columns[0]))
        except Exception as e:
            st.write(
                f"Hmmm... We can't seem to get the shows right now. Check out {theater_link} to see what they have."
            )


main()