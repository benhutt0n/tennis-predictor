from pathlib import Path
from urllib.request import urlretrieve

mainDataUrl = "https://raw.githubusercontent.com/Aneeshers/tennis-sackmann-archive/main/atp"
rawFolder = Path(__file__).resolve().parent.parent / "data" / "raw"

for year in range(2000, 2027):
    # for every year on the github page download each file into the raw folder
    urlretrieve(f"{mainDataUrl}/atp_matches_{year}.csv", rawFolder / f"atp_matches_{year}.csv")
    urlretrieve(f"{mainDataUrl}/matches_data_dictionary.txt", rawFolder / "matches_data_dictionary.txt")