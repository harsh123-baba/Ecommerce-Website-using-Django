from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length = 30)
    product_category = models.CharField(max_length=50 , default = "")
    product_subcategory = models.CharField(max_length=50, default="")
    product_img = models.ImageField(upload_to = "images/pics")
    product_description = models.CharField(max_length=2000)
    product_price= models.IntegerField(default=0)
    stock = models.IntegerField(default=100)
    
    def __str__(self):
        return self.product_name
    
    @property
    def imageUrl(self):
        try:
            url = self.product_img.url
        except:
            url=''
        return url

class Contact(models.Model):
    name = models.CharField(max_length=30, default="")
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15, default="")
    desc=models.CharField(max_length=300, default="")
    def __str__(self):
        return self.email

class Customer(models.Model):
    user = models.OneToOneField(User, null= True, blank = True, on_delete =models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    


class Order(models.Model):
    customer = models.ForeignKey(Customer , on_delete = models.SET_NULL, null= True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default= False, null = True)
    trasaction_id = models.CharField(max_length = 200, null =True)

    def __str__(self):
        return str(self.id)


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        items = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank = True, null =True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.product_price * self.quantity
        return total



    
class Checkout(models.Model):
    # product = models.ForeignKey(product, on_delete=models.SET_NULL, blank = True, null = True)
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank=True, null=True)
    # order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank = True, null =True)
    # quantity = models.IntegerField(default=0, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    







    
