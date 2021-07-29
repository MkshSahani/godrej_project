from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from .models import Mould, MouldStatus, MouldComment, GeneralCleaningPresent
import matplotlib.pyplot as plt  
import matplotlib.dates as mdates 
import os
import datetime 

# ------------------------------------------------- 


MOULD_DELECTED = False 
MOULD_ID_DELETED = None 

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
        general_cleaning_threshold_value = request.POST.get('GeneralCleaningthresholdValue')
        preventive_maintaince_value = request.POST.get('PreventiveMaintainceValue')
        tool_life_count = request.POST.get('toolLifeCount')
        mould_desc = request.POST.get('mouldDesc')
        mould_order_number = request.POST.get('orderNumber')
        mould_raw_material = request.POST.get('rawMaterial')        
        part_weight = request.POST.get('partWeight')
        runner_weight = request.POST.get('runnerWeight')
        tonnage = request.POST.get('tonnage')
        cycle_time = request.POST.get('cycleTime')
        target_shots = request.POST.get('shotsPerDay')
        mould = Mould()
        mould.mould_id = mould_id 
        mould.mould_name = mould_name 
        mould.cavity_number = cavity_number 
        mould.registered_by = request.user 
        mould.general_maintaince_cleaning_threshold_value = general_cleaning_threshold_value  
        mould.present_count = 0 
        mould.preventive_maintaince_clearning_thresold_value = preventive_maintaince_value 
        mould.tool_life = tool_life_count 
        
        mould.moud_desc = mould_desc
        mould.order_number = mould_order_number
        mould.raw_material = mould_raw_material 
        mould.part_weight = part_weight 
        mould.runner_weight = runner_weight 
        mould.tonnage = tonnage 
        mould.cycle_time = cycle_time 
        mould.number_of_shots_per_day = target_shots
        
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
    if request.method == "POST": 
        comment_on_mould_id = request.POST.get('id')
        comment_text = request.POST.get('comment')
        comment_by = request.user 
        comment = MouldComment()
        comment.comment_text = comment_text 
        comment.commented_by = comment_by
        comment.mould_id = Mould.objects.get(mould_id = comment_on_mould_id)
        comment.save()
        return redirect(f'/mould/{comment_on_mould_id}')

    comments = MouldComment.objects.filter(mould_id = mould_id).order_by('commented_date_time')
    comments = list(comments)[::-1]
    print(comments)
    context['comments'] = comments 
    mould_data =  Mould.objects.get(mould_id = mould_id)
    context['data'] = mould_data 
    
    drawGraphMould_vs_shots(mould_data)
    return render(request, 'mould_id.html', context)


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


@login_required
def mould_search(request): 
    context = {}
    mould_id = Mould.objects.all()
    global MOULD_DELECTED, MOULD_ID_DELETED 
    if MOULD_DELECTED: 
        context['mould_deleted'] = True 
        context['mould_id_deleted'] = MOULD_ID_DELETED 
        MOULD_ID_DELETED = None 
        MOULD_DELECTED = False 
    mould_list_id = []
    for mould in mould_id: 
        mould_list_id.append(mould.mould_id)
    context['mould_id'] = mould_list_id
    if request.method == "POST": 
        mould_id = request.POST.get('mould_id')
        return redirect(f'/mould/{mould_id}')
    else: 
        return render(request, 'mould_search.html', context)


@login_required 
def mould_data_update(request, mould_id): 
    context = {}
    mould_data = Mould.objects.get(mould_id = mould_id)
    context['MouldData'] = mould_data 
    if request.method == "POST": 
        return render(request, 'mould_data_update.html', context)
    else: 
        return render(request, 'mould_data_update.html', context)



# ------------------------------------------------------------
# Graph Drawer. 

def drawGraphMould_vs_shots(mould_id): 
    mould_status_data = MouldStatus.objects.filter(mould_id = mould_id).order_by('status_update')
    
    increment_date = []
    increment_count = []

    for mould in mould_status_data: 
        increment_date.append(mould.status_update.date())
        increment_count.append(mould.count_increment)
    print(increment_count)
    print(increment_date)
    plt.title(f'Shot vs Date for Mould ID {mould_id}')
    plt.xlabel('Date')
    plt.ylabel('Shot Count')
    # plt.show()
    plt.plot(increment_date, increment_count,marker='>', color='blue')
    # beautify the x-labels
    plt.gcf().autofmt_xdate()
    myFmt = mdates.DateFormatter('%D:%M:%Y')
    plt.gca().xaxis.set_major_formatter(myFmt)
    plt.savefig('mould/static/images/mould_daily_count.png')
    plt.close()

# ------------------------------------------------------------ 


@login_required 
def mould_value_update(request, mould_id): 
    context = {}
    context['mould_id'] = mould_id
    mouldData = Mould.objects.get(mould_id = mould_id)
    print(mouldData)
    context['mouldData'] = mouldData 
    context['moldUpdated'] = False 

    if request.method == "POST": 
        mould_name = request.POST.get('mouldName')
        mould_cavity_number = request.POST.get('cavityNumber')
        mould_general_cleaning = request.POST.get('GeneralCleaningthresholdValue')
        mould_preventive_cleaning = request.POST.get('PreventiveMaintainceValue')
        mould_tool_life = request.POST.get('toolLifeCount')
        mouldData.mold_name = mould_name 
        mouldData.cavity_number = mould_cavity_number 
        mouldData.general_maintaince_cleaning_threshold_value = mould_general_cleaning 
        mouldData.preventive_maintaince_clearning_thresold_value = mould_preventive_cleaning 
        mouldData.tool_life = mould_tool_life 
        mouldData.save() # tool date updated. 
        context['mouldUpdated'] = True 
        return render(request, 'mould_value_update.html', context)
    return render(request, 'mould_value_update.html', context)

# ----------------------- Mould Delete ------------------------- 
@login_required 
def mould_delete(request, mould_id):
    mould_data = Mould.objects.get(mould_id = mould_id)
    mould_data.delete()
    global MOULD_DELECTED, MOULD_ID_DELETED
    MOULD_ID_DELETED = mould_id 
    MOULD_DELECTED = True 
    return redirect('/mould/mouldSearch/')



@login_required 
def general_cleaning(request, mould_id): 
    mould_data = Mould.objects.get(mould_id = mould_id)
    context = {}
    context['mould_data'] = mould_data 
    return render(request, 'mould_general_cleaning.html', context)


@login_required 
def general_cleaning_accept(request): 
    context = {}
    if request.method == "POST": 
        mould_id = request.POST.get('id')
        comment = request.POST.get('comment')
        try:
            general_cleaning = GeneralCleaningPresent.objects.get(mould_id = mould_id)
        except: 
            general_cleaning = None 
        if general_cleaning is not None: 
            context['ALREDY_IN_SERVICE'] = True
            return render(request, 'mould_gclean_accept.html',context) 
        else: 
            general_cleaning_accept_object = GeneralCleaningPresent()
            general_cleaning_accept_object.mould_id = Mould.objects.get(mould_id = mould_id)
            general_cleaning_accept_object.comment = comment 
            general_cleaning_accept_object.save()
        
            context['ACCEPTED'] = True 
            context['mould_data'] = general_cleaning_accept_object
            return render(request, 'mould_gclean_accept.html', context)
    else: 
        context['NO_DATA'] = True 
        return render(request, 'mould_gclean_accept.html', context)
