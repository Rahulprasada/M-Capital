from django.db import models

class stock(models.Model):
    heading = models.CharField(max_length=30)
    content = models.TextField()
    url = models.URLField( blank=True, null=True)
    
    
    def __str__(self):
        return self.heading
    