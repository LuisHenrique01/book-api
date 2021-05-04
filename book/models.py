from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class PublishingCompany(models.Model):

    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "publishing company"
        verbose_name_plural = "publishers companies"

    def __str__(self):
        return self.name

    
class Book(models.Model):

    title = models.CharField(max_length=150)
    isbn = models.CharField(max_length=17)
    author = models.ManyToManyField(Author)
    publishing_company = models.ForeignKey(PublishingCompany, on_delete=models.CASCADE)
    number_of_pages = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
