from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    country = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    agent = models.ForeignKey(
        "Agent",
        on_delete=models.CASCADE,
        related_name="players",
        null=True,
        blank=True
    )

    class Meta:
        ordering = ("last_name",)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(AbstractUser):
    class Meta:
        verbose_name = "agent"
        verbose_name_plural = "agents"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("catalog:agent-detail", kwargs={"pk": self.pk})


class Club(models.Model):
    club_name = models.CharField(max_length=255, unique=True)
    league = models.CharField(max_length=255)

    class Meta:
        ordering = ("club_name",)

    def __str__(self):
        return self.club_name


class Transfer(models.Model):
    transfer_date = models.DateField()
    agents = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="transfers"
    )
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name="transfers"
    )
    transaction_amount = models.IntegerField()

    class Meta:
        ordering = ("transfer_date",)

    def __str__(self):
        return (f"Transfer on {self.transfer_date}"
                f" for {self.transaction_amount} amount")
