from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    def _str_(self):
        return self.name;

class About_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    def _str_(self):
        return self.name;


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_type = models.CharField(max_length=10, choices=[('Free', 'Free'), ('Pay', 'Pay')])
    image = models.ImageField(upload_to='course/')
    author_image = models.ImageField(upload_to='author/')

    def __str__(self):
        return self.title;
