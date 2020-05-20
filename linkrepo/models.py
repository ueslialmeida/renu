from django.db import models

# Create your models here.


class Link(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    notes = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title
