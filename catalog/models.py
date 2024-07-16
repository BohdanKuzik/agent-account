from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    class Meta:
        ordering = ("last_name",)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(AbstractUser):
    players = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="agents",
        null=True,
        blank=True
    )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Club(models.Model):
    club_name = models.CharField(max_length=255, unique=True)
    league = models.CharField(max_length=255)
    players = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="clubs"
    )

    class Meta:
        ordering = ("club_name",)

    def __str__(self):
        return self.club_name


class Transfer(models.Model):
    transfer_date = models.DateField()
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name="transfers"
    )
    agents = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="transfers")
    transaction_amount = models.IntegerField()

    class Meta:
        ordering = ("transfer_date",)

    def __str__(self):
        return f"Transfer on {self.transfer_date} for {self.transaction_amount} amount"
