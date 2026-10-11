from pathlib import Path
import pandas as pd

rawFolder = Path(__file__).resolve().parent.parent / "data" / "raw"

def loadMatches(startYear=2000, endYear=2026):

    allYears = []

    for year in range (startYear, endYear+1):
        
        filePath = rawFolder / ("atp_matches_" + str(year) + ".csv")
        yearTable = pd.read_csv(filePath)
        allYears.append(yearTable)

    # all years into one big table
    matches = pd.concat(allYears)

    matches["tourney_date"] = pd.to_datetime(matches["tourney_date"].astype(str), format="%Y%m%d")

    matches = matches.sort_values(["tourney_date", "match_num"])

    matches = matches.reset_index(drop=True)

    return matches


def cleanData():
    matches = loadMatches()
    requiredColumns = ["winner_id", "loser_id", "winner_ht", "loser_ht", "winner_age", "loser_age", "winner_rank", "loser_rank", "winner_rank_points", "loser_rank_points", "surface", "w_ace", "w_df", "w_svpt", "w_1stIn", "w_1stWon", "w_2ndWon", "w_SvGms", "w_bpSaved", "w_bpFaced", "l_ace", "l_df", "l_svpt", "l_1stIn", "l_1stWon", "l_2ndWon", "l_SvGms", "l_bpSaved", "l_bpFaced",]

    # throw away any match missing one of those
    cleanMatches = matches.dropna(subset=requiredColumns)

    # renumber the rows again
    cleanMatches = cleanMatches.reset_index(drop=True)

    return cleanMatches