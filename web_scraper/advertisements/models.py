from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    price = models.IntegerField(default=0)
    photo = models.CharField(max_length=100)
    link = models.CharField(max_length=100, unique=True)
    shop_name = models.CharField(max_length=50)
    shop = models.ForeignKey('Shops', default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        result = f'{self.name} {self.price} {self.photo} {self.link}'
        return result

    class Meta:
        db_table = 'Phones'


class Shops(models.Model):
    shop_name = models.CharField(max_length=50)

    def __str__(self):
        return self.shop_name

    class Meta:
        db_table = 'Shops'
