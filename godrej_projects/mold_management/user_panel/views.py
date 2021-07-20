from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from mould.models import Mould 

@login_required 
def homePage(request): 
    context = {}
    print(request.user)
    context['user'] = request.user 
    print("-----------------------")
    print(context['user'])
    mould_data = Mould.objects.all()
    context['mould_data'] = mould_data 
    print("----------------------")
    return render(request, 'user_panel/user_dashboard.html', context)
    

