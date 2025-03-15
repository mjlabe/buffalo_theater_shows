import streamlit as st
import pandas as pd

from


for site in settings.sites:
    st.write(site["theater_name"])
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))

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

# Original data
r = {"showNames":["Tarzan","Out of Eden - Tribute to The Eagles","An Evening With The Stars","The Ultimate Tribute to the Bee Gees","Kinky Boots","100th Birthday Event - Throughout the Decades"],"dates":["Mar 15, 2025 - Mar 16, 2025","Saturday, March 29, 2025","Saturday, April 5, 2025","Saturday, April 26, 2025","Jul 10, 2025 - Jul 20, 2025","Friday, July 18, 2025"],"times":["7:30 PM EDT","7:30 PM EDT","7:30 PM EDT","7:30 PM EDT","7:00 PM EDT"],"pictures":[]}

# Normalize the arrays
r = normalize_array_lengths(r, fill_value="TBD")  # Using "TBD" as fill value for missing data

# Convert to DataFrame if needed
df = pd.DataFrame(r)