from django.db import models


class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)  # По батькові (необов'язкове поле)
    birthday_date = models.DateField(null=False)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)  # Припустимо, що номер телефону не більше 20 символів
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone_number}'
