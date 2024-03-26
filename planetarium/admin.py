from django.contrib import admin

from .models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)

app_name = "planetarium"

admin.site.register(AstronomyShow)
admin.site.register(ShowTheme)
admin.site.register(PlanetariumDome)
admin.site.register(ShowSession)
admin.site.register(Reservation)
admin.site.register(Ticket)
