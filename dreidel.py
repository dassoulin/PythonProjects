import random
import math

class Dreideler:
    def __init__(self, name, money):
        self.name = name
        self.money = money
    def __str__(self):
        return str(self.name) + " now has " + str(self.money) + " gelt(s)."

def ante(p, pot):
    print("Antes up!")
    print(" ✡ ", end="")
    for i in range(0, len(p)):
        if p[i].money > 0:
            p[i].money -= 1
            pot += 1
        print(p[i], end=" ")
    print("")
    print(" ✪ The pot now has " + str(pot) + " gelt(s).")
    return p, pot

def roll(p, pot):
    i = random.randint(0, 3)
    if i==0:
        print(p.name + " rolled a נ; nothing happened!")
        return p, pot
    if i==1: 
        p, pot = gimmel(p, pot)
        print(p.name + " rolled a ג, taking the WHOLE POT!")
        return p, pot
    if i==2:
        p, pot = hey(p, pot)
        print(p.name + " rolled a ה, taking half of the pot!")
        return p, pot
    if i==3:
        p, pot = shin(p, pot)
        print(p.name + " rolled a ש; there goes another gelt into the pot!")
        return p, pot

def gimmel(p, pot): #player gets pot
    p.money += pot
    pot = 0
    return p, pot

def hey(p, pot): #player gets half of the pot
    p.money += math.ceil(pot/2)
    pot -= math.ceil(pot/2)
    return p, pot

def shin(p, pot): #player puts in a gelt
    if p.money > 0:
        p.money -= 1
        pot += 1
    return p, pot

def checkup(p, pot):
    print(" ✡ " + str(p))
    print(" ✪ The pot now has " + str(pot) + " gelt(s).")

def main():
    welcome = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Welcome to the Dreidel game!
    Here are the rules:
    • There can be up to 4 players, each entering with 10 gelt.
    • Whoever runs out of money is eliminated.
    • Even if a player has no gelt, he is not eliminated until he has 0 gelt at the end of his turn.
    • The last player standing wins.
    • Player1 will begin by spinning the dreidel, followed by Player2, etc..
    • Each new round, the player must put a gelt into the pot as an ante.
    • If a player has 0 gelt, then he does not put in anything.
    • If the dreidel lands on נ, nothing happens!
    • If the dreidel lands on ג, the player gets the pot!
    • If the dreidel lands on ה, the player gets half of the pot!
    • If the dreidel lands on ש, the player puts a gelt into the pot!
    • When the pot is empty or at 1 gelt, everyone must ante up again, even before a new round begins!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    print(welcome)
    Players = []
    for i in range(0, 4):
        Players += [Dreideler("Player"+str(i+1), 10)]
    pot = 0
    while (len(Players)>1):
        print("New round!")
        Players, pot = ante(Players, pot)
        playerCount = len(Players)
        for i in range(0, playerCount):
            if len(Players) != playerCount:
                i -= (playerCount-len(Players))
            Players[i], pot = roll(Players[i], pot)
            checkup(Players[i], pot)
            if pot == 0:
                Players, pot = ante(Players, pot)
            if Players[i].money <= 0:
                print(Players[i].name + " is eliminated!")
                Players.pop(i)
                i-=1
                if len(Players)==1:
                    break
    print(Players[0].name + " is the winner! Congratulations!")   
    congrats = """______________________________________________________________________________
\                ____ ,_  _ _ _   __  __  _  _ ____   __ ____                /
  \               | | /_| |/_/    , | __| | __\ | |    ,\ | |              /
    \                                                                    /
      \----------------------------------------------------------------/
      |                          ___         _|_____________________|_ |
      |  _           _   ,------|,,,|------,|   | C H A N U K A H |   ||
      | ( \___/^\___/ )  |_   =========    | \_/~~~~~~~~~~~~~~~~~~~\_/ |
      | |-------------|  |\|   § ó ò §     |                           |
      | ||,\ ,-,-,_,-||  |~    §\ > /§     |  ,*, , , , _ , , , ,      |
      | |||_||_|_|_|_||  |    __|||||__    |/~/_U_U_U_U_|_U_U_U_U_     |
      | ||  _ _,-,_,-||  |   /  \\\|//  \   (@}  \_\_\_\_|_/_/_/_/      |
      | || |=|-|=|-|=||  |  / /       \  \/ /      |_\_\|/_/_|         |
      | ||_|_|_|_|_|_||  | / /_   :    |\__/          |\|/|            |
      | ||-,_,-,,-,  ||  | \___}  :    |   |           \|/             |
      | ||=|=|=||=|_ ||  |   \____:____/   |            |              |
      | ||_|_|_||_|\\\||  |  //|   |   |\\\  |           /|\             |
      | |~~~~~~~~~~~~~|  |  ""|   |   |""  |          |/|\|            |
      /-|/~~~~~~~~~~~\|--|----|   |   |----|---------/|/|\|\-----------\\
    /                         \__/ \__/            _|  _|_  |_           \  
  /                           (__| |__)                              _  |_ \ 
/                                                                    _|_ /   \\
------------------------------------------------------------------------------
"""
    print(congrats);         

main()