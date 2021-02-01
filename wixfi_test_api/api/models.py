from django.db import models


class User(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='First name',
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='Last name',
    )
    email = models.CharField(
        max_length=50,
        verbose_name='Email',
    )
    password = models.CharField(
        max_length=50,
        verbose_name='Password',
    )
    referral_code = models.CharField(
        max_length=5,
        blank=True,
        verbose_name='Referral code',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
