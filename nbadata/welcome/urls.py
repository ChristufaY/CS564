from django.urls import path, include
from . import views

urlpatterns = [
    # url of welcome page
    path('', views.index, name = 'index'),
    # urls for player table related functions/pages
    path('add_player_page/', views.add_player_page, name = 'add_player_page'),
    path('add_player_page/add_player/', views.add_player, name = 'add_player'),
    path('delete_player_page/', views.delete_player_page, name = 'delete_player_page'),
    path('delete_player_page/delete_player/<int:id>', views.delete_player, name = 'delete_player'),
    path('search_player_page/', views.search_player_page, name = 'search_player_page'),
    path('search_player_page/search_player/', views.search_player, name = 'search_player'),
    path('update_player_page/', views.update_player_page, name = 'update_player_page'),
    path('update_player_page/update_player_form/<int:id>', views.update_player_form, name = 'update_player_form'),
    path('update_player_page/update_player_form/update_player/', views.update_player, name = 'update_player'),
    path('add_player_page/result_player', views.result_player, name = 'result_player'),
    # urls for team table related functions/pages
    path('add_team_page/', views.add_team_page, name = 'add_team_page'),
    path('add_team_page/add_team/', views.add_team, name = 'add_team'),
    path('delete_team_page/', views.delete_team_page, name = 'delete_team_page'),
    path('delete_team_page/delete_team/<int:id>', views.delete_team, name = 'delete_team'),
    path('search_team_page/', views.search_team_page, name = 'search_team_page'),
    path('search_team_page/search_team/', views.search_team, name = 'search_team'),
    path('update_team_page/', views.update_team_page, name = 'update_team_page'),
    path('update_team_page/update_team_form/<int:id>', views.update_team_form, name = 'update_team_form'),
    path('update_team_page/update_team_form/update_team/', views.update_team, name = 'update_team'),
    path('add_team_page/result_team', views.result_team, name = 'result_team'),
    
    # urls for ranking table related functions/pages
    # path('add_ranking_page/', views.add_ranking_page, name = 'add_ranking_page'),
    # path('add_ranking_page/add_ranking/', views.add_ranking, name = 'add_ranking'),
    # path('delete_ranking_page/', views.delete_ranking_page, name = 'delete_ranking_page'),
    # path('delete_ranking_page/delete_ranking/<int:id>', views.delete_ranking, name = 'delete_ranking'),
    # path('search_ranking_page/', views.search_ranking_page, name = 'search_ranking_page'),
    # path('search_ranking_page/search_ranking/', views.search_ranking, name = 'search_ranking'),
    # path('update_ranking_page/', views.update_ranking_page, name = 'update_ranking_page'),
    # path('update_ranking_page/update_ranking_form/<int:id>', views.update_ranking_form, name = 'update_ranking_form'),
    # path('update_ranking_page/update_ranking_form/update_ranking/', views.update_ranking, name = 'update_ranking'),
    # path('add_ranking_page/result_ranking', views.result_ranking, name = 'result_ranking'),
    
    # urls for game table related functions/pages
    # path('add_game_page/', views.add_game_page, name = 'add_game_page'),
    # path('add_game_page/add_game/', views.add_game, name = 'add_game'),
    # path('delete_game_page/', views.delete_game_page, name = 'delete_game_page'),
    # path('delete_game_page/delete_game/<int:id>', views.delete_game, name = 'delete_game'),
    # path('search_game_page/', views.search_game_page, name = 'search_game_page'),
    # path('search_game_page/search_game/', views.search_game, name = 'search_game'),
    # path('update_game_page/', views.update_game_page, name = 'update_game_page'),
    # path('update_game_page/update_game_form/<int:id>', views.update_game_form, name = 'update_game_form'),
    # path('update_game_page/update_game_form/update_game/', views.update_game, name = 'update_game'),
    # path('add_game_page/result_game', views.result_game, name = 'result_game'),
    
    # urls for game_detail table related functions/pages
    # path('add_game_detail_page/', views.add_game_detail_page, name = 'add_game_detail_page'),
    # path('add_game_detail_page/add_game_detail/', views.add_game_detail, name = 'add_game_detail'),
    # path('delete_game_detail_page/', views.delete_game_detail_page, name = 'delete_game_detail_page'),
    # path('delete_game_detail_page/delete_game_detail/<int:id>', views.delete_game_detail, name = 'delete_game_detail'),
    # path('search_game_detail_page/', views.search_game_detail_page, name = 'search_game_detail_page'),
    # path('search_game_detail_page/search_game_detail/', views.search_game_detail, name = 'search_game_detail'),
    # path('update_game_detail_page/', views.update_game_detail_page, name = 'update_game_detail_page'),
    # path('update_game_detail_page/update_game_detail_form/<int:id>', views.update_game_detail_form, name = 'update_game_detail_form'),
    # path('update_game_detail_page/update_game_detail_form/update_game_detail/', views.update_game_detail, name = 'update_game_detail'),
    # path('add_game_detail_page/result_game_detail', views.result_game_detail, name = 'result_game_detail'),
]