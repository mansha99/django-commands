from django.db import models
class BlogHeader(models.Model):
   alt = models.CharField(max_length=255)
   image_path=models.CharField(max_length=255)
   dimension_checked = models.BooleanField(default=False) 
   has_correct_dimension = models.BooleanField(default=False) 
   def __str__(self):
        return self.alt