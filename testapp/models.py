from django.db import models


# Create your models here.

class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    img = models.ImageField(upload_to='pics')
    heading = models.CharField(max_length=250)
    desc = models.TextField()

    # def __str__(self):
    #     return self.name, self.desc

    def __str__(self):
        return self.heading, self.desc
