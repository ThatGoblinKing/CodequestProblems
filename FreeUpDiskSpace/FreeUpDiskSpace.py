import datetime

finalOutput = ""
TODAY = datetime.date(2019, 4, 27)
EXPECTED_OUTPUT = "file7.mp3 36031.250\nfile6.sh 7703.125\nfile3.mov 7218.750\nfile10.jpg 7055.500\nfile4.gif 3656.250\nfile2.exe 3468.750\nfile5.doc 2234.375"

class File():
    def __init__(self, rawDate: str, rawTime: str, pm: bool, size: int, fileName: str):
        splitDate = [int(val) for val in rawDate.split("/")]
        splitTime = [int(val) for val in rawTime.split(":")]
        splitTime[0] += 12 if pm and splitTime[0] != 12 else 0
        self.pm = pm
        self.dateTime = datetime.date(splitDate[2], splitDate[1], splitDate[0])
        self.size = size
        self.fileName = fileName
        self.calculateGrade()

    def calculateGrade(self) -> int:
        time = TODAY - self.dateTime
        day = time.days
        day -= 0.5 if self.pm else 0
        megabytes = (self.size/1000)
        self.grade = day * megabytes


n_cases = int(input())
for _ in range(n_cases):
    files = []
    line = input().rstrip()
    fileCount, driveSize = [float(val) for val in line.split(" ")]
    fileCount = int(fileCount)
    for i in range(fileCount):
        line = input().rstrip()
        date, time, dayHalf, size, file = [val for val in line.split(" ")]
        files.append(File(date, time, dayHalf == "PM", int(size), file))

    files.sort(key=lambda x: x.grade, reverse=True)

    driveSizeKilobytes = driveSize * 1000 * 1000
    eraseSize = driveSizeKilobytes/4

    alreadyErased = 0 

    erasedFiles = []

    for file in files:
        if alreadyErased >= eraseSize:
            break
        else:
            erasedFiles.append(file)
            alreadyErased += file.size

    for file in erasedFiles:
        finalOutput += (f"{file.fileName} {file.grade:.03f}\n")

print(finalOutput.strip()) 