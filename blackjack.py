"""
This script implements a simple game of blackjack player against the computer (dealer)
"""

import random

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

#Define deck and hands
deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
dealer_hand = []
player_hand = []

#Draws and removes a card from the deck
def draw():
    card = deck[(random.randint(0,len(deck)-1))]
    deck.remove(card)
    return card

#Deals two cards
def deal():
    hand = [draw(),draw()]
    return hand

#Gets score of a hand
def adder(list):
    total = 0
    for item in list:
        total = total + int(item)
    return total

#Determines winning hands
def compare(player_hand,dealer_hand):
    player_score = adder(player_hand)
    dealer_score = adder(dealer_hand)
    if player_score > 21:
        if dealer_score > 21:
            return "You both busted"
    if player_score > 21:
        if dealer_score < 21:
            return "You busted, dealer wins"
    if dealer_score > 21:
        if player_score > 21:
            return "You both busted"
    if dealer_score > 21:
        if player_score < 21:
            return "Dealer busted, you win!"
    if player_score == 21:
        if dealer_score != 21:
            return "Blackjack, you win!!!"
    if dealer_score > player_score:
        return "Dealer Wins"
    if player_score > dealer_score:
        return "You win!!!"
    if dealer_score == player_score:
            return "It's a draw"

#Main gameplay script
def gameplay():
    print(logo)
    def hit(player_hand,dealer_hand):
        player_score = adder(player_hand)
        dealer_score = adder(dealer_hand)
        print(f"You current total is {player_score}")
        hitorstay = input("Do you want to hit or stay? Type hit or stay\n")
        if hitorstay.lower() == "hit":
            newcard = draw()
            player_hand.append(newcard)
            player_score = player_score + newcard
            print()
            print(f"OK, you got a {newcard}")
            if player_score > 21:
                for item in player_hand:
                    if item == 11:
                        item = 1
            if player_score > 21:
                print("You busted!")
                newgame = input("Do you want to play again? Type y or n\n")
                print()
                if newgame.lower() == "y":
                    gameplay()
                if newgame.lower() == "n":
                    print("OK, thanks for playing blackjack")
            if player_score == 21:
                print("Blackjack!")
                newgame = input("Do you want to play again? Type y or n\n")
                print()
                if newgame.lower() == "y":
                    gameplay()
                if newgame.lower() == "n":
                    print("OK, thanks for playing blackjack")
            if player_score < 21:
                hit(player_hand,dealer_hand)
        if hitorstay.lower() == "stay":
            while dealer_score < 17:
                dealercard = draw()
                dealer_hand.append(dealercard)
                dealer_score = dealer_score + dealercard
                if dealer_score > 21:
                    for item in dealer_hand:
                        if item == 11:
                            item = 1
            print(f"Dealer gets {dealer_score}")
            print()
            print(compare(player_hand,dealer_hand))
            print()
            newgame = input("Do you want to play again? Type y or n\n")
            print()
            if newgame.lower() == "y":
                gameplay()
            if newgame.lower() == "n":
                print("OK, thanks for playing blackjack")

    player_hand = deal()
    dealer_hand = deal()
    player_card_one = player_hand[0]
    player_card_two = player_hand[1]
    dealer_card_one = dealer_hand[0]
    print(f"You have a {player_card_one} and a {player_card_two}. The dealer has a {dealer_card_one} showing.")
    print()
    hit(player_hand,dealer_hand)

gameplay()

