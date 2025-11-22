from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Video(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500,default='',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default = 1)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name
