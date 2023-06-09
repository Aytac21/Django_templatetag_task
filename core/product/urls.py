from django.urls import path
from . import views


app_name = "product"

urlpatterns = [
    path('list/', views.list_view, name="list"),
    path('otherlist/', views.list_2_view, name="otherlist")
]