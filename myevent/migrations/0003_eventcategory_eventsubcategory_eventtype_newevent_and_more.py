# Generated by Django 4.2.1 on 2023-06-23 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myevent', '0002_alter_event_location_alter_event_ticket_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EventSubcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NewEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_Name', models.CharField(max_length=100)),
                ('is_online', models.BooleanField(default=False)),
                ('Venue_name', models.CharField(max_length=100)),
                ('Event_description', models.TextField()),
                ('Event_image', models.ImageField(upload_to='event_images/')),
                ('is_one_time_event', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('is_seating_reserved', models.BooleanField(default=False)),
                ('total_capacity_of_event', models.PositiveIntegerField()),
                ('is_ticket_sale_immediate', models.BooleanField(default=True)),
                ('is_ticket_sale_schedule', models.BooleanField(default=False)),
                ('is_cutoff_time', models.BooleanField(default=False)),
                ('ticket_sale_end_time', models.DateTimeField(blank=True, null=True)),
                ('event_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myevent.eventcategory')),
                ('event_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myevent.eventsubcategory')),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myevent.eventtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_name', models.CharField(max_length=100)),
                ('ticket_quantities', models.PositiveIntegerField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ticket_description', models.TextField()),
                ('ticket_buy_by_list', models.BooleanField(default=False)),
                ('minimum_ticket_order', models.PositiveIntegerField(default=1)),
                ('maximum_ticket_order', models.PositiveIntegerField(default=10)),
                ('service_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ticket_password', models.CharField(blank=True, max_length=50)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myevent.newevent')),
                ('ticket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myevent.tickettype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
