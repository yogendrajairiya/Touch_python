from django.db import models
from django.utils import timezone
# Create your models here.
class TouchVariety(models.Model):
    TOUCH_CHOICES = [
        ('HA', 'Haptic'),
        ('VI', 'Visual'),
        ('AU', 'Auditory'),
        ('OL', 'Olfactory'),
        ('GU', 'Gustatory'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='touch_images/', blank=True, null=True)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=TOUCH_CHOICES)
    date_added = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

def __str__(self):
    return self.name