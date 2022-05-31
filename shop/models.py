from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

from config.settings import AUTH_USER_MODEL
from users.models import User
from django.conf import settings
from django.utils.text import slugify


class Category(models.Model):
    c_name = models.CharField(max_length=200, db_index=True)
    c_slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meata:
        ordering = ['c_name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.c_name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.c_slug])

    def get_absolute_url2(self):
        return reverse('shop:product_in_category', args=[self.c_slug])



class Type(models.Model):
    t_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.t_name

class Product(models.Model):
    writer = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    p_name = models.CharField(max_length=200, db_index=True)
    p_slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, null=True, blank=True)
    addr = models.TextField(blank=True)
    content = models.TextField(blank=True)
    address1 = models.CharField("Address line 1", max_length=300)
    address2 = models.CharField("Address line 2", max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=0, null=True)
    stock = models.IntegerField(default=1)
    size = models.ForeignKey('Size', on_delete=models.CASCADE, null=True)
    facility1 = models.BooleanField('Facility1', null=True, blank=True, default=False)
    facility2 = models.BooleanField('Facility2', null=True, blank=True, default=False)
    facility3 = models.BooleanField('Facility3', null=True, blank=True, default=False)
    facility4 = models.BooleanField('Facility4', null=True, blank=True, default=False)
    facility5 = models.BooleanField('Facility5', null=True, blank=True, default=False)
    rule1 = models.BooleanField('Rule1', null=True, blank=True, default=False)
    rule2 = models.BooleanField('Rule2', null=True, blank=True, default=False)
    rule3 = models.BooleanField('Rule3', null=True, blank=True, default=False)
    safety1 = models.BooleanField('Safety1', null=True, blank=True, default=False)
    safety2 = models.BooleanField('Safety2', null=True, blank=True, default=False)
    safety3 = models.BooleanField('Safety3', null=True, blank=True, default=False)
    display = models.BooleanField('Display', default=True)
    order = models.BooleanField('Order', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    checkin = models.DateTimeField(null=True, blank=True)
    checkout = models.DateTimeField(null=True, blank=True)

    class Meata:
        ordering = ['-created']
        index_together = [['id','p_slug']]

    def __str__(self):
        return self.p_name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.p_slug])


def path_image_path(instance, filename):
    #{instance.content} => {instance.product.content}
    return f'products/{instance.product.content}/{filename}'

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = ProcessedImageField(upload_to='products/%Y/%m/%d', null=False, processors=[ResizeToFill(120, 100)], format='JPEG', options={'quality':90})

class Inquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Size(models.Model):
    z_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'sizes'

    def __str__(self):
        return self.z_name

class ProductSizes(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size     = models.ForeignKey('Size', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_sizes'