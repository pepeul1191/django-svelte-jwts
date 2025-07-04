"""
URL configuration for tickesapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, re_path
from django.contrib.staticfiles.views import serve
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import apis

urlpatterns = [
  path('', views.home), 
  path('assets', views.home), 
  path('employees', views.home), 
  path('issues', views.home),
  path('issues/new', views.home), 
  path('sign-in', views.access), 
  path('sign-up', views.access), 
  path('reset-password', views.access),
  path('sign-out', views.signout),  
  path('api/v1/user/sign-in', apis.user_sign_in), 
  path('api/v1/user/session', apis.user_session),
]

handler404 = views.custom_404

if settings.DEBUG:
  # Esto ya estaba y sirve estáticos directamente desde STATICFILES_DIRS/app_static
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0] if settings.STATICFILES_DIRS else '')
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)