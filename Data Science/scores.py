import school_scores
list_of_record = school_scores.get_all()



averages = []

for record in list_of_record:
    mathScore= record["Gender"]["Male"]["Math"]
    averages.append(mathScore)


##print(averages)
allScores = sum(averages)/len(averages)
print(allScores)
