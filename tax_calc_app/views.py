from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def tax_calc_func(request):
    
    content = {
        'message':'テンプレだよ！'
    }
    
    return render(request, 'tax_calc.html', content)
    
