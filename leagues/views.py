from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	# Query 1 : All womens' leagues
	context = {
		"q_title": "All womens' leagues",
		# "leagues": League.objects.all(),
		"leagues": League.objects.filter(name__contains="womens'"),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")