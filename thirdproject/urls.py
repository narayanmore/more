"""thirdproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from naru3app import views as v1
from naru4app import views as v2
from django.conf.urls import include

urlpatterns = [
    path('contact/',include('contact.urls')),
    path('naru3app/',include('naru3app.urls')),
    path('naru4app/',include('naru4app.urls')),
#path('',v1.intro),
#path('info/',v2.info),
 path('admin/', admin.site.urls),
]
