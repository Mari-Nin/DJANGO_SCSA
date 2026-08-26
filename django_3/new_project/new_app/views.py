from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Item

def hello_view(request):
    return render(request,'hello.html')

def about_view(request):
    return render(request,'about.html')

def item_detail_view(request,item_id):
    try:
        item=Item.objects.get(id=item_id)
        context={'item':item}
        return render(request,'item.html',context)
    except Item.DoesNotExist:
        return HttpResponse(f"Item M {item_id} does not exist")

