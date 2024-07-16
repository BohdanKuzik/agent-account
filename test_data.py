import os
from random import randint, choice

import django
from django.contrib.auth import get_user_model
from faker import Faker

from catalog.models import Player, Club, Transfer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agent_account.settings')
django.setup()


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
for _ in range(15):
    agent = User.objects.create_user(
        username=fake.user_name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password='password123'
    )
    agent.players = choice(players)
    agent.save()
    agents.append(agent)


clubs = []
for _ in range(30):
    club = Club.objects.create(
        club_name=fake.company(),
        league=fake.word(),
        players=choice(players)
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
print("Data generation completed!")
