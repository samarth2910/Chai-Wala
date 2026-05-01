from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Chai(models.Model):
    name = models.CharField(max_length=100)
    short_Description = models.CharField(max_length=200, default="")
    date_added = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='chai_images')
    description = models.TextField(default="")
    price= models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    CHAI_TYPE_OPTIONS = [
        ('gr', 'Green Tea'),
        ('bl', 'Black Tea'),
        ('mi', 'Milk Tea'),
        ('he', 'Herbal Tea'),
    ]
    
    type = models.CharField(max_length=2, choices=CHAI_TYPE_OPTIONS)

    def __str__(self):
        return self.name

#one to many
class Chai_Review(models.Model):
    chai = models.ForeignKey(Chai, on_delete=models.CASCADE,related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comments = models.TextField(default="")
    
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.chai.name} - {self.rating}"
    
class Store(models.Model):
    name = models.CharField(max_length=100,)
    location=models.CharField(max_length=200, default="")   
    chai = models.ManyToManyField(Chai, related_name="stores") 

    def str__(self):
        return self.name
    
#one to one
class  Chai_Certificate(models.Model):
    chai = models.OneToOneField(Chai, on_delete=models.CASCADE, related_name="certificate")
    certificate_number = models.CharField(max_length=50, unique=True)
    issued_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField()

    def __str__(self):
        return f"Certificate {self.certificate_number} for {self.chai.name}"
    
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    chai_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def subtotal(self):
        return self.price * self.quantity