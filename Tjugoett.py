import os
from Tjugoett_class import CardDeck


def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def displayHand(hand):
    rows = ['', '', '', '']
    for card in hand:
        value = card['Value']
        suit = card['Suit']
        rows[1] += '|{} | '.format(value.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(value.rjust(2, '_'))
    for row in rows:
        print(row)


def playRound(deck):
    deck.shuffle()
    playerHand = [deck.draw_card()]
    dealerHand = [deck.draw_card()]
    playerTurn = True
    playerPoint = 0
    dealerPoint = 0
    

    while True:
        clearScreen()
        print('-' * 30)
        print("Player's Hand:")
        displayHand(playerHand)
        playerPoint = deck.calculate_points(playerHand)
        print("Total player score:", playerPoint)
        print('-' * 5)
        print("Dealer's Hand:")
        displayHand(dealerHand)
        dealerPoint = deck.calculate_points(dealerHand,)
        print("Total dealer score:", dealerPoint)
        print("-" * 5)

        if playerTurn:
            newCard = input("Do you want a new card? Y/N\n> ").lower()

            if newCard == "n":
                if any(card['Value'] == 'A' for card in playerHand):
                    valueChoice = input("Should ace resemble \"1\" or \"14\": ")
                    if valueChoice == "14":
                        playerPoint += 13
                        #få utskrift av sammanlagda poäng av ess
                        print(f"Player hand: {playerPoint}")
                    else:
                        # få utskrift av sammanlagda poäng av ess

                        print(f"Player hand is {playerHand}")
                playerTurn = False

            elif newCard == "y":
                newCard = deck.draw_card()
                playerHand.append(newCard)
                print(f"You drew: {newCard['Value']} of {newCard['Suit']}")
                displayHand(playerHand)
                playerPoint = deck.calculate_points(playerHand)
                print("Total player score:", playerPoint)
                print("-" * 5)

            if playerPoint == 21:
                print("The player has won!")
                break
            elif playerPoint > 21:
                print("You lost, and the dealer has won!")
                break

        else:
            if dealerPoint < 17:
                print("Dealer takes a new card")
                newCard = deck.draw_card()
                dealerHand.append(newCard)
                print(f"The dealer drew: {newCard['Value']} of {newCard['Suit']}")
                displayHand(dealerHand)
                dealerPoint = deck.calculate_points(dealerHand)
                print("-" * 5)
                input("Press Enter to continue...")

            elif dealerPoint == 21:
                print("The dealer has won!")
                break
            elif dealerPoint > 21:
                print("The dealer has lost!")
                break
            elif dealerPoint >= playerPoint:
                print("The dealer has won!")
                break
            elif playerPoint > dealerPoint:
                print("The player has won!")
                break
        

def playAgain():
    while True:
        play_again = input("Do you want to play again? (Y/N) > ").lower()
        try:
            if play_again == "n":
                return False
            elif play_again == "y":
                return True
        except ValueError:
            print("ERROR: Please enter y or n")


def main():
    deck = CardDeck()
    while True:
        playRound(deck)
        if not playAgain():
            break

main()
