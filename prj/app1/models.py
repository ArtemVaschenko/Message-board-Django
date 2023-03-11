from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=150, blank=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    price = models.IntegerField(default=1)
    description = models.TextField(blank='This item has no description')
    item_img = models.ImageField(upload_to='static/images')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contact = models.CharField(max_length=150, default='None', blank=False, null=True)

    def __str__(self):
        return f'Id {self.pk} name: {self.name} price: {self.price}'

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})

