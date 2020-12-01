from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150, null=True)
    password = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=150, null=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Role(models.Model):
    role = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.role


class Product(models.Model):
    CATEGORY = (
        ('dungeon', 'Dungeon'),
        ('raid', 'Raid'),
        ('pvp', 'PVP'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=80, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=10, null=True, choices=CATEGORY)
    description = models.TextField(max_length=600, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATE = (
        ('Vacant', 'Vacant'),
        ('In progress','In progress'),
        ('Done', 'Done'),
    )

    product = models.ForeignKey('Product', null=True, on_delete=models.SET_NULL)
    comment = models.TextField(max_length=300, blank=True, null=True)
    customer = models.ForeignKey('User', null=True, on_delete=models.SET_NULL, related_name='customer')
    contractor = models.ForeignKey('User', null=True, on_delete=models.SET_NULL, related_name='contracotor')
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    execution_date = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(null=True)
    state = models.CharField(max_length=12, null=True, choices=STATE, default=STATE[0][0])

    def __str__(self):
        return self.customer + ' - ' + self.product