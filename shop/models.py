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

class Type(models.Model):
    t_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.t_name

class Product(models.Model):
    writer = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    type     = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    p_name     = models.CharField(max_length=200, db_index=True)
    p_slug     = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, null=True, blank=True)
    addr     = models.TextField(blank=True)
    content  = models.TextField(blank=True)
    address1 = models.CharField("Address line 1", max_length=300)
    address2 = models.CharField("Address line 2", max_length=300)
    price    = models.DecimalField(max_digits=8, decimal_places=0, null=True)
    stock    = models.IntegerField(default=1)
    size     = models.ForeignKey('Size', on_delete=models.CASCADE, null=True)
    attribute= models.ForeignKey('Attribute', on_delete=models.CASCADE, null=True)
    facility = models.ForeignKey('Facility', on_delete=models.CASCADE, null=True)
    rule     = models.ForeignKey('Rule', on_delete=models.CASCADE, null=True)
    safety   = models.ForeignKey('Safety', on_delete=models.CASCADE, null=True)
    display = models.BooleanField('Display', default=True)
    order = models.BooleanField('Order', default=True)
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meata:
        ordering = ['-created']
        index_together = [['id','p_slug']]

    def __str__(self):
        return self.p_name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.p_slug])


# class ProductImage(models.Model) :
#     productImage = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='products/%Y/%m/%d')

def path_image_path(instance, filename):
    #{instance.content} => {instance.product.content}
    return f'products/{instance.product.content}/{filename}'

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = ProcessedImageField(upload_to='products/%Y/%m/%d', null=False, processors=[ResizeToFill(120, 100)], format='JPEG', options={'quality':90})

class Inquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
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

class Attribute(models.Model):
    a_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'attributes'

    def __str__(self):
        return self.a_name


class ProductAttributes(models.Model):
    product  = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_attributes'

class Facility(models.Model):
    f_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'facilities'

    def __str__(self):
        return self.f_name


class ProductFacilities(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    facility = models.ForeignKey('Facility', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_facilities'

class Rule(models.Model):
    r_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'rules'

    def __str__(self):
        return self.r_name


class ProductRules(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rule     = models.ForeignKey('Rule', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_rules'

class Safety(models.Model):
    s_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'safeties'

    def __str__(self):
        return self.s_name


class ProductSafeties(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    safety   = models.ForeignKey('Safety', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_safeties'