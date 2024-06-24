from django.shortcuts import render
from .models import Author,Biography

def mergeddata1(request):
    data = Author.objects.select_related('biography').all()
    context = {'data': data}
    return render(request, 'app/merged_list.html', context)

def mergeddata2(request):
    data = Biography.objects.select_related().all()
    context = {'data': data}
    return render(request, 'app/new.html', context)
