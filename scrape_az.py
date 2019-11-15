from pathlib import Path
from pprint import pprint

import pandas as pd
from requests_html import HTMLSession

if __name__ == '__main__':
    DATA = Path(__file__).parent / "data"
    AZ_COUNTIES = ["Apache", "Cochise", "Coconino", "Gila", "Graham",
                   "Greenlee", "La Paz", "Maricopa", "Mohave", "Navajo",
                   "Pima", "Pinal", "Santa Cruz", "Yavapai", "Yuma", ]

    url = "https://broadbandnow.com/Arizona"
    session = HTMLSession()
    response = session.get(url)
    print(response)
    response.html.render()
    broadban = []
    broadban_append = broadban.append
    for idx in range(3, len(AZ_COUNTIES) + 3):
        sel = f'#svg-map > svg > path:nth-child({idx})'
        info = response.html.find(sel)
        broadban_append(info[0].attrs["fill-opacity"])

    az_broadband = dict(zip(AZ_COUNTIES, broadban))
    az_df = pd.DataFrame.from_records([az_broadband])

    az_df.T.to_excel((DATA / "az_broadband.xlsx"))
