#https://lmcodequestacademy.com/problem/make-the-grade

EXPECTED_OUTPUT = """Bob 62.5% D
Sarah 75.0% C
Kris 87.5% B"""

def round_half_away(num, decimalPoints):
    decimal = 10.0**-(decimalPoints + 1) #makes a decimal you can use to multiply/divide (IE decimalPoints = 2, decimal = 0.01 )
    roundedNum = abs(int((num/decimal) + decimal/10)) #puts digits you want to keep on the left side of the decimal (IE 1.394 = 139)
    finalDigit = roundedNum%10 #Gets the ones place
    if finalDigit >= 5:
        roundedNum += (10 - finalDigit) #rounds number up to nearest 10
    roundedNum *= decimal * (num/abs(num))#Multiplies Num back down to the right number of decimal points and makes it positive/negative
    return roundedNum

def percent_to_grade(percent):
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    else:
        return "F"

final_output = ""
cases = int(input())
for _ in range(cases):
    line = input()
    num_of_students, correct_answers = line.split(" ")
    num_of_students = int(num_of_students)
    for i in range(num_of_students):
        answered_correctly = 0
        student_name, student_answers = input().split(" ")
        for j in range(len(student_answers)):
            if student_answers[j] == correct_answers[j]:
                answered_correctly += 1

        percent_right = 100*(answered_correctly/len(correct_answers))

        final_output += f"{student_name} {round_half_away(percent_right, 1):.01f}% {percent_to_grade(percent_right)}\n"

print(final_output.strip())
