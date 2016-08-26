import random


def atack(num):
    for i in range (0,num):
        game.player_attack_class(vasya)
        game.players_status()
        game.log('log.txt')
        game.player_attack_class(kolya)
        game.players_status()
        game.log('log.txt')
        game.player_attack_class(dima)
        game.players_status()
        game.log('log.txt')

class Player:
    def __init__(self, name,strength=10,dex=10,intel=10,weapon=5,status='alive'):
        self.h = 30+7*strength
        self.name = name
        self.str=strength
        self.dmg=sself.str+weapon
        self.int=intel
        self.mp=self.int+10
        self.dext=dex
        self.status=status
        
    def save(self):
        pass
        
class Game:
    players = []
  
    def add_player(self, name):
        player = Player(name)
        self.players.append(player)
        return player


    def log(self,file_name):
        for p in self.players:
            with open(file_name, 'a') as fout:
                print(p.name,p.h,p.status, file=fout)

                
    def player_hit(self,name,dmg=50):
        for i in self.players:
            if i.name==name:
                i.h=i.h-dmg

                
    def player_attack_class(self, p1,p2=None):
        if not p2:
            p2 = random.choice(self.players)
        p2.h=p2.h-p1.dmg
        p2.save()


    def players_status(self):
        for p in self.players:
            if (p.h==0) or (p.h<0):
                p.status='dead'


game = Game()


vasya = game.add_player("Vasya")
kolya = game.add_player("Kolya")
dima = game.add_player("Dima")


game.players_status()

atack(1)

inf = [p.__dict__ for p in game.players]
print(inf)
