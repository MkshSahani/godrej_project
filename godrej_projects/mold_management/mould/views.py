from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from .models import Mould, MouldStatus 



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
    mould_data =  Mould.objects.get(mould_id = mould_id)
    context['data'] = mould_data 

    return render(request, 'mould_dataShow.html', context)


@login_required 
def mould_update(request): 
    context = {}
    context['MouldUpdate'] = False 
    if request.method == "POST": 
        context['MouldUpdate'] = True 
        mould_data = Mould.objects.all() 
        context['Mould_Data'] = mould_data 
        mould_id = request.POST.get('mouldID')
        increment = request.POST.get('increment')

        target_mould = Mould.objects.get(mould_id = mould_id)
        target_mould.present_count = target_mould.present_count + int(increment) 
        target_mould.save()


        mould_entry = MouldStatus()
        mould_entry.mould_id = target_mould 
        mould_entry.count_increment = increment 
        mould_entry.save()
        print(mould_id, increment)
        mould_entry_data = MouldStatus.objects.filter(mould_id = target_mould)
        context['target_mould_data'] = mould_entry_data 

        return render(request, 'mould_update.html', context)
    else: 
        mould_data = Mould.objects.all() 
        context['Mould_Data'] = mould_data 
        return render(request, 'mould_update.html', context)