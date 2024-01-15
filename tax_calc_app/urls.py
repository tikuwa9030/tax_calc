from django.urls import path
from .views import tax_calc_func

urlpatterns = [
    path('', tax_calc_func, name='tax_calc'),
]
