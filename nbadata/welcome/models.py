from django.db import models

# Create your models here.
class player(models.Model):
    player_name = models.CharField(max_length=255, default='')
    team_id = models.CharField(max_length=10, default='')
    player_id = models.CharField(max_length=7, default='')
    season = models.CharField(max_length=4, default='')
    class Meta:
        db_table = 'player'

class team(models.Model):
    team_id = models.CharField(max_length=10, default='')
    min_year = models.CharField(max_length=4, default='')
    max_year = models.CharField(max_length=4, default='')
    abbreviation = models.CharField(max_length=3, default='')
    nickname = models.CharField(max_length=255, default='')
    year_founded = models.CharField(max_length=4, default='')
    city = models.CharField(max_length=255, default='')
    arena_name = models.CharField(max_length=255, default='')
    arena_cap = models.CharField(max_length=7, default='')
    owner = models.CharField(max_length=255, default='')
    general_manager = models.CharField(max_length=255, default='')
    head_coach = models.CharField(max_length=255,default='')
    d_league_affiliation = models.CharField(max_length=255,default='')
    class Meta:
        db_table = 'team'

class ranking(models.Model):
    team_id = models.CharField(max_length=255, default='')
    league_id = models.CharField(max_length=255, default='')
    season_id = models.CharField(max_length=255, default='')
    standings_date = models.CharField(max_length=255, default='')
    conference = models.CharField(max_length=255, default='')
    team_name = models.CharField(max_length=255, default='')
    games = models.CharField(max_length=255, default='')
    win = models.CharField(max_length=255, default='')
    loss = models.CharField(max_length=255, default='')
    win_pct = models.CharField(max_length=255, default='')
    home_record = models.CharField(max_length=255, default='')
    road_record = models.CharField(max_length=255, default='')
    return_to_play = models.CharField(max_length=255, default='')
    class Meta:
        db_table = 'ranking'

class game(models.Model):
    game_date = models.CharField(max_length=255, default='')
    game_id = models.CharField(max_length=255, default='')
    game_status = models.CharField(max_length=255, default='')
    home_team_id = models.CharField(max_length=255, default='')
    visitor_team_id = models.CharField(max_length=255, default='')
    season = models.CharField(max_length=255, default='')
    team_id_home = models.CharField(max_length=255, default='')
    pts_home = models.CharField(max_length=255, default='')
    fg_pct_home = models.CharField(max_length=255, default='')
    ft_pct_home = models.CharField(max_length=255, default='')
    fg3_pct_home = models.CharField(max_length=255, default='')
    ast_home = models.CharField(max_length=255, default='')
    reb_home = models.CharField(max_length=255, default='')
    team_id_away = models.CharField(max_length=255, default='')
    pts_away = models.CharField(max_length=255, default='')
    fg_pct_away = models.CharField(max_length=255, default='')
    ft_pct_away = models.CharField(max_length=255, default='')
    fg3_pct_away = models.CharField(max_length=255, default='')
    ast_away = models.CharField(max_length=255, default='')
    reb_away = models.CharField(max_length=255, default='')
    home_team_wins = models.CharField(max_length=255, default='')
    class Meta:
        db_table = 'game'

class game_detail(models.Model):
    game_id = models.CharField(max_length=255, default='')
    team_id = models.CharField(max_length=255, default='')
    abbreviation = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    player_id = models.CharField(max_length=255, default='')
    player_name = models.CharField(max_length=255, default='')
    nickname = models.CharField(max_length=255, default='')
    start_position = models.CharField(max_length=255, default='')
    comment = models.CharField(max_length=255, default='')
    minutes = models.CharField(max_length=255, default='')
    fgm = models.CharField(max_length=255, default='')
    fga = models.CharField(max_length=255, default='')
    fg_pct = models.CharField(max_length=255, default='')
    fg3m = models.CharField(max_length=255, default='')
    fg3a = models.CharField(max_length=255, default='')
    fg3_pct = models.CharField(max_length=255, default='')
    ftm = models.CharField(max_length=255, default='')
    fta = models.CharField(max_length=255, default='')
    ft_pct = models.CharField(max_length=255, default='')
    o_reb = models.CharField(max_length=255, default='')
    d_reb = models.CharField(max_length=255, default='')
    reb = models.CharField(max_length=255, default='')
    ast = models.CharField(max_length=255, default='')
    stl = models.CharField(max_length=255, default='')
    blk = models.CharField(max_length=255, default='')
    turnovers = models.CharField(max_length=255, default='')
    pf = models.CharField(max_length=255, default='')
    pts = models.CharField(max_length=255, default='')
    plus_minus = models.CharField(max_length=255, default='')
    class Meta:
        db_table = 'game_detail'