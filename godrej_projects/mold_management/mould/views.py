from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from .models import Mould 



# ------------------------------------------------- 
class MouldData: 

    def __init__(self): 
        self.threshold = None 
        self.presentCount = None 
    
    def isThresholdCross(self): 
        diffrence = self.threshold - self.presentCount 
        alert_flag = True 
        if diffrence <= 500: 
            alert_flag = True 
        else: 
            alert_flag = False 
 
        return alert_flag     
    

@login_required 
def mould_registration(request): 
    context = {}
    context['mouldRegistered'] = False 
    if request.method == "POST": 
        mould_id = request.POST.get('mouldNumber')
        mould_name = request.POST.get('mouldName')
        cavity_number = request.POST.get('cavityNumber')
        threshold_number = request.POST.get('thresholdValue')
        mould = Mould()
        mould.mould_id = mould_id 
        mould.mould_name = mould_name 
        mould.cavity_number = cavity_number 
        mould.registered_by = request.user 
        mould.threshold_value = threshold_number 
        mould.present_count = 0 
        mould.save() # mould registered. 
        context['mouldRegistered'] = True 
        context['mouldName'] = mould_name
        print(mould_id, mould_name, cavity_number)
        return render(request, 'mould_registration.html', context)
    else: 
        context['mouldRegistered'] = False 
        return render(request, 'mould_registration.html', context)



@login_required 
def mould_view(request, mould_id): 
    context = {}
    mould = Mould.objects.get(mould_id = mould_id)
