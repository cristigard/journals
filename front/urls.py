from django.urls import path
from . import views 


urlpatterns = [
    
    path('create', views.CreateJournalView.as_view(), name = 'create'),
    path('excel', views.export_excel, name = 'excel'),
    path('pdf', views.export_pdf, name = 'pdf'),
    path('mail', views.send_mail_excel, name = 'mail'),
    path('list', views.JournalListView.as_view(), name = 'list'),
    
    ]