from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import (
    Player,
    Agent,
    Club,
    Transfer,
)


@admin.register(Agent)
class AgentAdmin(UserAdmin):
    pass


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    search_fields = ("transfer_date",)
    list_filter = ("transaction_amount",)


admin.site.register(Club)

admin.site.register(Player)
