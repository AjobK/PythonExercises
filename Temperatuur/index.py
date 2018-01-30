tempweek = {}
total = 0
tempweek["monday"] = 10
tempweek["tuesday"] = 15
tempweek["wednesday"] = 20
tempweek["thursday"] = 23
tempweek["friday"] = 25
tempweek["saturday"] = 27
tempweek["sunday"] = 30

for day in tempweek:
    total += tempweek[day]

print("The average temperature per day is " + str(int(total / len(tempweek))) + " degrees.")