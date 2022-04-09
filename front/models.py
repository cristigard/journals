from django.db import models
from users.models import CustomUser

CHOICES = (
    ('Vanzari','Vanzari'),
    ('Cumparari','Cumparari'),
    ('Balanta', 'Balanta'))

class AccountingJournal(models.Model):
	journal = models.CharField('Type: ',max_length=30, choices=CHOICES)
	date = models.DateField('Date: ')
	time = models.TimeField('Time: ')
	price = models.DecimalField('Price: ',max_digits=10, decimal_places=2)
	message = models.TextField('Message: ')
	author = models.ForeignKey(CustomUser, on_delete = models.CASCADE)

