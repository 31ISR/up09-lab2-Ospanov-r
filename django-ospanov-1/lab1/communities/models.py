from django.db import models
# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=150)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField(default=True)
    avatar = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.name