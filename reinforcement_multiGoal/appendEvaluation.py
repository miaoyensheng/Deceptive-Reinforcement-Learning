currentResults = open("evaluation.txt", "r")
overallResults = open("overallResults.txt", "a")

overallResults.write("\n")

for i in currentResults:
    overallResults.write(i)

currentResults.close()
overallResults.close()