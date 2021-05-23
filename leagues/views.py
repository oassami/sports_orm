from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		'q_title': 'All (current) players in the American Conference of Amateur Football with last name "Lopez"',
		"players": Player.objects.filter(curr_team__league=League.objects.get(name="American Conference of Amateur Football")).filter(last_name="Lopez")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")