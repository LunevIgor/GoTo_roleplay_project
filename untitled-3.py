

class Player:
    def __init__(self, name, h=200):
        self.h = h
        self.name = name

        
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
            print(p.name, p.h)
            with open(file_name, 'a') as fout:
                print(p.name,p.h, file=fout)
    def player_hit(self,name,dmg=50):
        for i in self.players:
            if i.name==name:
                i.h=i.h-dmg
    def player_attack(self,atack_name,target_name,dmg):
        for i in self.players:
            if i.name==atack_name:
                print(i.name,"attacks",target_name)
        self.player_hit(target_name,dmg)


    def load_player(self,name,h):
         for p in self.players:
             if p.name==name:
                 p.h=h
    def print_players(self):
        for p in self.players:
            print(p.name,p.h)


game = Game()

a=10
b=10
game.add_player("Vasya")
game.add_player("Kolya")


file=open('save.txt','r')
s=int(file.readline())
f=int(file.readline())
with open('save.txt','w'):
    pass


game.load_player("Vasya",s)
game.load_player("Kolya",f)
game.print_players()

game.player_attack("Vasya","Kolya",a)

game.log('log.txt')


game.player_attack("Kolya","Vasya",b)


game.log('log.txt')
game.save_stats('save.txt')
