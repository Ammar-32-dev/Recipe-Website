from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def receipe(request):

    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_ingredients=data.get('receipe_ingredients')

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_ingredients=receipe_ingredients,
        )

     
        return redirect('receipe')
    
    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        # print(request.GET.get('search'))
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipe':queryset}

    return render(request, 'receipe.html',context)


def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_ingredients=data.get('receipe_ingredients')

        queryset.receipe_name = receipe_name
        queryset.receipe_ingredients = receipe_ingredients

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('receipe')

    context = {'receipe':queryset}

    return render(request, 'update_receipe.html',context)


def delete_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()

    return redirect('receipe')