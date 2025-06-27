from django.db import models

# start writing your models below

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'"{self.text[:50]}..."- {self.author}'
    
