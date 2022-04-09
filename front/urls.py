from django.urls import path
from . import views 


urlpatterns = [
    
    path('create', views.CreateJournalView.as_view(), name = 'create'),
    path('download', views.export_excel, name = 'download'),
    path('mail', views.send_mail_excel, name = 'mail'),
    path('list', views.JournalListView.as_view(), name = 'list'),

    
    ]