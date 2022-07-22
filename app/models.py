from django.db import models
from django.db.models import Sum,Window,F
from django.contrib.auth.models import User
import datetime

from numpy import product

# 顧客クラス
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_app_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"""ID:{self.id}, {self.customer_name}, 登録日:{self.customer_app_date}"""

# 商品クラス
class Products(models.Model):
    products_name = models.CharField(max_length=50)
    best_before_duration = models.IntegerField()
    product_app_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"""ID:{self.id}, {self.products_name}, 賞味 {self.best_before_duration}日, 登録日:{self.product_app_date}"""

# 製造クラス
class Production(models.Model):
    products_name = models.ForeignKey(Products, on_delete=models.CASCADE)
    production_date = models.DateField()
    production_volume = models.IntegerField()
    
    def __str__(self):
        return f"""ID:{self.id}, {self.products_name}, 製造日:{self.production_date}, 製造量:{self.production_volume}cs"""

# 販売クラス
class Sale(models.Model):
    products_name = models.ForeignKey(Products, on_delete=models.CASCADE)
    production_date = models.ForeignKey(Production, on_delete=models.CASCADE)
    best_before_duration = models.ForeignKey(Products, on_delete=models.CASCADE)
    best_before_date = models.IntegerField()
    customer_name = models.OneToOneField(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField()
    sale_volume = models.IntegerField()
    sale_price = models.IntegerField()
    unit_price = models.IntegerField()

    def save(self, *args, **kwargs):
        self.unit_price = self.sale_price / self.sale_volume
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"""ID:{self.id}, {self.products_name}, 製造日:{self.production_date}, 賞味期限:{self.production_date + datetime.timedelta(days=self.best_before_duration)} /
        顧客名:{self.customer_name}, 販売日:{self.sale_date}, 販売量:{self.sale_volume}, 単価:{self.unit_price}"""

# 在庫クラス
class Stock(models.Model):
    products_name = models.ForeignKey(Products, on_delete=models.CASCADE)
    production_date = models.ForeignKey(Production, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()
    
    def __str__(self):
        return f"""ID:{self.id}, {self.products_name}, 賞味 {self.best_before_duration}日, 登録日:{self.product_app_date}"""


