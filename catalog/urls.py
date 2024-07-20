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
    AgentRegisterView,
    player_delete_confirm, create_player, PlayerUpdateView, ClubDetailView, UserProfileView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "clubs/",
        ClubListView.as_view(),
        name="club-list",
    ),
    path(
        "clubs/<int:pk>/",
        ClubDetailView.as_view(),
        name="club-detail",
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
    path('player/<int:pk>/delete/', player_delete_confirm, name='player-delete'),
    path('player/<int:pk>/update/', PlayerUpdateView.as_view(), name='player-update'),
    path('player/create/', create_player, name='player-create'),
    path('register/', AgentRegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]

app_name = "catalog"
