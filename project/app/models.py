from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name
class Biography(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    bio = models.TextField()
    def __str__(self):
        return f"Biography of {self.author.name}"
