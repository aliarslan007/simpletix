from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255,null=True, blank=True)
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
    # Add more fields as per your requirements

    def __str__(self):
        return self.title

class EventType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class EventCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class EventSubcategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class NewEvent(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    Event_Name = models.CharField(max_length=100)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    event_category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    event_subcategory = models.ForeignKey(EventSubcategory, on_delete=models.CASCADE)
    is_online = models.BooleanField(null=True, blank=True,default=False)
    Venue_name = models.CharField(max_length=100)
    Event_description = models.TextField()
    Event_image = models.ImageField(upload_to='event_images/')
    is_one_time_event = models.BooleanField(default=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    is_seating_reserved = models.BooleanField(default=False)
    total_capacity_of_event = models.PositiveIntegerField()
    
    def __str__(self):
        return self.Event_Name
    
class TicketType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(NewEvent, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    ticket_name = models.CharField(max_length=100)
    ticket_quantities = models.PositiveIntegerField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    # ticket_description = models.TextField(null=True, blank=True,)
    # ticket_buy_by_list = models.BooleanField(default=False)
    # minimum_ticket_order = models.PositiveIntegerField(default=1)
    # maximum_ticket_order = models.PositiveIntegerField(default=10)
    # service_fee = models.DecimalField(max_digits=10, decimal_places=2)
    # ticket_password = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.ticket_name
