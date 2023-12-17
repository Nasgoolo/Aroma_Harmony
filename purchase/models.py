from django.db import models
from user.models import User  # Припускається, що у вас є додаток "user" з моделлю користувача
from product.models import Product  # Припускається, що у вас є додаток "product" з моделлю продукту


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchase'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.product.name} ({self.purchase_date})'

