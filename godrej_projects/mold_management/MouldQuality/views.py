from django.shortcuts import render
from mould.models import Mould 
from .utils import DataCollector 

def QualityPageRender(request): 
    context = {}

    # get list of moulds. 
    mould_data_list = Mould.objects.all()
    mould_commulative_cont_data = []
    
    for mould in mould_data_list: 
        mould_data_collector = DataCollector(mould.mould_id)
        mould_commulative_cont_data.append(MouldCommulativeCount(mould, 
        
            mould_data_collector.get_commulative_count(), 
            
            mould_data_collector.count_g_clean(), 
            
            mould_data_collector.count_p_main()))

    print(data.g_clean for data in mould_commulative_cont_data)

    context['mould_data'] = mould_commulative_cont_data    

    return render(request, 'quality/mould_quality.html', context)


# -------------------------------------------- 
class MouldCommulativeCount: 

    def __init__(self, mould_data, commulative_count, g_clean, p_main):
        self.mould_data = mould_data 
        self.commulative_count = commulative_count 
        self.g_clean = g_clean 
        self.p_main = p_main 

        