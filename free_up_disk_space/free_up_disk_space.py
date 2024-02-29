import datetime

def roundHalfUp(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.50002 if val >= 0 else -0.50002))
    return result / 10**n_digits


finalOutput = ""
TODAY = datetime.date(2019, 4, 27)

class File():
    def __init__(self, rawDate: str, rawTime: str, pm: bool, size: int, fileName: str):
        splitDate = [int(val) for val in rawDate.split("/")]
        splitTime = [int(val) for val in rawTime.split(":")]
        self.dateTime = datetime.date(splitDate[2], splitDate[1], splitDate[0])
        splitTime[0] += 12 if pm and splitTime[0] != 12 else 0
        self.pm = pm
        self.size = size
        self.fileName = fileName
        self.grade = self.calculateGrade()

    def calculateGrade(self) -> float:
        time = TODAY - self.dateTime
        day = time.days
        day -= 0.5 if self.pm else 0
        megabytes = (self.size/1000)
        grade = day * megabytes
        return grade


n_cases = int(input())
for _ in range(n_cases):
    files: list[File] = []
    # GET INPUTS =======================================================================================|
    line = input().rstrip()
    fileCount, driveSize = [float(val) for val in line.split(" ")]
    fileCount = int(fileCount)
    for i in range(fileCount):
        line = input().rstrip()
        date, time, dayHalf, size, file = [val for val in line.split(" ")]
        files.append(File(date, time, dayHalf == "PM", int(size), file))

    files.sort(key=lambda x: x.grade, reverse=True)

    driveSizeKilobytes = driveSize * 1000 * 1000
    eraseSize = driveSizeKilobytes*.25

    alreadyErased = 0

    erasedFiles: list[File] = []
    erasedFiles: list[File] = []

    iterator = 0

    while alreadyErased < eraseSize:
        erasedFiles.append(files[iterator])
        alreadyErased += files[iterator].size
        iterator += 1

    for file in erasedFiles:
        finalOutput += (f"{file.fileName} {roundHalfUp(file.grade,3):.03f}\n")

print(finalOutput.strip())
