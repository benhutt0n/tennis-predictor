import math, pandas as pd

def estimateRating(rank):
    # no ranking (e.g. a wildcard nobody's heard of) -> start lowish
    if pd.isna(rank):
        return 1400
    # better rank -> higher starting rating It uses a log because the gap between no. 1 and no. 10 is huge, while the gap between no. 500 and no. 510 means almost nothing. A log squashes the big numbers together, which matches how tennis really works.
    return 2100 - 150 * math.log10(rank)


K = 32   # how fast ratings move (bigger = more jumpy)

def chanceOfWinning(winnerRating, opponentRating):
    myStrength = 10 ** (winnerRating / 400)
    opponentStrength = 10 ** (opponentRating / 400)
    return myStrength / (myStrength + opponentStrength)


def buildRatings(matches):
    # dictionary with player name and their rating
    playersRatings = {}

    # for every match in matches
    for index, row in matches.iterrows():
        winner = row["winner_name"]
        loser = row["loser_name"]

        # check both players exist already, if not add them using their ranking
        if winner not in playersRatings:
            playersRatings[winner] = estimateRating(row["winner_rank"])
        if loser not in playersRatings:
            playersRatings[loser] = estimateRating(row["loser_rank"])

        # do the percentage rating change depending on whether they should have won
        winnerChance = chanceOfWinning(playersRatings[winner], playersRatings[loser])
        change = K * (1 - winnerChance)

        # update playersRatings
        playersRatings[winner] = playersRatings[winner] + change
        playersRatings[loser] = playersRatings[loser] - change

        # do the margin of victory later

    return playersRatings