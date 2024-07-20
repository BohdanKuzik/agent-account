from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


from catalog.forms import AgentCreationForm
from catalog.models import (
    Agent,
    Club,
    Player,
    Transfer,
)


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


class ClubListView(LoginRequiredMixin, generic.ListView):
    model = Club
    context_object_name = "club_list"
    template_name = "catalog/club_list.html"
    paginate_by = 10


class TransferListView(LoginRequiredMixin, generic.ListView):
    model = Transfer
    paginate_by = 5
    queryset = Transfer.objects.all().select_related("club")


class TransferDetailView(LoginRequiredMixin, generic.DetailView):
    model = Transfer


class AgentListView(LoginRequiredMixin, generic.ListView):
    model = Agent
    paginate_by = 5


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Agent
    template_name = 'catalog/agent_detail.html'
    context_object_name = 'agent'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agent = self.get_object()
        context['transfers'] = Transfer.objects.filter(agents=agent)
        context['players'] = agent.players.all()
        return context


class PlayerListView(LoginRequiredMixin, generic.ListView):
    model = Player
    paginate_by = 15


class PlayerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Player


class AgentRegisterView(generic.CreateView):
    model = Agent
    form_class = AgentCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
