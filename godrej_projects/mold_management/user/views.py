from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Employee 

def user_login(request): 
    context = {}

    if request.method == "POST": 
        pass 
    else: 
        return render(request, 'users/login.html', context) # render login page. 



def user_signup(request): 
    context = {}
    if request.method == "POST": 
        user_email = request.POST.get('userEmail')
        user_password = request.POST.get('userPassword')
        user_first_name = request.POST.get('userFirstName')
        user_last_name = request.POST.get('userLastName')
        user_address = request.POST.get('userAddress')
        user_phone_number = request.POST.get('userTelNumber')
        user_group = request.POST.get('userLevel')
        print(user_email, user_password, user_first_name, user_last_name, user_phone_number, user_address, user_group)
    
        new_employee = User.objects.create_user(username = user_email, 
            email=user_email, 
            first_name = user_first_name, 
            last_name = user_last_name, 
            password = user_password, 
            )

        new_employee_data = Employee.objects.create(employee_id = new_employee, 
          employee_level = user_group, 
          employee_address=user_address, 
          employee_phone=user_phone_number)
        
        
        return render(request, 'users/signup.html', context) # render singup page. 
    else: 
        return render(request, 'users/signup.html', context) # render signup page. 


def user_profile(request): 
    context = {}

    return render(request, 'users/userProfile.html', context) # user profile render. 

    