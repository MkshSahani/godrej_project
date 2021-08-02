from django.shortcuts import render

def QualityPageRender(request): 
    context = {}
    return render(request, 'quality/mould_quality.html', context)