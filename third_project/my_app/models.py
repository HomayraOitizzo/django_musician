from django.db import models
from django.urls import reverse
# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    
    def get_absolute_url(self):
        return reverse('musician_details', kwargs={'pk':self.pk})


    
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_list')
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    
    rating = (
        (1, "worst"),
        (2, "Bad"),
        (3, "Average"),
        (4, "Good"),
        (5, "Excellent"),
    )
    num_stars = models.IntegerField(choices=rating, default=1)