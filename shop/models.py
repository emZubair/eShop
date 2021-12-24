from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', null=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%m/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_details', args=[self.id, self.slug])
