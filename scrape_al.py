from pathlib import Path
from pprint import pprint

import pandas as pd
from requests_html import HTMLSession

if __name__ == '__main__':
    DATA = Path(__file__).parent / "data"
    AL_COUNTIES = ["Autauga", "Baldwin", "Barbour", "Bibb", "Blount",
                   "Bullock", "Butler", "Calhoun", "Chambers",
                   "Cherokee", "Chilton", "Choctaw", "Clarke", "Clay",
                   "Cleburne", "Coffee", "Colbert", "Conecuh", "Coosa",
                   "Covington", "Crenshaw", "Cullman", "Dale", "Dallas",
                   "Dekalb", "Elmore", "Escambia", "Etowah", "Fayette",
                   "Franklin", "Geneva", "Greene", "Hale", "Henry", "Houston",
                   "Jackson", "Jefferson", "Lamar", "Lauerdale", "Lawrence",
                   "Lee", "Limestone", "Lowndes", "Macon", "Madison",
                   "Marengo", "Marion", "Marshall", "Mobile", "Monroe",
                   "Montgomery", "Morgan", "Perry", "Pickens", "Pike",
                   "Randolph", "Russell", "St. Clair", "Shelby", "Sumter",
                   "Talladega", "Tallapoosa", "Tuscaloosa", "Walker",
                   "Washington", "Wilcox", "Winston", ]

    url = "https://broadbandnow.com/Alabama"
    session = HTMLSession()
    response = session.get(url)
    print(response)
    response.html.render()
    broadban = []
    broadban_append = broadban.append
    for idx in range(3, len(AL_COUNTIES) + 3):
        sel = f'#svg-map > svg > path:nth-child({idx})'
        info = response.html.find(sel)
        broadban_append(info[0].attrs["fill-opacity"])

    al_broadband = dict(zip(AL_COUNTIES, broadban))
    al_df = pd.DataFrame.from_records([al_broadband])

    al_df.T.to_excel((DATA / "al_broadband.xlsx"))
