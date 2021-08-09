from django.shortcuts import redirect, render
from mould.models import GeneralCleaningPresent, GeneralClearningArchieve, Mould, MouldDailyCheck, PreventiveMaintainceArchive
from mould.models import MouldDamageArchive

from .utils import DataCollector 
from .models import PPMData

def QualityPageRender(request): 
    context = {}

    # get list of moulds. 
    mould_data_list = Mould.objects.all()
    mould_commulative_cont_data = []
    
    for mould in mould_data_list: 
        mould_data_collector = DataCollector(mould.mould_id)
        print("-----")
        print(mould_data_collector.get_commulative_count())
        print("-----")
        mould_commulative_cont_data.append(MouldCommulativeCount(mould, 
        
            mould_data_collector.get_commulative_count(), 
            
            mould_data_collector.count_g_clean(), 
            
            mould_data_collector.count_p_main()))

    print(data.g_clean for data in mould_commulative_cont_data)

    context['mould_data'] = mould_commulative_cont_data    

    return render(request, 'quality/mould_quality.html', context)





# -------------------------------------------- 

def ppmDataView(request): 
    context = {}
    
    
    if request.method == "POST": 

        new_code = request.POST.get('newCode')
        vendor_name = request.POST.get('vendorName')
        total_number_of_lot = request.POST.get('totalLot')
        rejected_number_of_lot = request.POST.get('rejectedLot')

        ppm_obect = PPMData()
        ppm_obect.new_code = new_code 
        ppm_obect.vendor_name = vendor_name 
        ppm_obect.total_number_of_lot = total_number_of_lot
        ppm_obect.total_number_of_lot_rejected = rejected_number_of_lot 

        ppm_obect.save()    
    
    ppm_data = PPMData.objects.all()
    context['ppm_data'] = ppm_data 
    if len(ppm_data) == 0: 
        context['NO_DATA'] = True 
    else: 
        context['NO_DATA'] = False 

    for ppm in ppm_data: 
        print(ppm.ppm_data_added)

    return render(request, 'quality/ppmData.html', context)

# -------------------------------------------- 
def inspectionDataShow(request):

    context = {}
    mould_check_data = MouldDailyCheck.objects.all()
    if len(mould_check_data) > 10: 
        mould_check_data = mould_check_data[:10]
    
    context['mould_check_data'] = mould_check_data 
    return render(request, 'quality/mould_inspection_show.html', context) # render inspect data show page. 
    


# ---------------------------------------------

class MouldCommulativeCount: 

    def __init__(self, mould_data, commulative_count, g_clean, p_main):
        self.mould_data = mould_data 
        self.commulative_count = commulative_count 
        self.g_clean = g_clean 
        self.p_main = p_main 



# ------------------------------------------------ 
def mold_name_select(request): 
    context = {}

    if request.method == "POST": 
        mould_id = request.POST.get('mould_id')
        return redirect(f'/quality/historyCard/{mould_id}') 
    else: 
        mould_data_list = Mould.objects.all()
        mould_id = [mould.mould_id for mould in mould_data_list]

        context['mould_id'] =  mould_id 
        return render(request, 'quality/mould_select.html', context) 



# -------------------------------------------------- 

def mold_history_card(request, mould_id): 

    context = {}

    # mould data 
    context['mould_data'] = Mould.objects.get(mould_id = mould_id)
    context['GEN_CLEAN_DATA'] = GeneralClearningArchieve.objects.filter(mould_id = Mould.objects.get(mould_id = mould_id))
    context['P_MAIN_DATA'] = PreventiveMaintainceArchive.objects.filter(mould_id= Mould.objects.get(mould_id = mould_id))
    context['DAMAGE_DATA'] = MouldDamageArchive.objects.filter(mould_id = Mould.objects.get(mould_id = mould_id))
    
    if len(context['GEN_CLEAN_DATA']) != 0: 
        context['G_CLEAN'] = True 
    
    if len(context['P_MAIN_DATA']) != 0: 
        context['P_MAIN'] = True 
    
    if len(context['DAMAGE_DATA']) != 0: 
        context['DAMAGE'] = True 

    print(context['GEN_CLEAN_DATA'])

    return render(request, 'quality/mould_history_card.html', context) # return history card. 
