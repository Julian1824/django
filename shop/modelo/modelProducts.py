from django.db import models
from django.core.validators import RegexValidator

class Products(models.Model):
    name = models.CharField(max_length=20)
    cod_product = models.CharField(
              max_length=20,
        validators=[RegexValidator(
            regex='^[0-9]*$',
            message='El ID del prodcuto solo puede contener números.',
            code='invalid_id'
        )]
    )
    cant = models.CharField(
              max_length=4,
        validators=[RegexValidator(
            regex='^[0-9]*$',
            message='La cantidad solo puede contener números.',
            code='invalid_id'
        )]
    )


    def __str__(self):
        return self.name