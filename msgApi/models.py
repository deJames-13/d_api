from django.db import models

# Create your models here.
class Message(models.Model):
    msg = models.TextField(null=True, blank=True)
    day = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.msg
    
    
