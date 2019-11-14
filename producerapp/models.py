
# Create your models here.
from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        return super(CustomManager, self).get_queryset().\
            filter(book_qty__gte=12)

class Books(models.Model):
    book_name = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30)
    book_publication = models.CharField(max_length=30)
    book_qty= models.IntegerField()
    book_price = models.FloatField()

    class Meta:
        db_table="book_details"
