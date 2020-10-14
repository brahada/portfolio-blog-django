from django.db import models
from django.forms import ModelForm
from django.utils.timezone import now
SUB_CHOICES = (
    ('d', 'Deals'),
    ('j', 'Jobs'),
)
class Contact(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender",null=True)
    email = models.EmailField(max_length=200,null=True)
    subject = models.CharField(max_length=1, choices=SUB_CHOICES)
    message = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.name + "-" +  self.email
'''
STATUS_CHOICES = (
    ('d', 'Deals'),
    ('j', 'Jobs'),
)
class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    content = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
# Create your models here.
'''
