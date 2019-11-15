import time
from itertools import chain
from pathlib import Path
from pprint import pprint

import pandas as pd
from requests_html import HTMLSession


def scrape_broadband(state, counties):
    url = "https://broadbandnow.com/"
    state = state.title()
    url += state.replace(" ", "-")
    session = HTMLSession()
    response = session.get(url)
    print(response)
    response.html.render()
    broadban = []
    broadban_append = broadban.append
    for idx in range(3, len(counties) + 3):
        sel = sel = f'#svg-map > svg > path:nth-child({idx})'
        info = response.html.find(sel)
        broadban_append(info[0].attrs["fill-opacity"])

    return broadban


if __name__ == '__main__':
    DATA = "County data for most states before editing.xlsx"
    df = pd.read_excel(DATA, sheet_name="Master Data")
    df_slice = df[["States", "County"]]
    df_slice.set_index("States", inplace=True)

    all_broadband_data = []
    for state in df_slice.index.unique():
        print(state)
        state_data = df_slice.loc[state, :]
        state_dict = state_data.to_dict(orient="split")
        counties = list(chain.from_iterable(state_dict["data"]))
        all_broadband_data.extend(scrape_broadband(state, counties))
        time.sleep(1)

    df_slice["Percent Broadband Coverage"] = all_broadband_data
    df_slice.loc[:, ["County", "Percent Broadband Coverage"]].to_excel(
        "all_states_broadband.xlsx")
