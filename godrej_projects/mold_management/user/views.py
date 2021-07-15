from django.shortcuts import render

def user_login(request): 
    context = {}
    return render(request, 'users/login.html', context) # render login page. 



def user_signup(request): 
    context = {}

    return render(request, 'users/signup.html', context) # render signup page. 


def user_profile(request): 
    context = {}

    return render(request, 'users/userProfile.html', context) # user profile render. 

    