from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from account.models import Accounts
import datetime
# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30,default='None')
    short_descipt = models.CharField(max_length=200)
    expected_number = models.IntegerField(default=5)
    registered_members = models.ManyToManyField(Accounts) 
    # content = RichTextField()
    post = models.TextField(default=None)
    # content_html = models.TextField(blank=True, editable=False)
    hold_time = models.DateField(default = datetime.date.today)
    publish_time = models.DateTimeField(auto_now_add=True)
    last_edit_time = models.DateTimeField(auto_now=True)
    deadline =  models.DateTimeField(default = timezone.now)
    passed = models.BooleanField(default=False)
    comment = models.CharField(max_length=200,default = None,blank=True,null=True)
    comment_user = models.CharField(max_length=30,blank=True,default=None,null=True)
    pic = models.ImageField(height_field=None, width_field=None, max_length=None,blank=True,null=True,default='/media/smile.png')
    
    def __str__(self):
        return self.title

        