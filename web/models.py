from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return str(self.name)


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    title = models.CharField(max_length=300)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    attachment = models.FileField(upload_to='books/')

    def __str__(self):
        return str(self.title)