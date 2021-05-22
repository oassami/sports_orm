from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	# Query 1 : All baseball leagues
	context = {
		"q_title": "All baseball leagues",
		# "leagues": League.objects.all(),
		"leagues": League.objects.filter(sport__contains='Baseball'),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")