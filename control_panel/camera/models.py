from django.db import models

class Image(models.Model):
    text = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.text