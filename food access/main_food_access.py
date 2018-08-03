import food_access
list_of_record = food_access.get_records(test=True)

lowInc = []

for people in list_of_record:
    county = people["State"]["CA"]
    lowInc.sppend(county)

print(lowInc)
