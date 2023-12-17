from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('tea', 'Чай'),
        ('coffee', 'Кава'),
        ('cocoa', 'Какао'),
        ('tableware', 'Посуд'),
        ('desserts', 'Десерти'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return f'{self.name} ({self.category}) - {self.price}'
