from itu.algs4.fundamentals.queue import Queue
import random
import time
import os

deck = []
#for i in range(4):
for i in range(2, 12):
    for j in range(4):
        if i == 10:
            for k in range(3):
                deck.append(str(i))
        if i == 11:
            deck.append("Ace")
        else:
            deck.append(str(i))

playerdeck = []
playertotal = 0
housedeck = []
housetotal = 0
otherdeck = []
othertotal = 0

os.system('clear')

def UI(playerdeck, housedeck, otherdeck,  deck):
    os.system('clear')
    print("Blackjack odds calculator")
    print("Player deck  :   {p}".format(p=playerdeck))
    print("House deck   :   {p}".format(p=housedeck))
    print("Other deck  :   {d}".format(d=otherdeck))
    print("Deck Cards   :   {d}".format(d=len(deck)))
    print("Deposit key  :   'p' = player, 'h' = house, 'o' = other, 'c' = cancel, 'r' = restart")
    print("Player odds  :   {b}% bust, {c}% blackjack, {d}% house".format(b=bustodds(deck, playerdeck), c=blackodds(deck, playerdeck), d=houseodds(deck, playerdeck, housedeck)))
    print("House odds   :   {b}% bust, {c}% blackjack".format(b=bustodds(deck, housedeck), c=blackodds(deck, housedeck)))
    print("Other odds   :   {b}% bust, {c}% blackjack, {d}% house".format(b=bustodds(deck, otherdeck), c=blackodds(deck, otherdeck), d=houseodds(deck, otherdeck, housedeck)))

def bustodds(deck, deck2):
    total1 = 0
    total2 = 0
    for i in deck2:
        if i == "Ace":
            total1 += 1
            total2 += 11
        elif int(i) < 12:
            total1 += int(i)
            total2 += int(i)
    fucks1 = 0
    fucks2 = 0
    for i in deck:
        if i == "Ace":
            if 1 + int(total1) > 21:
                fucks1 += 1
            if 1 + int(total2) > 21:
                fucks2 += 1
        else:
            if int(i) + int(total1) > 21:
                fucks1 += 1
            if int(i) + int(total2) > 21:
                fucks2 += 1
    if fucks1 < fucks2:
        chance = 100 * (int(fucks1) / len(deck))
        return round(chance, 2)
    else:
        chance = 100 * (int(fucks2) / len(deck))
        return round(chance, 2)

def houseodds(deck, deck2, housed):
    total1 = 0
    total2 = 0
    housetotal1 = 0
    housetotal2 = 0
    for i in deck2:
        if i == "Ace":
            total1 += 1
            total2 += 11
            housetotal1 += 1
            housetotal2 += 11
        elif int(i) < 12:
            total1 += int(i)
            total2 += int(i)
    for i in housed:
        if i == "Ace":
            housetotal1 += 1
            housetotal2 += 11
        elif int(i) < 12:
            housetotal1 += int(i)
            housetotal2 += int(i)
    newtot = 0
    if total2 > total1 and total2 < 22:
        newtot = total2
    else:
        newtot = total1
    fucks1 = 0
    fucks2 = 0
    for i in deck:
        if i == "Ace":
            if (11 + int(housetotal1) > int(newtot)) and (11 + int(housetotal1) < 22) or (1 + int(housetotal1) > int(newtot)) and (1 + int(housetotal1) < 22):
                fucks1 += 1
            if (11 + int(housetotal2) > int(newtot)) and (11 + int(housetotal2) < 22) or (1 + int(housetotal2) > int(newtot)) and (1 + int(housetotal2) < 22):
                fucks2 += 1
        else:
            if (int(i) + int(housetotal1) > int(newtot)) and (int(i) + int(housetotal1 < 22)):
                fucks1 += 1
            if (int(i) + int(housetotal2) > int(newtot)) and (int(i) + int(housetotal2 < 22)):
                fucks2 += 1

    if fucks1 < fucks2:
        chance = 100 * (int(fucks2) / len(deck))
        return round(chance, 2)
    else:
        chance = 100 * (int(fucks1) / len(deck))
        return round(chance, 2)

    for i in deck:
        if i == "Ace":
            if 1 + int(total1) > 21:
                fucks1 += 1
            if 1 + int(total2) > 21:
                fucks2 += 1
        else:
            if int(i) + int(total1) > 21:
                fucks1 += 1
            if int(i) + int(total2) > 21:
                fucks2 += 1
    if fucks1 < fucks2:
        chance = 100 * (int(fucks1) / len(deck))
        return round(chance, 2)
    else:
        chance = 100 * (int(fucks2) / len(deck))
        return round(chance, 2)

def blackodds(deck, deck2):
    total1 = 0
    total2 = 0
    for i in deck2:
        if i == "Ace":
            total1 += 1
            total2 += 11
        elif int(i) < 12:
            total1 += int(i)
            total2 += int(i)
    fucks1 = 0
    fucks2 = 0
    for i in deck:
        if i == "Ace":
            if 1 + int(total1) == 21:
                fucks1 += 1
            if 11 + int(total2) == 21:
                fucks2 += 1
        else:
            if int(i) + int(total1) == 21:
                fucks1 += 1
            if int(i) + int(total2) == 21:
                fucks2 += 1
    if fucks1 < fucks2:
        chance = 100 * (int(fucks2) / len(deck))
        return round(chance, 2)
    else:
        chance = 100 * (int(fucks1) / len(deck))
        return round(chance, 2)

over = False

while over == False:
    UI(playerdeck, housedeck, otherdeck, deck)
    print("Please choose a deposit key")
    deposit = input()
    if deposit == "p":
        depositing = True
        while depositing == True:
            number = input()
            if str(number) == "c":
                depositing = False
            elif str(number) in deck:
                deck.remove(str(number))
                playerdeck.append(str(number))
                UI(playerdeck, housedeck, otherdeck, deck)
    if deposit == "h":
        depositing = True
        while depositing == True:
            number = input()
            if number == "c":
                depositing = False
            elif str(number) in deck:
                deck.remove(str(number))
                housedeck.append(str(number))
                UI(playerdeck, housedeck, otherdeck, deck)
    if deposit == "o":
        depositing = True
        while depositing == True:
            number = input()
            if number == "c":
                depositing = False
            elif str(number) in deck:
                deck.remove(str(number))
                otherdeck.append(str(number))
                UI(playerdeck, housedeck, otherdeck, deck)
    if deposit == "r":
        os.exec*()
