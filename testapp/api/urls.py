from django.urls import path
from . import views

urlpatterns = [
    path('', views.Listvue.as_view(), name="testapp")
]
