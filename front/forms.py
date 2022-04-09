from django import forms
from .models import AccountingJournal
import django.forms.widgets


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AccountingJournalForm(forms.ModelForm):
	class Meta:
		model = AccountingJournal
		fields = ['journal', 'date', 'time', 'price', 'message']
		widgets= { 'date': DateInput(),'time': TimeInput()}
