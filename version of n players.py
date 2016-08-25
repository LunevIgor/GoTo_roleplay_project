import random


def atack(num):
    for i in range (0,num):
        game.player_attack("Vasya")
        game.players_status()
        game.log('log.txt')
        game.player_attack("Kolya")
        game.players_status()
        game.log('log.txt')
        game.player_attack("Dima")
        game.players_status()
        game.log('log.txt')

class Player:
    def __init__(self, name,strength=10,dex=10,intel=10,weapon=5,status='alive'):
        self.h = 30+7*strength
        self.name = name
        self.str=strength
        self.dmg=self.str+weapon
        self.int=intel
        self.mp=self.int+10
        self.dext=dex
        self.status=status
        
class Game:
    players = []
  
    def add_player(self, name):
        player = Player(name)
        self.players.append(player)


    def save_stats(self,file_name):
        for p in self.players:
            with open(file_name, 'a') as fout:
                print(p.h, file=fout)


    def log(self,file_name):
        for p in self.players:
            print(p.name, p.h,p.status)
            with open(file_name, 'a') as fout:
                print(p.name,p.h,p.status, file=fout)

                
    def player_hit(self,name,dmg=50):
        for i in self.players:
            if i.name==name:
                i.h=i.h-dmg

                
    def player_attack(self,attack_name,target_name=''):
        for i in self.players:
            if i.name==attack_name:
                target_name=random.choice(self.players).name
                print(i.name,"attacks",target_name)
                b=[1,2]
                a=random.choice(b)
                if a==1:
                    dmg=i.dmg
                else:
                    dmg=i.dmg
                    self.power_strike(i,dmg)
        self.player_hit(target_name,dmg)


    def load_player(self,name,h):
         for p in self.players:
             if p.name==name:
                 p.h=h
    def print_players(self):
        for p in self.players:
            if p.status=='dead':
                print(p.name,p.status)
            else:
                print(p.name,p.h,p.status)
    def players_status(self):
        for p in self.players:
            if (p.h==0) or (p.h<0):
                p.status='dead'


    def power_strike(self,i,dmg):
        dmg=3*i.str+dmg-25
        return(dmg)



game = Game()


game.add_player("Vasya")
game.add_player("Kolya")
game.add_player("Dima")


file=open('save.txt','r')
s=int(file.readline())
f=int(file.readline())
l=int(file.readline())
with open('save.txt','w'):
    pass


game.load_player("Vasya",s)
game.load_player("Kolya",f)
game.load_player("Dima",l)
game.print_players()
game.players_status()

atack(10)


game.save_stats('save.txt')
