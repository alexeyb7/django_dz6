from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    client_reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        # return f'Client:{self.name}, e-mail:{self.email}, phone:{self.phone}, addr:{self.address}'
        return self.name


class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_desc = models.CharField(max_length=100)
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)
    prod_quant = models.DecimalField(max_digits=10, decimal_places=2)
    prod_reg_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)

    def __str__(self):
        return self.prod_name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    sum_order = models.FloatField()
    order_date = models.DateField(auto_now_add=True)

    def calculate_total_amount(self):
        total = sum(product.prod_price * product.prod_quant for product in self.products.all())
        self.sum_order = total
        self.save()

    def __str__(self):
        return f'Order {self.id} by {self.client.name}'

