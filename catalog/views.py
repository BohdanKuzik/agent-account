from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.urls import reverse_lazy, reverse
from django.views import generic


from catalog.forms import (
    AgentCreationForm,
    PlayerForm,
    PlayerSearchForm,
)
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


class ClubDetailView(LoginRequiredMixin, generic.DetailView):
    model = Club


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
    template_name = "catalog/agent_detail.html"
    context_object_name = "agent"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agent = self.get_object()
        context["transfers"] = Transfer.objects.filter(agents=agent)
        context["players"] = agent.players.all()
        return context


class PlayerListView(LoginRequiredMixin, generic.ListView):
    model = Player
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PlayerListView, self).get_context_data(**kwargs)
        last_name = self.request.GET.get("last_name", "")
        context["search_form"] = PlayerSearchForm(
            initial={"last_name": last_name}
        )
        return context

    def get_queryset(self):
        queryset = Player.objects.all()
        last_name = self.request.GET.get("last_name")
        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)
        return queryset


class PlayerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Player


class PlayerUpdateView(generic.UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = "catalog/player_form.html"
    success_url = reverse_lazy("catalog:player-list")


class AgentRegisterView(generic.CreateView):
    model = Agent
    form_class = AgentCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserProfileView(LoginRequiredMixin, generic.DetailView):
    model = Agent
    template_name = "catalog/user_profile.html"
    context_object_name = "agent"

    def get_object(self):
        return self.request.user


@login_required
def player_delete_confirm(request, pk):
    player = get_object_or_404(Player, pk=pk)

    if request.method == "POST":
        player.delete()
        return redirect(reverse("catalog:player-list"))

    return render(
        request,
        "catalog/player_confirm_delete.html",
        {"player": player}
    )


@login_required
def create_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalog:player-list")
    else:
        form = PlayerForm()

    return render(request, "catalog/player_create.html", {"form": form})
