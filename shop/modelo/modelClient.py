from django.db import models
from django.core.validators import RegexValidator

class Client(models.Model):
    id_number = models.CharField(
              max_length=20,
        validators=[RegexValidator(
            regex='^[0-9]*$',
            message='El ID del empleado solo puede contener números.',
            code='invalid_id'
        )]
    )
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    date_birhday = models.DateTimeField(auto_now_add = False)

    def __str__(self):
        return self.name