from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title




class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    age=models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True,max_length=225)
    occupation=models.CharField(null=True, blank=True,max_length=225)
    qualification=models.CharField(null=True, blank=True,max_length=225)
    expertise=models.CharField(null=True, blank=True,max_length=225)
    Current_Projects=models.CharField(null=True, blank=True,max_length=225)
    duration=models.CharField(null=True, blank=True,max_length=225)
    sponsorship=models.TextField(null=True, blank=True,max_length=225)
    Completed_project=models.TextField(null=True, blank=True,max_length=225)
    Year_of_Completion=models.CharField(null=True, blank=True,max_length=225)
    first_name=models.CharField(null=True, blank=True,max_length=225)
    last_name=models.CharField(null=True, blank=True,max_length=225)
    email_confirmed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, verbose_name="Category" ,on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.user.username 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Engineers(models.Model):
    category = models.ForeignKey(Category, verbose_name="Category" ,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True,max_length=225)
    occupation=models.CharField(null=True, blank=True,max_length=225)
    qualification=models.CharField(null=True, blank=True,max_length=225)
    expertise=models.CharField(null=True, blank=True,max_length=225)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
   

    def __str__(self):
        return self.user.username 


class Entrepreneur(models.Model):
    category = models.ForeignKey(Category, verbose_name="Category" ,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True,max_length=225)
    occupation=models.CharField(null=True, blank=True,max_length=225)
    qualification=models.CharField(null=True, blank=True,max_length=225)
    expertise=models.CharField(null=True, blank=True,max_length=225)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    


    def __str__(self):
        return self.user.username 

class Researchers(models.Model):

    category = models.ForeignKey(Category, verbose_name="Category" ,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True,max_length=225)
    occupation=models.CharField(null=True, blank=True,max_length=225)
    qualification=models.CharField(null=True, blank=True,max_length=225)
    expertise=models.CharField(null=True, blank=True,max_length=225)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
   


    def __str__(self):
        return self.user.username 

class Academician(models.Model):
    
    category = models.ForeignKey(Category, verbose_name="Category" ,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True,max_length=225)
    occupation=models.CharField(null=True, blank=True,max_length=225)
    qualification=models.CharField(null=True, blank=True,max_length=225)
    expertise=models.CharField(null=True, blank=True,max_length=225)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    


    def __str__(self):
        return self.user.username 

class Doctors(models.Model):

    category = models.ForeignKey(Category, verbose_name="Category" ,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True,max_length=225)
    occupation=models.CharField(null=True, blank=True,max_length=225)
    qualification=models.CharField(null=True, blank=True,max_length=225)
    expertise=models.CharField(null=True, blank=True,max_length=225) 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    

    def __str__(self):
        return self.user.username 


