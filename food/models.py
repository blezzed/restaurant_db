from django.db import models


# Create your models here.

class Food(models.Model):
    MEAL = (
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Super", "Super")
    )
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0.00)
    stars = models.IntegerField(default=3)
    image = models.ImageField(default='', null=True, blank=True)
    meal = models.CharField(max_length=200, null=True, choices=MEAL)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Mete:
        ordering = ['-updated']
