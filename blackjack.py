from itu.algs4.fundamentals.queue import Queue
import random
import time
import os

os.system('clear')

# Add card choice feature
# Improve bot hand odds

deck = []

def UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips):
    print("Blackjack")
    print("Player deck  :   {p}".format(p=playerdeck))
    print("Deck total   :   {d}".format(d=playertotal))
    print("House deck   :   {p}".format(p=housedeck))
    print("Deck total   :   {d}".format(d=housetotal))
    print("Total chips  :   {c}".format(c=chips))
    print("Current bet  :   {b}".format(b=bet))
    print("Deck Cards   :   {d}".format(d=len(q)))
    print("Profit made  :   {p}%".format(p=100+(100*((int(chips) - int(OGchips))/int(OGchips)))))

for i in range(2, 12):
    for j in range(4):
        if i == 10:
            for k in range(3):
                deck.append(i)
        if i == 11:
            deck.append("Ace")
        else:
            deck.append(i)

dex = random.sample(deck, len(deck))
q = Queue()
for i in dex:
    q.enqueue(i)
print("How many chips do you want?")
OGchips = input()
chips = OGchips

playerdeck = []
housedeck = []
go = True
while int(chips) > 0 and len(deck) > 0:
    print("You have {c} chips left".format(c=chips))
    print("How much would you like to bet?")
    bet = input()
    while int(bet) > int(chips):
        print("You don't have enough for that")
        bet = input()
    playerdeck = []
    housedeck = []
    playertotal = 0
    housetotal = 0
    os.system('clear')
    UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
    p1 = q.dequeue()
    if p1 == "Ace":
        print("You drew an Ace. Do you choose 11 or 1?")
        acechoice = input()
        if acechoice == "1":
            p5 = 1
            playerdeck.append(p5)
            playertotal += 1
            os.system('clear')
            UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
        if acechoice == "11":
            p5 = 11
            playertotal += 11
            playerdeck.append(p5)
            os.system('clear')
            UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
    else:
        playerdeck.append(p1)
        playertotal += int(p1)
        os.system('clear')
        UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)

    time.sleep(1)
    p2 = q.dequeue()
    if p2 == "Ace":
        if housetotal + 11  <= 21:
            p5 = 11
            housedeck.append(p5)
            housetotal += 11
            os.system('clear')
            UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
        else:
            p5 = 1
            housedeck.append(p5)
            housetotal += p5
            os.system('clear')
            UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
    else:
        housedeck.append(p2)
        housetotal += int(p2)
        os.system('clear')
        UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)

    time.sleep(1)
    p3 = q.dequeue()
    if p3 == "Ace":
        time.sleep(1)
        print("You drew an Ace. Do you choose 11 or 1?")
        acechoice = input()
        if acechoice == "1":
            p5 = 1
            playerdeck.append(p5)
            playertotal += 1
            os.system('clear')
            UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
        if acechoice == "11":
            p5 = 11
            playerdeck.append(p5)
            playertotal += 11
            os.system('clear')
            UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
    else:
        playerdeck.append(p3)
        playertotal += int(p3)
        os.system('clear')
        UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)


    time.sleep(1)

    over = False
    while not over:
        fucks = 0
        for i in deck:
            if i == "Ace":
                if 1 + int(playertotal) > 21:
                    fucks += 1
            else:
                if int(i) + int(playertotal) > 21:
                    fucks += 1
        chance = int(fucks) / len(deck)
        print("You have a {c}% chance of going bust.".format(c=format(chance*100)))
        time.sleep(1)
        ducks = 0
        for i in deck:
            if i == "Ace":
                if (11 + int(housetotal) > int(playertotal)) and (11 + int(housetotal) < 22) or (1 + int(housetotal) > int(playertotal)) and (1 + int(housetotal) < 22):
                    ducks += 1
            else:
                if (int(i) + int(housetotal) > int(playertotal)) and (int(i) + int(housetotal < 22)):
                    ducks += 1
        bance = int(ducks) / len(deck)
        print("House has a {c}% chance of beating your hand by drawing 1 more card.".format(c=format(bance*100)))
        time.sleep(1)
        print("Do you hit (h) or stand (s)?")
        choice = input()
        if choice == "h":
            p4 = q.dequeue()
            if p4 == "Ace":
                time.sleep(1)
                print("Ace. Do you choose 11 or 1?")
                acechoice = input()
                if acechoice == 1:
                    p5 = 1
                    playerdeck.append(p5)
                    playertotal += int(p5)
                    os.system('clear')
                    UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
                if acechoice == 11:
                    p5 = 11
                    playerdeck.append(p5)
                    playertotal += int(p5)
                    os.system('clear')
                    UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
            else:
                playerdeck.append(p4)
                playertotal += int(p4)
                os.system('clear')
                UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)

            if playertotal > 21:
                print("You lost {b} chips".format(b=bet))
                over = True
                chips = int(chips) - int(bet)
        if choice == "s":
            while housetotal < playertotal:
                p4 = q.dequeue()
                if p4 == "Ace":
                    acechoice = input()
                    if housetotal + 11  <= 21:
                        p5 = 11
                        housedeck.append(p5)
                        housetotal += int(p5)
                        os.system('clear')
                        UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
                    else:
                        p5 = 1
                        housedeck.append(p5)
                        housetotal += int(p5)
                        os.system('clear')
                        UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
                else:
                    housedeck.append(p4)
                    housetotal += int(p4)
                    os.system('clear')
                    UI(playerdeck, chips, bet, housedeck, playertotal, housetotal, q, OGchips)
            if housetotal > playertotal and housetotal <= 21:
                print("You lost {b} chips.".format(b=bet))
                over = True
                chips = int(chips) - int(bet)
            if housetotal == playertotal:
                print("Issa draw!!")
                over = True
                chips = int(chips)
            if housetotal > 21:
                print("You won {b} chips!".format(b=bet))
                over = True
                chips = int(chips) + int(bet)
time.sleep(1)
if len(deck) == 0:
    print("You managed to play all cards without going bust!")
if chips < 1:
    print("You ran out of money thumbass")
