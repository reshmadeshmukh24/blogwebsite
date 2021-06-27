from django.db import models
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=80)
    slug=models.SlugField(max_length=50)
    description=models.TextField()


    def get_absolute_url(self):
        return reverse('hello',kwargs={'slug':self.slug})

