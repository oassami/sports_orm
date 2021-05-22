from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		'q_title': 'All (current) players on the Boston Penguins',
		# "leagues": League.objects.all(),
		# "teams": Team.objects.filter(league=League.objects.get(name="Atlantic Soccer Conference")),
		"players": Player.objects.filter(curr_team=Team.objects.get(team_name="Penguins", location="Boston")),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")