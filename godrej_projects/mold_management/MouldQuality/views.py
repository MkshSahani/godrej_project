from django.shortcuts import render
from mould.models import Mould 
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
class MouldCommulativeCount: 

    def __init__(self, mould_data, commulative_count, g_clean, p_main):
        self.mould_data = mould_data 
        self.commulative_count = commulative_count 
        self.g_clean = g_clean 
        self.p_main = p_main 

        