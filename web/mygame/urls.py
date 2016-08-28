"""mygame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from gameapp1.views import api_user_command
from gameapp1.views import api_get_items
from gameapp1.views import index_view
from gameapp1.views import api_get_player
from gameapp1.views import game_view
from gameapp1.views import api_get_players
from gameapp1.views import player_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api_get_items/$', api_get_items),
    url(r'^$', index_view, name='index'),
    url(r'^game/(?P<id>[0-9]+)$', game_view, name='game'),
    url(r'^api_get_player/$', api_get_player, name = 'api_get_player'),
    url(r'^player/(?P<id>[0-9]+)$', player_view, name = 'player'),
    url(r'^api_user_command/$', api_user_command),
    url(r'^api_get_players/$', api_get_players)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
