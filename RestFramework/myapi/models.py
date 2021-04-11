from django.db import models


class Product(models.Model):
    product_code = models.CharField(max_length=100,default= '')
    category_names = models.CharField(max_length=100,default = '')
    sub_category1   = models.CharField(max_length=100,default = '')
    sub_category2   = models.CharField(max_length=100,default = '')
    product_name   = models.CharField(max_length=100,default = '')
    product_price   = models.IntegerField(max_length=100,default = 0)

    def __str__(self):
        return super().__str__()
