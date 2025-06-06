from django.db import models
from PIL import Image
import os
from django.conf import settings

# Create your models here.

class Projects(models.Model):
    image = models.ImageField(upload_to='project_images/')
    name = models.CharField(max_length=50)
    sub_text= models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        # Delete the file from filesystem
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        
        # Call the parent delete method
        super().delete(*args, **kwargs)