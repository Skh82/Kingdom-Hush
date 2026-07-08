#import pandas as pd
#import matplotlib.pyplot as plt

class Cards:
    def __init__(self, damage):
        self.damage = damage

class Game_managment:
    players = list()

    def __init__(self, name, health, cards, score=0):
        self.name = name
        self.health = health
        self.cards = cards
        self.score = score
        Game_managment.players.append(self)

    def game_proccess(self, player):
        for ind, card in enumerate(self.cards):
            self.health -= player.cards[ind].damage
            player.health -= card.damage
            if card.damage > player.cards[ind].damage:
                self.score += 1
            else:
                player.score += 1
        a1 = f"{self.name} -> Score: {self.score}, Health: {self.health}"
        a2 = f"{player.name} -> Score: {player.score}, Health: {player.health}"
        print(a1)
        print(a2)
        mydata = (a1, a2)
        return mydata

names = input().split()
healths = (input().split())
damages = (input().split())
lst3 = list()
for _ in range(0,3):
    x = input().split()
    lst3.append(x)
try:
    healths = list(map(int,healths))
    damages = list(map(int,damages))
    [A, B, C] = list(map(Cards, damages))
    lst1 = list()
    lst2 = list()
    for x in lst3:
        lst1.append(eval(x[0]))
        lst2.append(eval(x[1]))
    player1 = Game_managment(names[0], healths[0], lst1)
    player2 = Game_managment(names[1], healths[1], lst2)
    my_data = player1.game_proccess(player2)
    #df = pd.DataFrame(my_data)
    #df.to_csv('output.txt', index=False)

except:
    print("Invalid Command.")
#import matplotlib.pyplot as plt
#fig, ax = plt.subplots()
#names = [player.name for player in Game_managment.players]
#values = [player.score for player in Game_managment.players]
#ax.bar(names, values, color='skyblue')
#plt.xlabel('Players\' Names')
#plt.ylabel('Players\' Scores')
#plt.title('Bar Chart with Names on X-axis')
#plt.grid(axis='y')
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()