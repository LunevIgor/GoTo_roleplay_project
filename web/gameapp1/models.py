import random

from django.db import models

# Create your models here.

class Item (models.Model):
    name = models.CharField(max_length=30)
    bonus = models.IntegerField()
    modif = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Game (models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.name

    def player_attack_class(self, p1, p2):
        if not p2:
            p2 = random.choice(self.players.all())
        p2.hp = p2.hp - p1.dmg
        p2.save()
        return str(p2.name) + " is attacked by " + str(p1.name) + ": " + str(p1.dmg) + " dmg"

    def suicide (self, p1, p2=None):
        p1.hp = p1.hp - p1.hp
        return str (p1.name) + 'commited a suicide'

    def weakness (self, p1, p2):
        if not p2:
            p2 = random.choice(self.players.all())
        p2.dmg = p2.dmg - 5
        return str(p2.name) + 'is weakend by' + str (p1.name)

    def players_status(self):
            if (Player.hp==0) or (Player.hp<0):
                Player.status=0




class Player(models.Model):
    game = models.ForeignKey(Game, related_name='players')
    name = models.CharField(max_length=30)
    STATUSES = [
       (0, 'dead'),
       (1, 'alive')
    ]
    status = models.IntegerField(choices=STATUSES, default=1)
    strength = models.IntegerField (default=10)
    dex = models.IntegerField (default=10)
    intel = models.IntegerField (default=10)
    weapon = models.IntegerField (default=5)
    dmg = models.IntegerField(default= 10)
    mp = models.IntegerField(default= 10)
    hp = models.IntegerField(default= 100)
    def __str__(self):
        return self.name




