import random

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
NCARDS = 8


def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard


def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut


print('Welcome to Higher or Lower\nYou have to choose weather the next card to be shown will be higher or lower.')
print('If you make your guess correct, you will gain 20 point, and if it is wrong, \n you will lose 15 points')

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):  # thisValue represent the index
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

current_score = 50
while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print(f'starting card is {currentCardRank} of {currentCardSuit}')
    print()
    # step 3
    for cardNumber in range(0, NCARDS):
        answer = input('will be the next card higher? enter (h for higher and l for lower): ')
        answer = answer.casefold()
        # step 4
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print(f'Next card is: {nextCardRank} of {nextCardSuit}')
        # step 5
        if answer == 'h':
            if nextCardValue > currentCardValue:
                print(f'You got 20 points.')
                current_score += 20
            else:
                print('Sorry, It was not higher')
                current_score -= 15
        elif answer == 'l':
            if nextCardValue > currentCardValue:
                print(f'You got it right, It was lower')
                current_score += 20
                print(f'Your score is {current_score}')
            else:
                current_score -= 15
                print(f'Sorry it was not lower')
                currentCardRank = nextCardRank
                currentCardValue = nextCardValue
    goAgain = input('To play again, press Enter or "q" to quit: ')

    print(f'\nYour total score is {current_score}')
    if goAgain == 'q':
        break
        print('Good Bye')
