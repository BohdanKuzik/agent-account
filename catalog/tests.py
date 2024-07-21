from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import (
    Player,
    Agent,
    Club,
    Transfer,
)

User = get_user_model()


class ModelTests(TestCase):
    def setUp(self):
        self.agent = Agent.objects.create(first_name="Test")

    def test_player_str(self):
        player = Player.objects.create(
            first_name="John",
            last_name="Doe",
            age=25,
            country="USA",
            position="Forward",
            agent=self.agent
        )
        self.assertEqual(str(player), "John Doe")


class AgentModelTest(TestCase):
    def test_agent_str(self):
        agent = User.objects.create_user(
            username="agent1",
            first_name="Agent",
            last_name="Smith",
            password="password"
        )
        self.assertEqual(str(agent), "agent1 (Agent Smith)")

    def test_agent_get_absolute_url(self):
        agent = User.objects.create_user(
            username="agent2",
            first_name="Jane",
            last_name="Doe",
            password="password"
        )
        self.assertEqual(agent.get_absolute_url(), f"/catalog/agent-detail/{agent.pk}/")


class ClubModelTest(TestCase):
    def test_club_str(self):
        club = Club.objects.create(
            club_name="FC Awesome",
            league="Premier League"
        )
        self.assertEqual(str(club), "FC Awesome")


class TransferModelTest(TestCase):
    def setUp(self):
        self.agent1 = User.objects.create_user(username="agent1", password="password")
        self.agent2 = User.objects.create_user(username="agent2", password="password")
        self.club = Club.objects.create(club_name="FC Awesome", league="Premier League")

    def test_transfer_str(self):
        transfer = Transfer.objects.create(
            transfer_date="2024-01-01",
            club=self.club,
            transaction_amount=1000000
        )
        transfer.agents.set([self.agent1, self.agent2])
        self.assertEqual(str(transfer), "Transfer on 2024-01-01 for 1000000 amount")
