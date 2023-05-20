import os
from random import shuffle
import subprocess
import sys
from time import sleep

def baralho():
    v=0
    cards=[]
    valor=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    suit=["♥","♠","♣","♦"]
    while v<4:
        n=0
        while  n<13:
            cards.append(str(valor[n]) + " " + suit[v])
            n+=1
        v+=1
        
    shuffle(cards)
    return cards

def Visual(proxcarta,layer0,layer1,layer2,layer3,layer4):
    if proxcarta[0]!="10":
        layer0.append(" ___ ")
        layer1.append(f"|{proxcarta[1]}  |")
        layer2.append(f"| {proxcarta[0]} |")
        layer3.append(f"|  {proxcarta[1]}|")
        layer4.append(" \u203e\u203e\u203e ")
    else:
        layer0.append(" ___ ")
        layer1.append(f"|{proxcarta[1]}  |")
        layer2.append(f"| {proxcarta[0]}|")
        layer3.append(f"|  {proxcarta[1]}|")
        layer4.append(" \u203e\u203e\u203e ")

def printV(visu):
    n=0
    while len(visu)-n:
        print(visu[n],end="")
        n+=1
    print("")
def cardprint(jogador):
    printV(jogador.layer0)
    printV(jogador.layer1)
    printV(jogador.layer2)
    printV(jogador.layer3)
    printV(jogador.layer4)
    
sd=dict({'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K': 10}) 

repeat="Y"   
while repeat == "Y":
    class player:
        layer0=[]
        layer1=[]
        layer2=[]
        layer3=[]
        layer4=[]
        points=0
    
    class dealer:
        layer0=[" ___ "]
        layer1=["|\\\\\\|"]
        layer2=["|\\\\\\|"]
        layer3=["|\\\\\\|"]
        layer4=[" \u203e\u203e\u203e "]
        points=0
    
    os.system('cls')  
    count=0
    i=0
    confirm="hit"
    cartas=baralho()

    proxcarta=cartas[i]
    i+=1
    proxcarta=proxcarta.split(" ")
    dealer.points+=sd[proxcarta[0]]
    Visual(proxcarta,dealer.layer0,dealer.layer1,dealer.layer2,dealer.layer3,dealer.layer4)

    while confirm=="hit":
        cardprint(dealer)
        print(f"Dealer's points: {dealer.points}")
        print("DEALER'S CARDS")
        
        print("YOUR CARDS")
        proxcarta=cartas[i]
        i+=1
        proxcarta=proxcarta.split(" ")
        if proxcarta[0]=="A":
            count+=1
        print(count)
        player.points+=sd[proxcarta[0]]
        Visual(proxcarta,player.layer0,player.layer1,player.layer2,player.layer3,player.layer4)
        cardprint(player)
                
        if player.points>21 and player.points-10*count<=21: 
           while player.points>21:
                player.points-=10
                count-=1  
            
        elif player.points>21:
            print(f"Your points: {player.points}\nBUST")
            print("\nPlay Again?(Y/N)")
            repeat=input()
            if repeat=="Y":
                subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
            else:
                sys.exit()
        print(f"Your points: {player.points}")
        confirm=input()
        os.system("cls")
            
    dealer.layer0=[]
    dealer.layer1=[]
    dealer.layer2=[]
    dealer.layer3=[]
    dealer.layer4=[]
    Visual(cartas[0].split(),dealer.layer0,dealer.layer1,dealer.layer2,dealer.layer3,dealer.layer4)
        
    while (dealer.points<17 and confirm!="hit") or dealer.points<player.points:
        proxcarta=cartas[i]
        i+=1
        proxcarta=proxcarta.split(" ")
        dealer.points+=sd[proxcarta[0]]
        Visual(proxcarta,dealer.layer0,dealer.layer1,dealer.layer2,dealer.layer3,dealer.layer4)
        cardprint(dealer)
        print(f"Dealer's points: {dealer.points}")
        print("DEALER'S CARDS")
        
        cardprint(player)
        print(f"Your points: {player.points}\n")
        if dealer.points<17 or dealer.points<player.points:
            sleep(1)
            os.system('cls')    

    if player.points>dealer.points or dealer.points>21:
        print("YOU WIN")
    elif player.points==dealer.points:
        print("DRAW")
    else:
        print("YOU LOSE")
    print("\nPlay Again?(Y/N)")
    repeat=input()