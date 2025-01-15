def round_half_away(num, decimalPoints):
    decimal = 10.0**-(decimalPoints + 1) #makes a decimal you can use to multiply/divide (IE decimalPoints = 2, decimal = 0.01 )
    roundedNum = abs(int((num/decimal) + decimal/10)) #puts digits you want to keep on the left side of the decimal (IE 1.394 = 139)
    finalDigit = roundedNum%10 #Gets the ones place
    if finalDigit >= 5:
        roundedNum += (10 - finalDigit) #rounds number up to nearest 10
    roundedNum *= decimal * (num/abs(num))#Multiplies Num back down to the right number of decimal points and makes it positive/negative
    return roundedNum

# num = float(input("Number: "))
#
# while num != 0:
#     decimal = int(input("Decimal: "))
#     print(f"Rounded: {RoundHalfAway(num, decimal):.0{decimal}f}")
#     num = float(input("Number: "))