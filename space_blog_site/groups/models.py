from django.db import models

# Create your models here.
class GroupSubject(models.Model):
    title = models.CharField(max_length = 250)
    content = models.TextField()
    group_subscribers = models.ForeignKey('accounts.Customer', on_delete = models.CASCADE)
    
