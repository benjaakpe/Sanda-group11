from django.db import models

# Create your models here.
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User



Addresses_TYPES = (
    ('billing', 'Billing Addresses'),
    ('shipping', 'Shipping Addresses'),
)

Payment_STATUS_CHOICES = (
    ('In progress', 'In progress'),
    ('Completed', 'Completed'),
)

Payment_Method_CHOICES = (
    ('Credit card', 'credit card'),
    ('Debit card', 'Debit card'),
)

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


# Customer table
class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user.username)


#
# @receiver(post_save, sender=User)
# def create_user_customer(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_customer(sender, instance, **kwargs):
#     instance.customer.save()


Payment_STATUS_CHOICES = (
    ('In progress', 'In progress'),
    ('Completed', 'Completed'),
)

Payment_Method_CHOICES = (
    ('Credit card', 'credit card'),
    ('Debit card', 'Debit card'),
)

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


# category table
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()

    def __str__(self):
        return str(self.category_id)


# payment table
class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True,)
    order_id = models.ForeignKey(Category, on_delete=models.RESTRICT)
    payment_method = models.CharField(max_length=120, choices=Payment_Method_CHOICES)
    payment_status = models.CharField(max_length=120, choices=Payment_STATUS_CHOICES)

    def __str__(self):
        return str(self.payment_id)


# Addresses table
class Addresses(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True, help_text='Shipping to? Who is it for?')
    shipping_Addresses = models.CharField(max_length=120, choices=Addresses_TYPES, primary_key=True)
    billing_Addresses = models.CharField(max_length=120, choices=Addresses_TYPES)
    Addresses_line_1 = models.CharField(max_length=120)
    Addresses_line_2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default='United States of America')
    state = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        if self.name:
            return str(self.name)
        return str(self.Addresses_line_1)

    def get_absolute_url(self):
        return reverse("Addresses-update", kwargs={"pk": self.pk})

    def get_short_Addresses(self):
        for_name = self.name
        return "{for_name} {line1}, {city}".format(
            for_name=for_name or "",
            line1=self.Addresses_line_1,
            city=self.city
        )

    def get_Addresses(self):
        return "{for_name}\n{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
            for_name=self.name or "",
            line1=self.Addresses_line_1,
            line2=self.Addresses_line_2 or "",
            city=self.city,
            state=self.state,
            postal=self.postal_code,
            country=self.country
        )


# Orders table
class Order(models.Model):
    order_id = models.CharField(max_length=120, primary_key=True)
    cust_id = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    payment_id = models.ForeignKey(Payment, on_delete=models.RESTRICT)
    shipping_Addresses = models.ForeignKey(Addresses, on_delete=models.RESTRICT)
    # I think we need to discuss the billing address
    billing_Addresses = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(max_digits=100, decimal_places=2, null=False)
    order_total = models.DecimalField(max_digits=100, decimal_places=2, null=False)
    active = models.BooleanField(default=True)
    date_placed = models.DateTimeField(auto_now=True)
    date_shipped = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)


# Product table
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=120)
    product_description = models.TextField()
    product_price = models.DecimalField(decimal_places=2, max_digits=20, null=False)
    product_category = models.CharField(max_length=120)
    product_catalog = models.CharField(max_length=120, null=False)
    remaining_quantity = models.IntegerField(default=1000)

    def __str__(self):
        return str(self.product_id)


# Order details table
class OrderDetail(models.Model):
    order_details_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=100, decimal_places=2, null=False)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.order_details_id)


# Cart Table
class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_total = models.IntegerField()

    def __str__(self):
        return str(self.cart_id)


# Favorites Table
class Favorite(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    # Not sure we need this
    # def __str__(self):
    #     return str(self.cust_id)


