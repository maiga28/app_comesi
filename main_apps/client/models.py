from django.contrib.auth.models import AbstractUser
from django.db import models
from main_apps.gestion.models import Product, Order

class Client(AbstractUser):
    orders = models.ManyToManyField('gestion.Order', through='ClientOrder', related_name='clients')
    photo = models.ImageField(upload_to='profile_pics/', blank=True)
    adresse = models.CharField(max_length=30)
    numero_telephone = models.CharField(max_length=15)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)
    cover_picture = models.ImageField(upload_to='cover_picture/', blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='client_set',  # Add a unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='client_set',  # Add a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'numero_telephone']

    def __str__(self):
        return f"{self.username}"

    
class ClientOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order = models.ForeignKey('gestion.Order', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.client.username}, {self.order.id}"
