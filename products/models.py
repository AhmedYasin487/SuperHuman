from django.db import models
from superhuman.utils import unique_slug_generator
from django.db.models.signals import pre_save
# To handle with files you can you the following funtions. they will change the path of a file.
import random
from django.urls import reverse
import os

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance, filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(0,99999999999)
    name, ext =get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)
# Create your models here.

class ProductManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(feature=True)

    def get_by_id(self,pk):
        qs = self.get_queryset().filter(pk=pk)
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):

    title = models.CharField( max_length=50)
    slug = models.SlugField(blank =True,unique = True)
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2, default = 39.99)
    image = models.ImageField( upload_to=upload_image_path, height_field=None, width_field=None, max_length=None,blank = True,null = True)
    feature = models.BooleanField(blank=True,null=True)
    
    objects = ProductManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self,*args, **kwargs):
        return reverse("products:product_detail", kwargs={"slug": self.slug})


    

    

def product_pre_save_reciever(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever,Product)
    

