from django.db import models
# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=150)
    translation = models.TextField()
    
    class Meta:
       verbose_name_plural = 'words'

    def __str__(self):
        return self.word
