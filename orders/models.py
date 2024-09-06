from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    timeToCook = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    personName = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through='OrderProduct')
    quantity = models.IntegerField()

    @property
    def total_cooking_time(self):
        return sum(order_product.product.timeToCook * order_product.quantity for order_product in self.orderproduct_set.all())

    def __str__(self):
        return self.personName

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()