from django.urls import path
from naru3app import views
urlpatterns=[
    path('intro/',views.intro),
    path('',views.intro2),

]