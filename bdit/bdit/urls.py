"""
URL configuration for bdit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home,aboutus,contact
from vege.views import receipe,delete_receipe,update_receipe

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home , name='home'),

    path('aboutus/', aboutus, name='aboutus'),
    path('contact/', contact, name='contact'),
   

    path('receipe/', receipe, name='receipe'),
    path('delete-receipe/<id>/', delete_receipe, name='delete_receipe'),
    path('update-receipe/<id>/', update_receipe, name='update_receipe'),

    path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)