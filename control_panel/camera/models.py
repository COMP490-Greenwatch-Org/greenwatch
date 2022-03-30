from django.db import models

class Camera(models.Model):
    name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

class Image(models.Model):
    camera = models.ForeignKey(Camera, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 10)
    image = models.ImageField(null=True)
    results = models.CharField(max_length = 100, null = True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name