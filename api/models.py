from django.db import models
from django.contrib.gis.db import models
from datetime import datetime

STATE_CHOICES = (
    ('Por Validar','Por Validar'),
    ('Validado', 'Validado'),
    ('Resolvido','Resolvido'),
)

CATEGORY_CHOICES = (
    ('CONSTRUCTION','CONSTRUCTION'),
    ('SPECIAL_EVENT', 'SPECIAL_EVENT'),
    ('INCIDENT','INCIDENT'),
    ('WEATHER_CONDITION','WEATHER_CONDITION'),
    ('ROAD_CONDITION','ROAD_CONDITION'),
)

class Occurrence(models.Model):
    
    description=models.CharField(max_length=200)
    location = models.PointField()
    author=models.CharField(max_length=200)
    creationDate=models.DateTimeField(default=datetime.now())
    updateDate=models.DateTimeField(default=datetime.now())
    state = models.CharField(max_length=50, choices=STATE_CHOICES, default='Por Validar')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    def save(self, *args, **kwargs):
        self.author = 'user'
        super().save(*args, **kwargs) 
    
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.author + ', ' + self.state + ', ' + self.category + ' - ' + self.description 