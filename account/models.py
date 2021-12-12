from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import FileSystemStorage
def get_defaultDepartment():
    return Department.objects.get(name='Undistributed')
# picField = FileSystemStorage(location='/media/profile_photo')
class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=30,)
    department = models.CharField(max_length=50,blank=True)
    # department= models.ForeignKey('Department',on_delete=models.CASCADE,default=1)
    position = models.CharField( max_length=50,null=True)
    uni = models.CharField(max_length=50,null=True)
    phone_number =  models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    pic = models.ImageField(height_field=None, width_field=None, max_length=None,blank=True,default='/media/smile.png')
    profile = models.FileField(upload_to=None, max_length=100,blank=True)
    def __str__(self):
        return self.name
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        newAccount = Accounts.objects.create(user=instance,name=instance.username,email=instance.email)
    instance.accounts.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.accounts.save()


class Department(models.Model):
    name = models.CharField(max_length=30)
    introduction = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.name
 
