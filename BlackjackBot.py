import random

# Start how much cash do you have

cash = 1000
MINBET = 5

# Initiate the entire deck (unshuffled)
deck = []
numDecks = 6

cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
for card in cards:
    deck.extend([card]*4*numDecks)

# Key of Values
    
values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}

# Useful Functions

# getPlayerValue Function that gets the value of a the player's hand
def getPlayerValue(hand: list):
    global playerHandValue
    playerHandValue = []
    for card in hand:
        playerHandValue.append(values[card])
    if sum(playerHandValue) > 21 and 'A' in hand:
        for i in range(len(playerHandValue)):
            if playerHandValue[i] == 11:
                playerHandValue[i] = 1
                break

        return sum(playerHandValue)
    else:
        return sum(playerHandValue)

# payout Function that pays depending out the type of win
def payout(result, bet: int):
    if result == 'BLACKJACK':
        return 5/2 * bet
    if result == 'WIN':
        return 2*bet
    if result == 'LOSE':
        return 0
    if result == 'PUSH':
        return bet

# Recursive Function that calculates the expected outcome based on the decision to hit or stand
def expectedPayout(player: list, dealer: list, nextPlayerCard, nextDealerCard):
    playerValue = getPlayerValue(player)
    possiblePlayerHitValues = [i+1 for i in range(21 - playerValue)]
    possibleBustValues = []
    if playerValue > 10:
        possibleBustValues = []
        possibleBustValues

    
    return possiblePlayerCardValues

# Shuffle the Deck
    
random.shuffle(deck)
print(deck)

# START ROUND

# Ask how much the player wants to bet

bet = 10
cash -= bet

# Deal two cards to both player and dealer

playerHand = [deck[0],deck[2]]
playerHandValue = []
dealerHand = [deck[3],deck[1]]

# Check for Blackjack

if getPlayerValue(playerHand) == 21:
    cash += payout('BLACKJACK')

print(cash)

print(expectedPayout(playerHand, dealerHand, 2, 2))
    
#Calculate average value that you will get or go through each possible card and calculate what number the player can get
# and chance the dealer will get below that number and multiply by potential winnings


