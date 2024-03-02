import os
from random import shuffle
import subprocess
import sys
from time import sleep


class carta:
    def __init__(self, valor, naipe):
        self.simb = valor
        
        if naipe != "hidden":
            if valor == 'A':
                self.valor = 11
            elif valor == 'J' or valor == 'Q' or valor == 'K':
                self.valor = 10
            else:
                self.valor = int(valor)
        else:
            self.valor = 0
        self.naipe = naipe
        
        self.visu0 = " ____"
        
        if naipe != "hidden":
            self.visu1 = f"|{naipe}  |"
        else:
            self.visu1 = "|\\\\\\|"
            
        if naipe != "hidden" and valor != '10':
            self.visu2 = f"| {valor} |"   
        elif naipe != "hidden":
            self.visu2 = f"| {valor}|"
        else:
            self.visu2 = "|\\\\\\|"
            
        if naipe != "hidden":
            self.visu3 = f"|  {naipe}|"
        else:
            self.visu3 = "|\\\\\\|"
            
        self.visu4 = " \u203e\u203e\u203e\u203e"
        
def baralho():
    cards=[]
    valor=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    naipe=['♥',"♠","♣","♦"]
    v=0
    
    while v <= 12:
        n = 0
        while  n <= 3:
            card = carta(valor = valor[v], naipe = naipe[n])
            cards.append(card)
            n += 1
        v += 1
        
    shuffle(cards)
    return cards

class mão:
    def __init__(self, pontos, cartas):
        self.pontos = pontos
        self.cartas = cartas
        self.count = 0
        
    def new(self,carta):
        self.cartas.append(carta)
        self.pontos += carta.valor
        if carta.simb == "A":
            self.count += 1
        
    def clear(self):
        self.cartas = []
        self.pontos = 0

def cardprint(jogador):
    for carta in jogador.cartas:
        print(carta.visu0, end = " ")
    print()
    for carta in jogador.cartas:
        print(carta.visu1, end = " ")
    print()
    for carta in jogador.cartas:
        print(carta.visu2, end = " ")
    print()
    for carta in jogador.cartas:
        print(carta.visu3, end = " ")
    print()
    for carta in jogador.cartas:
        print(carta.visu4, end = " ")
    
cartavazia = carta(naipe = "hidden", valor = 0)

print("Escreva ""hit"" para receber outra carta e qualquer outra coisa para parar\n Aperte ""Enter"" botão para continuar:")
input()
os.system("cls")

repeat="Y"   
while repeat.upper() == "Y":
    cartas = baralho()
    player = mão(pontos = 0, cartas = [])
    dealer = mão(pontos = 0, cartas = [])
    dealer.new(carta = cartavazia)
    proxcarta = cartas[0]
    player.new(proxcarta)
        
    os.system('cls')
    player.count = 0
    i=1
    confirm="hit"
    
    proxcarta=cartas[i]
    i+=1
    dealer.new(proxcarta)
    
    while confirm.lower() == "hit":
        cardprint(dealer)
        print(f"Dealer's pontos: {dealer.pontos}")
        print("DEALER'S CARDS")
        print("YOUR CARDS")
        
        proxcarta = cartas[i]
        i+=1
        player.new(proxcarta)
        cardprint(player)
        print()
    
        if player.pontos > 21 and player.pontos-10*player.count <=21: 
           while player.pontos > 21:
                player.pontos -= 10
                player.count -= 1  
            
        elif player.pontos>21:
            print(f"Your pontos: {player.pontos}\nBUST")
            print("\nPlay Again?(Y/N)")
            repeat = input().lower().strip()[0]
            if repeat=="y":
                subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

            else:
                sys.exit()
        print(f"Your pontos: {player.pontos}")
        confirm=input()
        os.system("cls")
        
    dealer.cartas = [dealer.cartas[1]]
    while (dealer.pontos<22 and confirm!="hit") or dealer.pontos < player.pontos:
        proxcarta=cartas[i]
        i+=1
        dealer.new(proxcarta)
        cardprint(dealer)
        print()
        if dealer.pontos > 21 and dealer.count > 0:
            while dealer.pontos > 21:
                dealer.pontos -= 10
                dealer.count -= 1  
                
        print(f"Dealer's pontos: {dealer.pontos}")
        print("DEALER'S CARDS")
        cardprint(player)
        print(f"Your pontos: {player.pontos}\n")
        
        if dealer.pontos < 21 or dealer.pontos < player.pontos:
            sleep(1)
            os.system('cls')    

    if player.pontos > dealer.pontos or dealer.pontos > 21:
        print("YOU WIN")
        
    else:
        print("YOU LOSE")
    print("\nPlay Again?(Y/N)")
    repeat = input().strip().lower()