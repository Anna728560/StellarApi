# Generated by Django 4.2.11 on 2024-03-28 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("planetarium", "0003_alter_reservation_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="astronomyshow",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Enter a brief description of the astronomy show.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="astronomyshow",
            name="show_theme",
            field=models.ManyToManyField(
                help_text="Select show theme(s) for this astronomy show.",
                related_name="astronomy_shows",
                to="planetarium.showtheme",
            ),
        ),
        migrations.AlterField(
            model_name="astronomyshow",
            name="title",
            field=models.CharField(
                help_text="Enter the title of the astronomy show.", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="planetariumdome",
            name="name",
            field=models.CharField(
                help_text="Enter the name of the planetarium dome.", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="planetariumdome",
            name="rows",
            field=models.IntegerField(
                help_text="Enter the number of rows in the dome."
            ),
        ),
        migrations.AlterField(
            model_name="planetariumdome",
            name="seats_in_row",
            field=models.IntegerField(
                help_text="Enter the number of seats in each row."
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Date and time when the reservation was created.",
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="user",
            field=models.ForeignKey(
                help_text="The user who made the reservation.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="showsession",
            name="astronomy_show",
            field=models.ForeignKey(
                help_text="Select the astronomy show for this session.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="show_sessions",
                to="planetarium.astronomyshow",
            ),
        ),
        migrations.AlterField(
            model_name="showsession",
            name="planetarium_dome",
            field=models.ForeignKey(
                help_text="Select the planetarium dome for this session.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="show_sessions",
                to="planetarium.planetariumdome",
            ),
        ),
        migrations.AlterField(
            model_name="showsession",
            name="show_time",
            field=models.DateTimeField(
                help_text="Enter the date and time of the show session."
            ),
        ),
        migrations.AlterField(
            model_name="showtheme",
            name="name",
            field=models.CharField(
                help_text="Enter the name of the show theme.", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="reservation",
            field=models.ForeignKey(
                help_text="The reservation associated with the ticket.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tickets",
                to="planetarium.reservation",
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="row",
            field=models.IntegerField(help_text="The row number of the seat."),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="seat",
            field=models.IntegerField(help_text="The seat number in the row."),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="show_session",
            field=models.ForeignKey(
                help_text="The show session associated with the ticket.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tickets",
                to="planetarium.showsession",
            ),
        ),
    ]
