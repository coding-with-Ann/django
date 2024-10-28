from django.db import models
from django.utils import timezone

# Create your models here.
class coffeeVariety(models.Model):

    COFFEE_TYPE_CHOICE = [
        ('CL', 'chocolate'),
        ('GR', 'ginger'),
        ('KI', 'kiwi'),
        ('PL', 'plain')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='coffees/') 
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=COFFEE_TYPE_CHOICE)
    #we have to tell settings.py that we are using media. 
    # we have to define it in settings.py
    description = models.TextField(default='') # by default descriptuon is empty when default = ''
    # since we have changed database structure(added a new field i-e description to database) we have 
    # to run the commnad < python3 manage.py makemigrations coffee > and 
    # < python3 manage.py migrate >


    def __str__(self):
        return self.name
