from django.core.exceptions import ValidationError
from django.db import models

from config import settings


class ShowTheme(models.Model):
    """Model representing a theme for astronomy shows."""
    name = models.CharField(
        max_length=100,
        help_text='Enter the name of the show theme.'
    )

    def __str__(self):
        """String for representing the ShowTheme object."""
        return self.name


class AstronomyShow(models.Model):
    """Model representing an astronomy show."""
    title = models.CharField(
        max_length=100,
        help_text='Enter the title of the astronomy show.'
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text='Enter a brief description of the astronomy show.'
    )
    show_theme = models.ManyToManyField(
        ShowTheme,
        related_name="astronomy_shows",
        help_text='Select show theme(s) for this astronomy show.'
    )

    class Meta:
        ordering = ("title", )

    def __str__(self):
        """String for representing the AstronomyShow object."""
        return self.title


class PlanetariumDome(models.Model):
    """Model representing a planetarium dome."""
    name = models.CharField(
        max_length=100,
        help_text='Enter the name of the planetarium dome.'
    )
    rows = models.IntegerField(
        help_text='Enter the number of rows in the dome.'
    )
    seats_in_row = models.IntegerField(
        help_text='Enter the number of seats in each row.'
    )

    @property
    def capacity(self) -> int:
        """Calculate and return the capacity of the dome."""
        return self.rows * self.seats_in_row

    def __str__(self):
        """String for representing the PlanetariumDome object."""
        return self.name


class ShowSession(models.Model):
    """Model representing a show session."""
    astronomy_show = models.ForeignKey(
        AstronomyShow,
        on_delete=models.CASCADE,
        related_name="show_sessions",
        help_text='Select the astronomy show for this session.'
    )
    planetarium_dome = models.ForeignKey(
        PlanetariumDome,
        on_delete=models.CASCADE,
        related_name="show_sessions",
        help_text='Select the planetarium dome for this session.'
    )
    show_time = models.DateTimeField(
        help_text='Enter the date and time of the show session.'
    )

    class Meta:
        ordering = ("-show_time", )

    def __str__(self):
        """String for representing the ShowSession object."""
        return f"{self.planetarium_dome.name} - {self.show_time}"


class Reservation(models.Model):
    """Model representing a reservation made by a user."""
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Date and time when the reservation was created.'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations",
        help_text='The user who made the reservation.'
    )

    class Meta:
        ordering = ("-created_at", )

    def __str__(self):
        """String for representing the Reservation object."""
        return f"Reservation at {self.created_at}"


class Ticket(models.Model):
    """Model representing a ticket for a show session."""
    row = models.IntegerField(help_text='The row number of the seat.')
    seat = models.IntegerField(help_text='The seat number in the row.')
    show_session = models.ForeignKey(
        ShowSession,
        on_delete=models.CASCADE,
        related_name="tickets",
        help_text='The show session associated with the ticket.'
    )
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name="tickets",
        help_text='The reservation associated with the ticket.'
    )

    class Meta:
        unique_together = ("show_session", "row", "seat")
        ordering = ("row", "seat", )

    @staticmethod
    def validate_ticket(row, seat, planetarium_dome, error_to_raise):
        """Validate ticket attributes."""
        for ticket_attr_value, ticket_attr_name, planetarium_dome_attr_name in [
            (row, "row", "rows"),
            (seat, "seat", "seats_in_row"),
        ]:
            count_attrs = getattr(planetarium_dome, planetarium_dome_attr_name)
            if not (1 <= ticket_attr_value <= count_attrs):
                raise error_to_raise(
                    {
                        ticket_attr_name: f"{ticket_attr_name} "
                        f"number must be in available range: "
                        f"(1, {planetarium_dome_attr_name}): "
                        f"(1, {count_attrs})"
                    }
                )

    def clean(self):
        """Clean method to validate ticket."""
        Ticket.validate_ticket(
            self.row,
            self.seat,
            self.show_session.planetarium_dome,
            ValidationError,
        )

    def save(self, *args, **kwargs):
        """Save method to ensure clean is called."""
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        """String for representing the Ticket object."""
        return f"{str(self.show_session)} (row: {self.row}, seat: {self.seat})"
