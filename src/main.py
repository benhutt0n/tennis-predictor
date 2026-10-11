from data import loadMatches, cleanData

matches = loadMatches()
cleanMatches = cleanData()

print("All matches:", len(matches))
print("Clean matches:", len(cleanMatches))
print(cleanMatches.head())