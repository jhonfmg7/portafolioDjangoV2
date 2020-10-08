from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('career/', career, name='career'),
    path('discovery/', discovery, name='coming'),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success')
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
