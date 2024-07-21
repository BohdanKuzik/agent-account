from django.test import TestCase
from catalog.forms import (
    AgentCreationForm,
    PlayerForm,
    PlayerSearchForm,
)


class AgentCreationFormTest(TestCase):
    def test_agent_creation_form_valid_data(self):
        form = AgentCreationForm(data={
            "username": "agent1",
            "first_name": "First",
            "last_name": "Last",
            "email": "agent@example.com",
            "password1": "testpassword123",
            "password2": "testpassword123"
        })
        self.assertTrue(form.is_valid())

    def test_agent_creation_form_no_data(self):
        form = AgentCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class PlayerFormTest(TestCase):
    def test_player_form_valid_data(self):
        form = PlayerForm(data={
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "country": "USA",
            "position": "Forward"
        })
        self.assertTrue(form.is_valid())

    def test_player_form_no_data(self):
        form = PlayerForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)


class PlayerSearchFormTest(TestCase):
    def test_player_search_form_valid_data(self):
        form = PlayerSearchForm(data={"last_name": "Doe"})
        self.assertTrue(form.is_valid())

    def test_player_search_form_no_data(self):
        form = PlayerSearchForm(data={})
        self.assertTrue(form.is_valid())
