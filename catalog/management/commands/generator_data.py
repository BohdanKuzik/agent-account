import os
from random import randint, choice
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
from catalog.models import Player, Club, Transfer, Agent


class Command(BaseCommand):
    help = 'Generate random data for the database'

    def handle(self, *args, **kwargs):

        fake = Faker()

        players = []
        for _ in range(100):
            player = Player.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=randint(16, 41),
                country=fake.country(),
                position=choice(['Forward', 'Midfielder', 'Defender', 'Goalkeeper'])
            )
            players.append(player)

        agents = []
        User = get_user_model()
        for _ in range(20):
            agent = User.objects.create_user(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                password='password123'
            )
            if isinstance(agent, Agent):
                assigned_players = fake.random_elements(elements=players, length=randint(1, 3), unique=True)
                for player in assigned_players:
                    player.agent = agent
                    player.save()
            agents.append(agent)

        clubs = []
        for _ in range(30):
            club = Club.objects.create(
                club_name=fake.company(),
                league=fake.word(),
            )
            clubs.append(club)

        for _ in range(100):
            transfer = Transfer.objects.create(
                transfer_date=fake.date_between(start_date='-2y', end_date='today'),
                club=choice(clubs),
                transaction_amount=randint(50000, 300000000)
            )
            random_agents = fake.random_elements(elements=agents, length=randint(1, 3), unique=True)
            transfer.agents.add(*random_agents)

        self.stdout.write(self.style.SUCCESS("Data generation completed!"))
