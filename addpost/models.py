from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
diet_choices = (
    ('diabetic friendly', 'diabetic friendly'),
    ('eggetarian', 'eggetarian'),
    ('gluten free','gluten free'),

    ('high protein non vegetarian', 'high protein non vegetarian'),
    ('high protein vegetarian', 'high protein vegetarian'),

    ('no onion no garlic (sattvic)','no onion no garlic (sattvic)'),
    ('non vegetarian', 'non vegetarian'),
    ('vegan', 'vegan'),
    ('vegetarian', 'vegetarian')

)
course_choices = (
    ('appetizer', 'appetizer'),
    ('breakfast', 'breakfast'),
    ('dessert','dessert'),

    ('dinner', 'dinner'),
    ('lunch', 'lunch'),

    ('main course','main course'),
    ('one pot dish', 'one pot dish'),
    ('side dish', 'side dish'),
    ('snack', 'snack')

)

class Blog(models.Model):
    title = models.TextField()
    ingredients = models.TextField()
    body = models.TextField()
    # preptime = models.DecimalField(decimal_places=0, max_digits=3, default=0), 
    course = models.CharField(max_length=20, choices=course_choices, default='appetizer')
    diet = models.CharField(max_length=28, choices=diet_choices, default='diet')
    # describe the project 
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) :
        return (self.body)