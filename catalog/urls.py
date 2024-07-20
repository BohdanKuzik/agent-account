from django.urls import path, include

from catalog.views import (
    index,
    ClubListView,
    PlayerListView,
    AgentListView,
    TransferListView,
    TransferDetailView,
    PlayerDetailView,
    AgentDetailView,
    AgentRegisterView, PlayerDeleteView,
)

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
        "transfer/<int:pk>/",
        TransferDetailView.as_view(),
        name="transfer-detail",
    ),
    path(
        "agents/",
        AgentListView.as_view(),
        name="agent-list",
    ),
    path(
        "agents/<int:pk>/",
        AgentDetailView.as_view(),
        name="agent-detail",
    ),
    path(
        "players/",
        PlayerListView.as_view(),
        name="player-list",
    ),
    path(
        "players/<int:pk>/",
        PlayerDetailView.as_view(),
        name="player-detail",
    ),
    path('player/<int:pk>/delete/', PlayerDeleteView.as_view(), name='player-delete'),
    path('register/', AgentRegisterView.as_view(), name='register'),
]

app_name = "catalog"
