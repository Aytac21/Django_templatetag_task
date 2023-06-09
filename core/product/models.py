from django.db import models
from ckeditor.fields import RichTextField



class Product(models.Model):
    name = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name