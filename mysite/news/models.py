from django.db import models

# Create your models here.
class News(models.Model):
    heading = models.CharField(max_length=250)
    links = models.URLField()

    def __str__(self):
        return self.heading
