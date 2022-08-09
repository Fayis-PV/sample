from django.db import models
from django.contrib.auth.models import User


# # Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    # name = models.CharField(max_length=200)
    # email = models.EmailField()

    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    username = models.CharField(max_length=50,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    password = models.CharField(max_length=200,blank=True,null=True)

    # def __str__(self):
    #     return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_img = models.ImageField(upload_to='imgs')
    product_price = models.IntegerField()
    product_description = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

    @property
    def image_url(self):
        try:
            url = self.product_img.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    ordered_date = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_all_total(self):
        orderitems = self.orderitems_set.all()
        total = sum([item.total_price for item in orderitems])
        return total

    @property
    def get_items_count(self):
        orderitems = self.orderitems_set.all()
        total = sum([items.quantity for items in orderitems])
        return total

    @property
    def each_orderitems_quantity(self,**kwargs):
        order_items = self.orderitems_set.all()
        for each in order_items:
            quantity =each.quantity
        return quantity


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)


    @property
    def total_price(self):
        return self.quantity * self.product.product_price

    @property
    def delete_item(self):
        self.quantity = 0
        # return


class CheckOut(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    date_added = models.DateField(auto_now_add=True)
    transaction_id = models.IntegerField(blank=True,null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id)


class CheckOutItems(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    checkout = models.ForeignKey(CheckOut,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def total_price(self):
        return self.quantity*self.product.product_price


class Contact(models.Model):
    customer = models.ForeignKey(Customer,on_delete= models.SET_NULL, blank= True , null= True)
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_number = models.BigIntegerField()
    contact_message = models.CharField(max_length=1000)
    contact_date = models.DateTimeField(auto_now_add=True)
