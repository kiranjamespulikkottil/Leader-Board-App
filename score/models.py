from django.db import models
from django.urls import reverse

class Score(models.Model):
    class Meta:
        ordering = ['-score']
    name = models.CharField(max_length=250)
    score = models.IntegerField()

    def get_absolute_url(self):
        return reverse('score_detail', args=[str(self.id)])

    def __str__(self):
        return self.name
