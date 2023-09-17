from django.db import models 

class Estate(models.Model):
    Image = models.CharField(max_length=200),
    Title = models.CharField(max_length=200),
    Location = models.CharField(max_length=200),
    AreaInner = models.CharField(max_length=200),
    BedroomsInner = models.CharField(max_length=200),
    Bathrooms = models.CharField(max_length=200),
    Price = models.CharField(max_length=200),

    def __str__(self): 
        return self.title