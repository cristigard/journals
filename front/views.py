from django.shortcuts import render
from .forms import AccountingJournalForm
from .models import AccountingJournal
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.urls import reverse_lazy
from django.conf import settings
from io import BytesIO
import xlwt
from django.template.loader import render_to_string
from weasyprint import HTML
from django_renderpdf.views import PDFView
import tempfile
import datetime


class CreateJournalView(LoginRequiredMixin, CreateView):
	model = AccountingJournal
	form_class = AccountingJournalForm
	template_name = 'front/create-journal.html'
	success_url = reverse_lazy('list')

	#add user to form before save in db
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class JournalListView(LoginRequiredMixin, ListView):
	model = AccountingJournal
	template_name = 'front/list-journal.html'
	context_object_name = 'journals'

	#return queryset for specific condition
	def get_queryset(self,*args, **kwargs):
		if self.request.user.is_admin:
			#admin user can retrive all users data
			queryset = AccountingJournal.objects.all()
		else:
			#authenticated user can retrive his own data
			queryset = AccountingJournal.objects.filter(author = self.request.user)
		return queryset


@login_required
def export_excel(request):
	# create a file of ms-excel type
	response = HttpResponse(content_type='application/ms-excel')
	#decide file name
	# response['Content-Disposition'] = 'attachment; filename="journal.xls"'
	response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
	#creating workbook
	wb = xlwt.Workbook(encoding='utf-8')
	#adding sheet
	ws = wb.add_sheet("sheet1")
	# Sheet header, first row
	row_num = 0
	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True
	#column header names
	columns = ['Id', 'Owner','Journal', 'Date', 'Time', 'Price', 'Message']
	#write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()
	#admin can retrive all users data
	if request.user.is_admin:
		#admin user can retrive all users data
		data = AccountingJournal.objects.all()
	else:
		#authenticated user can retrive his own data
		data = AccountingJournal.objects.filter(author = request.user)
	#get data from database / write to xml
	for row in data:
		row_num += 1
		ws.write(row_num, 0, str(row.id), font_style)
		ws.write(row_num, 1, str(row.author.username), font_style)
		ws.write(row_num, 2, str(row.journal), font_style)	
		ws.write(row_num, 3, str(row.date), font_style)
		ws.write(row_num, 4, str(row.time), font_style)
		ws.write(row_num, 5, str(row.price), font_style)
		ws.write(row_num, 6, str(row.message), font_style)
	wb.save(response)
	return response


@login_required
def send_mail_excel(request):
	#save workbook object to a BytesIO instance(required in mail attached file)
	excelfile = BytesIO()
	#creating workbook
	wb = xlwt.Workbook(encoding='utf-8')
	#adding sheet
	ws = wb.add_sheet("sheet1")
	# Sheet header, first row
	row_num = 0
	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True
	#column header names
	columns = ['Id','Owner','Journal', 'Date', 'Time', 'Price', 'Message']
	#write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)
	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()
	if request.user.is_admin:
		#admin user can retrive all users data
		data = AccountingJournal.objects.all()
	else:
		#authenticated user can retrive his own data
		data = AccountingJournal.objects.filter(author = request.user)
	#get data from database / write to xml
	for row in data:
		row_num += 1
		ws.write(row_num, 0, str(row.id), font_style)
		ws.write(row_num, 1, str(row.author.username), font_style)
		ws.write(row_num, 2, str(row.journal), font_style)	
		ws.write(row_num, 3, str(row.date), font_style)
		ws.write(row_num, 4, str(row.time), font_style)
		ws.write(row_num, 5, str(row.price), font_style)
		ws.write(row_num, 6, str(row.message), font_style)
	wb.save(excelfile)
	#send mail
	subject = 'Accounting Journal'
	message = 'Your accounting journal'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [request.user,]
	mail = EmailMessage(subject, message, email_from, recipient_list,)
	mail.attach('journal.xls', excelfile.getvalue(), 'application/vnd.ms-excel')
	mail.send()
	return render(request, 'front/mail-confirm.html')



class ExportPDF(LoginRequiredMixin, PDFView):
	# https://django-renderpdf.readthedocs.io/en/latest/
	template_name = 'front/pdf.html'
	prompt_download = True

	def url_fetcher(url):
		print(url)
		return url

	@property
	#work if prompt_download = True
	def download_name(self):
		return f"{datetime.date.today()} - jurnal.pdf"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		if self.request.user.is_admin:
			#admin user can retrive all users data
			data = AccountingJournal.objects.all()
		else:
			#authenticated user can retrive his own data
			data = AccountingJournal.objects.filter(author = self.request.user)
		context['journals'] = data
		return context

