"""mtemp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from mon import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('monitor/', views.monitor, name='monitor'),
    path('monitor_graph/', views.monitor_graph, name='monitor_graph'),
    path('sensors/', views.sensors, name='sensors'),
    path('home/', views.home, name='home'),
    path('add/',views.add, name='add'),
    path('threshold_add/',views.Threshold_add, name='threshold_add'),
    path('device_add/',views.device_add, name='device_add'),
    path('threshold_view/',views.threshold_view, name='threshold_view'),
    path('delete/<id>', views.delete, name='delete'),
    path('tempedit/<edit_id>', views.tempedit, name='tempedit'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
