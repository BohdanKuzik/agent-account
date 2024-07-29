from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from catalog.models import (
    Player,
    Agent,
    Club,
    Transfer,
)

User = get_user_model()

PLAYER_URL = reverse("catalog:player-list")


class PublicPlayerTest(TestCase):
    def test_login_required(self):
        res = self.client.get(PLAYER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivatePlayerTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="test",
            password="test123",
            first_name="John",
            last_name="Doe",
        )
        self.client.force_login(self.user)

    def test_retrieve_players(self):
        Player.objects.create(
            first_name="John",
            last_name="Doe",
            age=25,
            country="USA",
            position="Forward",
            agent=self.user
        )
        response = self.client.get(PLAYER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/player_list.html")
        self.assertContains(response, "John")


class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(response.status_code, 302)

        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/index.html")


class ClubListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        Club.objects.create(club_name="FC Awesome", league="Premier League")

    def test_club_list_view(self):
        response = self.client.get(reverse("catalog:club-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/club_list.html")
        self.assertContains(response, "FC Awesome")


class ClubDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        self.club = Club.objects.create(club_name="FC Awesome", league="Premier League")

    def test_club_detail_view(self):
        response = self.client.get(reverse("catalog:club-detail", args=[str(self.club.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/club_detail.html")
        self.assertContains(response, "FC Awesome")


class TransferListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        self.club = Club.objects.create(club_name="FC Awesome", league="Premier League")
        self.transfer = Transfer.objects.create(transfer_date="2024-01-01", club=self.club, transaction_amount=1000000)
        self.transfer.agents.set([self.user])

    def test_transfer_list_view(self):
        response = self.client.get(reverse("catalog:transfer-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/transfer_list.html")
        self.assertContains(response, "1000000")


class AgentListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        Agent.objects.create(username="agent1", password="password")

    def test_agent_list_view(self):
        response = self.client.get(reverse("catalog:agent-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/agent_list.html")


class PlayerListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        self.agent = Agent.objects.create_user(username="agent1", password="password")
        Player.objects.create(first_name="John", last_name="Doe", age=25, country="USA", position="Forward", agent=self.agent)

    def test_player_list_view(self):
        response = self.client.get(reverse("catalog:player-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/player_list.html")
        self.assertContains(response, "John")


class PlayerDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")
        self.agent = Agent.objects.create_user(username="agent1", password="password")
        self.player = Player.objects.create(first_name="John", last_name="Doe", age=25, country="USA", position="Forward", agent=self.agent)

    def test_player_detail_view(self):
        response = self.client.get(reverse("catalog:player-detail", args=[str(self.player.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/player_detail.html")
        self.assertContains(response, "John")
