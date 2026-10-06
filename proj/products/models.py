from django.db import models

class Products(models.Model):
    CHOICES=[
        ('SMARTPHONES','Smartphones'),
        ('CHARGERS','Chargers'),
        ('BACKCOVER','Backcover')
    ]
    name=models.CharField(max_length=225)
    desc=models.TextField()
    category=models.CharField(max_length=225,choices=CHOICES)
    tags=models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return self.category
    