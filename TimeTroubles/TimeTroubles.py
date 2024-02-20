testCases = int(input())
finalOutput = ""

monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for case in range(testCases):
    line = input().rstrip()


    # change this line as needed:
    month, day, line = [val for val in line.split("/")]
    year, line, offset = line.split(" ")
    hour, minute = line.split(":")
    month, day, year, hour, minute = [int(val) for val in [month, day, year, hour, minute]]
    offset = float(offset)

    minute -= int(offset * 60)
    hour += minute//60
    minute = (minute%60)
    if hour > 23:
        day += 1
        hour -= 24
    elif hour < 0:
        hour += 24
        day -= 1
        
    if year % 4 == 0:
        monthLengths[1] = 29

        month -= 1
        day = monthLengths[month - 1]
    elif day > monthLengths[month - 1]:
        month += 1
        day = 1
    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        if day < 1:
            month = 1
            year += 1
    finalOutput += f"{month:0>2}/{day:0>2}/{year:0>4} {hour:0>2}:{minute:0>2}\n"
print(finalOutput.rstrip())