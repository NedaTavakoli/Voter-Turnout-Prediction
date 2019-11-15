from pathlib import Path
from pprint import pprint

import pandas as pd
from requests_html import HTMLSession

if __name__ == '__main__':
    DATA = Path(__file__).parent / "data"
    CA_COUNTIES = ["Alameda", "Alpine", "Amador", "Butte", "Calaveras",
                   "Colusa", "Contra Costa", "Del Norte", "El Dorado",
                   "Fresno", "Glenn", "Humboldt", "Imperial", "Inyo", "Kern",
                   "Kings", "Lake", "Lassen", "Los Angeles", "Madera",
                   "Marin", "Mariposa", "Mendocino", "Merced", "Modoc",
                   "Mono", "Monterey", "Napa", "Nevada", "Orange", "Placer",
                   "Plumas", "Riverside", "Sacramento", "San Benito",
                   "San Bernadino", "San Diego", "San francisco", "San Joaquin",
                   "San Luis Obispo", "San Mateo", "Santa Barbara",
                   "Santa Clara", "Santa Cruz", "Shasta", "Sierra",
                   "Siskiyou", "Solano", "Sonoma", "Stanislaus", "Sutter",
                   "Tehama", "Trinity", "Tulare", "Tuolumne", "Ventura",
                   "Yolo", "Yuba"]

    url = "https://broadbandnow.com/California"
    session = HTMLSession()
    response = session.get(url)
    print(response)
    response.html.render()
    broadban = []
    broadban_append = broadban.append
    for idx in range(3, len(CA_COUNTIES) + 3):
        sel = f'#svg-map > svg > path:nth-child({idx})'
        info = response.html.find(sel)
        broadban_append(info[0].attrs["fill-opacity"])

    ca_broadband = dict(zip(CA_COUNTIES, broadban))
    ca_df = pd.DataFrame.from_records([ca_broadband])

    ca_df.T.to_excel((DATA / "ca_broadband.xlsx"))
