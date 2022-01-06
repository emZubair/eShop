from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=32, unique=True, db_index=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()
    total_coupons = models.PositiveIntegerField(default=3)
    availed_coupons = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Coupon code:{self.code}"
