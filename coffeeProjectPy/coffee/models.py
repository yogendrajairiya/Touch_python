from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class CoffeeVariety(models.Model):
    COFFEE_TYPE_CHOICES = [
        ('ES', 'Espresso'),
        ('AM', 'Americano'),
        ('LA', 'Latte'),
        ('CA', 'Cappuccino'),
        ('MO', 'Mocha'),
        ('FL', 'Flat White'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='coffee_images/', blank=True, null=True)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=COFFEE_TYPE_CHOICES)
    date_added = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


# One to Many relationship
class CoffeeReview(models.Model):
    coffee_variety = models.ForeignKey(CoffeeVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.coffee_variety.name}'
    

# Many to Many relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    coffee_varieties = models.ManyToManyField(CoffeeVariety, related_name='stores')
    image = models.ImageField(upload_to='store_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
# One to One relationship
class CoffeeCertificate(models.Model):
    coffee  = models.OneToOneField(CoffeeVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50, unique=True)
    issued_by = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    
    def __str__(self):
        return f'Certificate for {self.coffee.name} - {self.certificate_number}'
    
    