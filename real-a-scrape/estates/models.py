from django.db import models 

class Estate(models.Model):
    Image = models.CharField(max_length=200, default='')
    Title = models.CharField(max_length=200, default='')
    Location = models.CharField(max_length=200, default='')
    AreaInner = models.CharField(max_length=200, default='')
    BedroomsInner = models.CharField(max_length=200, default='')
    Bathrooms = models.CharField(max_length=200, default='')
    Price = models.CharField(max_length=200, default='')

    def __str__(self): 
        return self.title