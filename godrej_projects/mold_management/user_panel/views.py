from django.shortcuts import render
from django.contrib.auth.decorators import login_required 


@login_required 
def homePage(request): 
    context = {}
    print(request.user)
    context['user'] = request.user 
    print("-----------------------")
    print(context['user'])
    print("----------------------")
    return render(request, 'user_panel/user_dashboard.html', context)
    

