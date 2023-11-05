from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=15)
    author = models.CharField(max_length=15)
    content = models.TextField()
    publish_date = models.DateTimeField()
    
    def __str__(self):
        return self.author

