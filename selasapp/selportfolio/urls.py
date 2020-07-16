from django.urls import include, path
from app_name import views
 
app_name = 'selportfolio'
 
urlpatterns = ['C:\Users\selas moro\Desktop\django_project\selasapp\selportfolio\urls.py'
]
from django.urls import include, path
from app_name import views
 
app_name = 'selportfolio'
 
urlpatterns = [
    path('contact_form',views.contact_form,name='contact_form'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('contact_form_submit',views.contact_form_submit,name='contact_form_submit'),
    path('all_data',views.all_data,name='all_data'),

]
 

