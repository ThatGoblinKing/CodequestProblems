#https://lmcodequestacademy.com/problem/get-out-the-vote

from string import ascii_uppercase


def RoundHalfAway(num, decimalPoints):
    decimal = 10.0**-(decimalPoints + 1) #makes a decimal you can use to multiply/divide (IE decimalPoints = 2, decimal = 0.01 )
    roundedNum = abs(int((num/decimal) + decimal/10)) #puts digits you want to keep on the left side of the decimal (IE 1.394 = 139)
    finalDigit = roundedNum%10 #Gets the ones place
    if finalDigit >= 5:
        roundedNum += (10 - finalDigit) #rounds number up to nearest 10
    roundedNum *= decimal * (num/abs(num))#Multiplies Num back down to the right number of decimal points and makes it positive/negative
    return roundedNum

def countVotes(ballots, candidates, tallies = 1):

    for vote in ballots:
        candidates[vote[0]] += 1
    if max(candidates.values()) > (len(ballots) // 2):
        return candidates, tallies
    else:
        shortenedBallots = []
        lastPlaceChar = min(candidates, key=candidates.get)
        for vote in ballots:
            shortenedBallots.append(vote.replace(lastPlaceChar, ""))
        candidates.pop(lastPlaceChar)
        return countVotes(shortenedBallots, {key :0 for key in candidates.keys()}, tallies + 1)

cases = int(input())
for _ in range(cases):
    line = input()
    ballots, candidates = (int(val) for val in line.split(" "))
    winnerDeclared = False
    castedVotes = []

    candidates = {ascii_uppercase[i]: 0 for i in range(candidates)}

    for i in range(ballots):
        castedVotes.append(input())
    finalVotes, tallies = countVotes(castedVotes, candidates)
    winner = max(finalVotes, key=finalVotes.get)
    print(f"Candidate {winner} won with {RoundHalfAway(max(finalVotes.values())/sum(finalVotes.values()) * 100, 1):.01f}% of the vote after {tallies} tallies")
