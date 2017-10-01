
from django.http import HttpResponse
from django.template import loader
from .models import List
from django.shortcuts import render,get_object_or_404

def index(request,list_id):
    listid=get_object_or_404(List,pk=list_id)
    context={
        'listid':listid,
    }
    return render(request,'info/index.html',context)

def details(request):
    comp_list = List.objects.all()
    context={
        'comp_list':comp_list,
    }
    return render(request,'info/details.html',context)

