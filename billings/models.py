from django.db import models
from django.db.models.signals import post_save
from django.contrib import auth
# Create your models here.

class BillingProfile(models.Model):

    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE,blank=True,null=True)
    email = models.EmailField(max_length=254)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.email

def user_create_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_create_receiver,sender=auth.models.User)


  
