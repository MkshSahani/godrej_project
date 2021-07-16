from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Employee 
from django.contrib.auth import login, logout, authenticate  
from django.contrib.auth import models 
from django.contrib.auth.decorators import login_required 

def user_login(request): 
    context = {}
    context['userCreditError'] = False 
    if request.method == "POST": 
        user_email = request.POST.get('userEmail')
        user_password = request.POST.get('userPassword')
        user_employee = authenticate(username=user_email, password=user_password)
        print(user_employee)
        if user_employee is not None: 
            login(request, user_employee)
            return redirect('')
        else: 
            context['userCreditError'] = True 
            return render(request, 'users/login.html', context)         
    else: 
        return render(request, 'users/login.html', context) # render login page. 



def user_signup(request): 
    context = {}
    context['userExist'] = False 
    context['UserRegistered'] = False 
    context['UserLogined']  = False 

   
    if request.method == "POST": 
        user_email = request.POST.get('userEmail')
        user_password = request.POST.get('userPassword')
        user_first_name = request.POST.get('userFirstName')
        user_last_name = request.POST.get('userLastName')
        user_address = request.POST.get('userAddress')
        user_phone_number = request.POST.get('userTelNumber')
        user_group = request.POST.get('userLevel')
        print(user_email, user_password, user_first_name, user_last_name, user_phone_number, user_address, user_group)
        try:
            new_employee = User.objects.create_user(username = user_email, 
                email=user_email, 
                first_name = user_first_name, 
                last_name = user_last_name, 
                password = user_password, 
                )
            new_employee.save()
            print("-----------------------------------------------")
            print(authenticate(username = user_email, password = user_password))
            print("-----------------------------------------------")
            new_employee_data = Employee.objects.create(employee_id = new_employee, 
              employee_level = user_group, 
              employee_address=user_address, 
              employee_phone=user_phone_number)
            
            # * user has been registered now get him online.
            context['UserRegistered'] = True  
            login(request, new_employee)
            context['UserLogined'] = True 
            context['userExist'] = False 
            return redirect('/')

        except:
            # if same user for same username or email address exits then throw error. 
            context['userExist'] = True 
            return render(request, 'users/signup.html', context)

    else: 
        print("------------------")
        return render(request, 'users/signup.html', context) # render signup page. 


@login_required 
def user_profile(request): 
    context = {}

    return render(request, 'users/userProfile.html', context) # user profile render. 


def user_logout(request): 
    context = {}
    logout(request) 
    return redirect('/user/login')