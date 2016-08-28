from django.contrib import admin

from .models import Item, Game, Player

# Register your models here.

admin.site.register(Item)
admin.site.register(Game)
admin.site.register(Player)
