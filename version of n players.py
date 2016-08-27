import random
        
def atack(p1,p2):
    game = Game()
    game.players_status()
    p1.h=p1.h-p2.dmg
    p1.save()
    s=''
    s=str(p2.name)+"atacked"+str(p1.name)


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

                
    def player_attack_class(self, p1,p2=None):
        if not p2:
            p2 = random.choice(self.players)
        p2.h=p2.h-p1.dmg
        p2.save()


    def players_status(self):
        for p in self.players:
            if (p.h==0) or (p.h<0):
                p.status='dead'


atack(p1,p2)
