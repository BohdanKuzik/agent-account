from django.urls import path

from catalog.views import index, ClubListView, PlayerListView, AgentListView, TransferListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "clubs/",
        ClubListView.as_view(),
        name="club-list",
    ),
    path(
        "transfers/",
        TransferListView.as_view(),
        name="transfer-list",
    ),
    path(
        "agents/",
        AgentListView.as_view(),
        name="agent-list",
    ),
    path(
        "players/",
        PlayerListView.as_view(),
        name="player-list",
    ),
]

app_name = "catalog"
