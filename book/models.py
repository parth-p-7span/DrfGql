from django.db import models
from users.models import ExtendUser


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    author = models.ForeignKey(Author, default=1, on_delete=models.CASCADE)
    # owner = models.ForeignKey(ExtendUser, default=1, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.title
