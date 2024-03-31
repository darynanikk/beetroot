from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return f"Category: {self.title}"


class Note(models.Model):
    title = models.CharField(max_length=225)
    text = models.TextField()
    reminder = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes", null=True)
    categories = models.ManyToManyField(Category, related_name="notes")

    def __str__(self):
        return f"Note: {self.title}"
