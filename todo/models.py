from django.db import models
from django.conf import settings 



# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField(max_length=101,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
    
    
   
    
    def __str__(self):
        return self.title

    