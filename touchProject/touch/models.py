from django.db import models
from django.utils import timezone
# Create your models here.
class TouchVariety(models.Model):
    TOUCH_CHOICES = [
        ('Haptic', 'Haptic'),
        ('Visual', 'Visual'),
        ('Auditory', 'Auditory'),
        ('Olfactory', 'Olfactory'),
        ('Gustatory', 'Gustatory'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='touch_images/', blank=True, null=True)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=TOUCH_CHOICES, default='Haptic')
    date_added = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Touch Variety'
        verbose_name_plural = 'Touch Variety'
        ordering = ['-created_at']  # Order by creation date, newest first