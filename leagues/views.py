from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		'q_title': 'Every player with last name "Cooper"',
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		"players": Player.objects.filter(last_name="Cooper"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")