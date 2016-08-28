from django.forms import model_to_dict
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Item, Game, Player


def api_get_items(request):
    data_Item = list(Item.objects.all().values())
    return JsonResponse({'data' : data_Item})


@csrf_exempt
def api_user_command(request):
    id = request.session['id']  # player id
    p1 = Player.objects.get(pk=id)
    target_id = request.POST['target_id']
    p2 = Player.objects.get(pk=target_id)
    ACTIONS = {
        'fit3': p1.game.player_attack_class,
        'fit2': p1.game.suicide,
        'fit1': p1.game.weakness
        }
    action =  request.POST['action_id']
    ans = ACTIONS[action](p1, p2)
    #ans = Player.game.player_attack_class(p1, p2)
    return JsonResponse({'ans': ans})

#def api_player (request, id):
#    return (request, .html, )

def api_get_player(request):
    player = Player.objects.get(pk=request.session['id'])
    return JsonResponse(model_to_dict(player))

def index_view(request):
    context = dict()
    games = Game.objects.all()
    context['games'] = games
    return render(request, 'index.html', context)


def game_view(request, id):
    context = dict()
    game = Game.objects.get(pk=id)
    players = game.players.all()
    context ['players'] = players
    return render(request, 'game.html', context)

def api_get_players (request):
    game = Game.objects.get(pk=request.session['game_id'])
    players = list(game.players.all().values('id', 'name'))
    return JsonResponse({'data':players})

def player_view(request, id):
    player = Player.objects.get(pk=id)
    context = dict()
    context['player_id'] = id
    context['game_id'] = player.game.id

    request.session['id'] = id
    request.session['game_id'] = player.game.id
    return render(request, 'player.html', context)



