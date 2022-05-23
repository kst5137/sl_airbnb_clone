from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meata:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

class Type(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.name

class Product(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    type     = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    name     = models.CharField(max_length=200, db_index=True)
    slug     = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    addr     = models.TextField(blank=True)
    content  = models.TextField(blank=True)
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
        index_together = [['id','slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

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
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)


class Size(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'sizes'

    def __str__(self):
        return self.name

class ProductSizes(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size     = models.ForeignKey('Size', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_sizes'

class Attribute(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'attributes'

    def __str__(self):
        return self.name


class ProductAttributes(models.Model):
    product  = models.ForeignKey('Product', on_delete=models.CASCADE)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_attributes'

class Facility(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'facilities'

    def __str__(self):
        return self.name


class ProductFacilities(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    facility = models.ForeignKey('Facility', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_facilities'

class Rule(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'rules'

    def __str__(self):
        return self.name


class ProductRules(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rule     = models.ForeignKey('Rule', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_rules'

class Safety(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'safeties'

    def __str__(self):
        return self.name


class ProductSafeties(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    safety   = models.ForeignKey('Safety', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_safeties'