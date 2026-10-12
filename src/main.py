from data import loadMatches, cleanData
from ratings import buildRatings


matches = loadMatches()
cleanMatches = cleanData()

print("All matches:", len(matches))
print("Clean matches:", len(cleanMatches))

# build everyone's rating by going through every match
playersRatings = buildRatings(matches)

# sort names from highest rating to lowest
sortedNames = sorted(playersRatings, key=playersRatings.get, reverse=True)

# print the top 10
print("Top 10 by rating:")
for name in sortedNames[:10]:
    print(name, round(playersRatings[name]))