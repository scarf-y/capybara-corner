from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    chill_level = models.IntegerField()

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5