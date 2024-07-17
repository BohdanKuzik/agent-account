from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from catalog.models import Agent, Club, Player, Transfer


@login_required
def index(request):
    """View function for the home page of the site."""

    num_agents = Agent.objects.count()
    num_clubs = Club.objects.count()
    num_players = Player.objects.count()
    num_transfers = Transfer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_agents": num_agents,
        "num_clubs": num_clubs,
        "num_players": num_players,
        "num_transfers": num_transfers,
        "num_visits": num_visits + 1,
    }

    return render(request, "catalog/index.html", context=context)
