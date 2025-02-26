testCases = int(input())
finalOutput = ""

EXPECTED_OUTPUT = "Player Score: 21 Dealer Score: 21 Tie!\nPlayer Score: 25 Dealer Score: 18 Dealer Wins!\nPlayer Score: 17 Dealer Score: 26 Player Wins!"
OUTCOME = ["Player Wins!", "Dealer Wins!", "Tie!"]
PLAYER, DEALER, TIE = (0, 1, 2)

for case in range(testCases):

# READ INPUTS ====================================================================================||

    line1 = input().rstrip()
    line2 = input().rstrip()

    # Splits line into a list of cards, then ignores everything after the first "_" b/c suit doesn't matter
    playerCards = [val[:val.find("_")] for val in line1.split(" ")]
    dealerCards = [val[:val.find("_")] for val in line2.split(" ")]

    playerScore, dealerScore = (0, 0)


# TURN CARDS INTO NUMBERS ========================================================================||

    for card in playerCards:
        if card.isdecimal():  # Checks if card is a face card (all letters) or not (all numbers)
            playerScore += int(card)
        elif card == "ACE":
            playerScore += 1 if (playerScore + 11) > 21 else 11
            # An ace is worth 11, unless an 11 would cause the player to bust, in which case it's worth 1
        else:
            playerScore += 10
            # Every face card (other than ace) is worth 10

    for card in dealerCards:
        if card.isdecimal():  # Checks if card is a face card (all letters) or not (all numbers)
            dealerScore += int(card)
        elif card == "ACE":
            dealerScore += 1 if (dealerScore + 11) > 21 else 11
            # An ace is worth 11, unless an 11 would cause the dealer to bust, in which case it's worth 1
        else:
            dealerScore += 10
            # Every face card (other than ace) is worth 10


# DECIDE OUTCOME =================================================================================||

    busted = [playerScore > 21, dealerScore > 21]
    
    if playerScore == 21 and not dealerScore == 21: #score greater than dealer 
        winner = PLAYER
    elif busted[DEALER] and not busted[PLAYER]:
        winner = PLAYER
    elif busted[PLAYER]:
        winner = DEALER
    elif busted[PLAYER] and busted[DEALER]:
        winner = DEALER
    elif playerScore == dealerScore:
        winner = TIE
    else:
        winner = PLAYER if playerScore > dealerScore else DEALER


# OUTPUT =========================================================================================||

    finalOutput += f"Player Score: {playerScore} Dealer Score: {dealerScore} {OUTCOME[winner]}\n"
#End of loop
print(finalOutput.strip())