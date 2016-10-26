from django.db import models

# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)

    def __str__():
        return '{}'.format(self.author)
