from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.urls import reverse
from .models import player, team, game, game_detail, ranking
from django.db import IntegrityError
from django.db.models import F, Value
from django.db.models.functions import Concat
# Create your views here.

# welcome/menu page
def index(request):
    return render(request, 'welcome.html')

def add_player_page(request):
    template = loader.get_template('addplayer.html')
    return HttpResponse(template.render({}, request))

def add_player(request):
    try:
        pname = request.POST.get('player_name')
        tid = request.POST.get('team_id')
        pid = request.POST.get('player_id')
        snum = request.POST.get('season')
        if(pname is None or pid is None or tid
        is None or snum is None or pname == '' or pid == '' or tid == '' or snum == ''):
            return HttpResponseRedirect(reverse('index'))
        else:
            p = player(player_name = pname, team_id = tid, player_id = pid, season = snum)
            p.save()
            return HttpResponseRedirect(reverse('result_player'))
    except(IntegrityError):
        return HttpResponseRedirect(reverse('index'))

# retrieves and displays all players in nbadata mysql player table
def delete_player_page(request):
    myplayers = player.objects.all().values()
    template = loader.get_template('deleteplayer.html')
    context = {'myplayers': myplayers}
    return HttpResponse(template.render(context, request))

# deletes selected player and redirects user back to delete page
def delete_player(request, id):
    try:
        p = player.objects.get(id = id)
        p.delete()
        return HttpResponseRedirect(reverse('delete_player_page'))
    except(IntegrityError):
        return HttpResponseRedirect(reverse('index'))

def update_player_page(request):
    myplayers = player.objects.all().values()
    template = loader.get_template('updateplayer.html')
    context = { 'myplayers': myplayers }
    return HttpResponse(template.render(context, request))

def update_player_form(request, id):
    myplayers = player.objects.get(id = id)
    template = loader.get_template('updateplayerform.html')
    context = {'x': myplayers, }
    return HttpResponse(template.render(context, request))

def update_player(request):
    try:
        pname = request.POST.get('player_name')
        tid = request.POST.get('team_id')
        pid = request.POST.get('player_id')
        snum = request.POST.get('season')
        id = request.POST.get('id')
        p = player.objects.get(id = id)
        if(pname != ''):
            p.player_name = pname
        if(tid != ''):
            p.team_id = tid
        if(pid != ''):
            p.player_id = pid
        if(snum != ''):
            p.season = snum
        p.save()
        template = loader.get_template('updateplayerresult.html')
        context = { 'x': p }
        return HttpResponse(template.render(context, request))
    except(IntegrityError):
        return HttpResponseRedirect(reverse('index'))

def search_player_page(request):
    template = loader.get_template('searchplayer.html')
    return HttpResponse(template.render({}, request))

def search_player(request):
    lastname = request.POST.get('lastname')
    template = loader.get_template('searchplayerresult.html')
    p = player.objects.filter(player_name__endswith = lastname).all().values()
    #  p = player.objects.filter(player_name = pname)
    context = { 'p': p, }
    return HttpResponse(template.render(context, request))
    #  return HttpResponseRedirect(reverse('searchplayerresult'))

#results page for player table
def result_player(request):
    myplayers = player.objects.all().values().order_by('-id')[:1]
    template = loader.get_template('resultplayer.html')
    context = { 'myplayers' : myplayers, }
    #return render(request, 'resultplayer.html', context)
    return HttpResponse(template.render(context, request))


def add_team_page(request):
    template = loader.get_template('addteam.html')
    return HttpResponse(template.render({}, request))

def add_team(request):
    try:
        tid = request.POST.get('team_id')
        miny = request.POST.get('min_year')
        maxy = request.POST.get('max_year')
        abb = request.POST.get('abbreviation')
        nname = request.POST.get('nickname')
        yearf = request.POST.get('year_founded')
        cname = request.POST.get('city')
        aname = request.POST.get('arena_name')
        acap = request.POST.get('arena_cap')
        oname = request.POST.get('owner')
        gm = request.POST.get('general_manager')
        hc = request.POST.get('head_coach')
        dla = request.POST.get('d_league_affiliation')
        if(tid is None or miny is None or maxy is None or abb is None or nname is None
        or yearf is None or cname is None or aname is None or acap is None or oname is None
        or gm is None or hc is None or dla is None or tid == '' or miny == '' or maxy == '' 
        or  abb == '' or nname == '' or  yearf == '' or cname == '' or aname == '' or acap == '' 
        or oname == '' or gm == '' or hc == '' or dla == ''):
            return HttpResponseRedirect(reverse('index'))
        else:
            t = team(team_id = tid, min_year = miny, max_year = maxy, abbreviation = abb, nickname = nname,
            year_founded = yearf, city = cname, arena_name = aname, arena_cap = acap, owner = oname,
            general_manager = gm, head_coach = hc, d_league_affiliation = dla)
            t.save()
            return HttpResponseRedirect(reverse('result_team'))
    except(IntegrityError):
        return HttpResponseRedirect(reverse('index'))

def delete_team_page(request):
    myteams = team.objects.all().values()
    template = loader.get_template('deleteteam.html')
    context = { 'myteams': myteams }
    return HttpResponse(template.render(context, request))

def delete_team(request, id):
    try:
        t = team.objects.get(team_id = id)
        t.delete()
        return HttpResponseRedirect(reverse('delete_team_page'))
    except(IntegrityError):
        return HttpResponseRedirect('index')

def update_team_page(request):
    myteams = team.objects.all().values()
    template = loader.get_template('updateteam.html')
    context = { 'myteams': myteams }
    return HttpResponse(template.render(context, request))

def update_team_form(request, id):
    myteams = team.objects.get(team_id = id)
    template = loader.get_template('updateteamform.html')
    context = { 'x': myteams }
    return HttpResponse(template.render(context, request))

def update_team(request):
    try:
        tid = request.POST.get('team_id')
        miny = request.POST.get('min_year')
        maxy = request.POST.get('max_year')
        abb = request.POST.get('abbreviation')
        nname = request.POST.get('nickname')
        yearf = request.POST.get('year_founded')
        cname = request.POST.get('city')
        aname = request.POST.get('arena_name')
        acap = request.POST.get('arena_cap')
        oname = request.POST.get('owner')
        gm = request.POST.get('general_manager')
        hc = request.POST.get('head_coach')
        dla = request.POST.get('d_league_affiliation')
        t = team.objects.get(team_id = tid)
        if(tid != ''):
            t.team_id = tid
        if(miny != ''):
            t.min_year = miny
        if(maxy != ''):
            t.max_year = maxy
        if(abb != ''):
            t.abbreviation = abb
        if(nname != ''):
            t.nickname = nname
        if(yearf != ''):
            t.year_founded = yearf
        if(cname != ''):
            t.city = cname
        if(aname != ''):
            t.arena_name = aname
        if(acap != ''):
            t.arena_cap = acap
        if(oname != ''):
            t.owner = oname
        if(gm != ''):
            t.general_manager = gm
        if(hc != ''):
            t.head_coach = hc
        if(dla != ''):
            t.d_league_affiliation = dla
        t.save()
        template = loader.get_template('updateteamresult.html')
        context = { 'x': t }
        return HttpResponse(template.render(context, request))
    except(IntegrityError):
        return HttpResponseRedirect(reverse('index'))

def search_team_page(request):
    template = loader.get_template('searchteam.html')
    return HttpResponse(template.render({}, request))

def search_team(request):
    cname = request.POST.get('cityname')
    template = loader.get_template('searchteamresult.html')
    t = team.objects.filter(city__startswith = cname).all().values()
    context = { 't': t}
    return HttpResponse(template.render(context, request))

def result_team(request):
    myteams = team.objects.all().values().order_by('-id')[:1]
    template = loader.get_template('resultteam.html')
    context = { 'myteams': myteams}
    return HttpResponse(template.render(context, request))

def add_ranking_page(request):
    template = loader.get_template('addranking.html')
    return HttpResponse(template.render({}, request))

def add_ranking(request):
    team_id = request.POST['team_id']
    league_id = request.POST['league_id']
    season_id = request.POST['season_id']
    standings_date = request.POST['standings_date']
    conference = request.POST['conference']
    team_name = request.POST['team_name']
    games = request.POST['games']
    win = request.POST['win']
    loss = request.POST['loss']
    win_pct = request.POST['win_pct']
    home_record = request.POST['home_record']
    road_record = request.POST['road_record']
    return_to_play = request.POST['return_to_play']
    r = ranking(team_id, league_id, season_id, standings_date,
    conference, team_name, games, win, loss, win_pct, home_record,
    road_record, return_to_play)
    r.save()
    # change the 'index' in reverse function to ranking
    # page after adding ranking
    return HttpResponseRedirect(reverse('index'))

def add_game_page(request):
    template = loader.get_template('addgame.html')
    return HttpResponse(template.render({}, request))

def add_game(request):
    game_date = request.POST['game_date']
    game_id = request.POST['game_id']
    game_status = request.POST['game_status']
    home_team_id = request.POST['home_team_id']
    visitor_team_id = request.POST['visitor_team_id']
    season = request.POST['season']
    team_id_home = request.POST['team_id_home']
    pts_home = request.POST['pts_home']
    fg_pct_home = request.POST['fg_pct_home']
    ft_pct_home = request.POST['ft_pct_home']
    fg3_pct_home = request.POST['fg3_pct_home']
    ast_home = request.POST['ast_home']
    reb_home = request.POST['reb_home']
    team_id_away = request.POST['team_id_away']
    pts_away = request.POST['pts_away']
    fg_pct_away = request.POST['fg_pct_away']
    ft_pct_away = request.POST['ft_pct_away']
    fg3_pct_away = request.POST['fg3_pct_away']
    ast_away = request.POST['ast_away']
    reb_away = request.POST['reb_away']
    home_team_wins = request.POST['home_team_wins']
    g = game(game_date, game_id, game_status, home_team_id, visitor_team_id,
    season, team_id_home, pts_home, fg_pct_home, ft_pct_home,
    fg3_pct_home, ast_home, reb_home, team_id_away, pts_away,
    fg_pct_away, ft_pct_away, fg3_pct_away, ast_away, reb_away,
    home_team_wins)
    g.save()
    # change the 'index' in reverse function to game
    # page after adding game
    return HttpResponseRedirect(reverse('index'))

def add_game_detail_page(request):
    template = loader.get_template('addgamedetail.html')
    return HttpResponse(template.render({}, request))

def add_game_detail(request):
    game_id = request.POST['game_id']
    team_id = request.POST['team_id']
    abbreviation = request.POST['abbreviation']
    city = request.POST['city']
    player_id = request.POST['player_id']
    player_name = request.POST['player_name']
    nickname = request.POST['nickname']
    start_position = request.POST['start_position']
    comment = request.POST['comment']
    minutes = request.POST['minutes']
    fgm = request.POST['fgm']
    fga = request.POST['fga']
    fg_pct = request.POST['fg_pct']
    fg3m = request.POST['fg3m']
    fg3a = request.POST['fg3a']
    fg3_pct = request.POST['fg3_pct']
    ftm = request.POST['ftm']
    fta = request.POST['fta']
    ft_pct = request.POST['ft_pct']
    o_reb = request.POST['o_reb']
    d_reb = request.POST['d_reb']
    reb = request.POST['reb']
    ast = request.POST['ast']
    stl = request.POST['stl']
    blk = request.POST['blk']
    turnovers = request.POST['turnovers']
    pf = request.POST['pf']
    pts = request.POST['pts']
    plus_minus = request.POST['plus_minus']
    gd = game_detail(game_id, team_id, abbreviation, city,
    player_id, player_name, nickname, start_position, comment, minutes,
    fgm, fga, fg_pct, fg3m, fg3a, fg3_pct, ftm, fta, ft_pct,
    o_reb, d_reb, reb, ast, stl, blk, turnovers, pf, pts,
    plus_minus)
    gd.save()
    # change the 'index' in reverse function to game_detail
    # page after adding game_detail
    return HttpResponseRedirect(reverse('index'))