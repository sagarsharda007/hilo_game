
'''Python code for a basic Hi-Lo game'''


from random import shuffle


def rules(action):
    print("The rules are simple\n")
    print("You will be given a random card from a standard deck\n")
    print("You then have to guess if the next caed is going to be of a higher or lower value\n")
    print("the number cards correspond to their face value\n")
    # here's some tweaks with my own set of rules
    print("card:A, holds the value 1\n")
    print("cards: J, K, Q. hold the values: 11,12,13 respectively\n")
    print("just type H or L for High or low\n")
    print("You win if you make more than 10 correct guesses\n")
    print("You lose if you make more that 10 wrong guesses\n")
    print("please note, if you make too many invalid inputs, you will lose.\n")
    print("")
    input("please enter '--resume' to resume the game")


def createDeck():
    Deck = []

    faceValues = ["A","J","K","Q"]

    for i in range(4): #4 different suits
        for card in range(2,11):
            Deck.append(str(card))
        for card in faceValues:
            Deck.append(card)
    shuffle(Deck)
    return Deck

cardDeck = createDeck()

Name = input("Hello,Please enter your name")

if Name == "--help":
    rules(Name)
else:
    print("Such a nice name you got", Name)
    print("")
    print("NOTE: Anytine during the game, enter the keyword: '--help' to read the rules")
    print("To exit anytime, enter the keyword: '--exit'")
    print("")



while(True):
    correctGuesses = 0
    wrongGuesses = 0
    invalidInputs = 0

    if len(cardDeck) < 10:
        print("Less than 10 cards remaining in the deck")
        print("To re-Shuffle, and resume: enter 'R'")
        print("Press any other key to exit")
        whatToDo = input().upper
        if whatToDo == "R":
            cardDeck = createDeck()
            continue
        else:
            break
    if correctGuesses == 10:
        print("Yay, you made 10 correct guesses, YOU WIN!!")
        replay = input("Play again? (Y/N)").upper()
        if replay == "Y":
            continue
        elif replay == "N":
            break
        else:
            print("Invalid input")
            break

    elif wrongGuesses == 10:
        print("oops, you made 10 Incorrect guesses, YOU LOSE :(")
        replay = input("Play again? (Y/N)").upper()
        if replay == "Y":
            continue
        elif replay == "N":
            break
        else:
            print("Invalid input")
            break
    elif invalidInputs == 5:
        print("oops, you made too many invalid inputs, YOU LOSE :(")
        replay = input("Play again? (Y/N)").upper()
        if replay == "Y":
            continue
        elif replay == "N":
            break
        else:
            print("Invalid input")
            break

    fCardsDict = {"A": 1, "J": 11, "Q": 12, "K": 13,}

    playerCard = cardDeck.pop()
    print("here's your card", playerCard)

    nextCard = cardDeck.pop()
    action = input("H/L").upper()

    if action == "--HELP":
        rules(action)
    if action == "H":
        if nextCard > playerCard:
            print("Yay!, You got that right.")
            print("The next card was",nextCard)
            correctGuesses += 1
        elif nextCard < playerCard:
            print("Oops!, You got that wrong")
            print("The next card was",nextCard)
            wrongGuesses += 1

    elif action == "L":
        if nextCard < playerCard:
            print("Yay!, You got that right.")
            print("The next card was",nextCard)
            correctGuesses += 1
        elif nextCard > playerCard:
            print("Oops!, You got that wrong")
            print("The next card was",nextCard)
            wrongGuesses += 1

    elif action == "--EXIT":
        break

    else:
        print("Invalid input, Please try Again")
        invalidInputs += 1
        continue
