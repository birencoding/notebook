from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):

    title = models.CharField(max_length=100)
    # subtitle = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']  # Order by creation date, newest first