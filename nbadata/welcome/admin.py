from django.contrib import admin

# Register your models here.
from .models import player, team, ranking, game, game_detail

admin.site.register(player)
admin.site.register(team)
admin.site.register(ranking)
admin.site.register(game)
admin.site.register(game_detail)