from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, max_length=200, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name

class Book(models.Model):
    bookname = models.CharField(max_length=1000, null=True)
    price = models.FloatField()
    book_image = models.ImageField(null=True)

    def __str__(self):
        return self.bookname

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, blank=True, on_delete=models.SET_NULL, null=True)
    transaction_id = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_items_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, max_length=100, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, max_length=1000, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def get_total(self):
        total = self.book.price * self.quantity
        return total


class Shipping(models.Model):
    customer = models.ForeignKey(Customer, blank=True, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, blank=True, on_delete=models.SET_NULL, null=True)
    Address = models.CharField(max_length=10, null=True)
    City = models.CharField(max_length=10, null=True)

