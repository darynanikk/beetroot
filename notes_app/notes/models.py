from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return f"Category: {self.title}"


class Note(models.Model):
    title = models.CharField(max_length=225)
    text = models.TextField()
    reminder = models.DateTimeField(blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="notes")

    def __str__(self):
        return f"Note: {self.title}"
