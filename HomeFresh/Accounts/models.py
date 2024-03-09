from django.contrib.auth.models import AbstractUser, Group,Permission
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/',null=True)
    is_producer = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(unique=True)  # Added email field
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(Group, blank=True, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="customuser_user_permissions")

    def __str__(self):
        return self.email

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_verified = models.BooleanField(default=False)

    QUANTITY_CHOICES = (
        ('Kilogram', 'Kilogram'),
        ('Liter', 'Liter'),
        ('Pieces', 'Pieces'),
    )
    quantity = models.CharField(max_length=20, choices=QUANTITY_CHOICES)
    producer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Location(models.Model):
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.district}, {self.state}"

class Producer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class Review(models.Model):
    reviewer = models.ForeignKey(CustomUser, related_name='reviews', on_delete=models.CASCADE)
    producer = models.ForeignKey(CustomUser, related_name='product_reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    star_count = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_allowed = models.BooleanField(default=False)
