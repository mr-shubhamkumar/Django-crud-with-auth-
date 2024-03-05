from django.shortcuts import render, redirect
from django.views import View
from .models import Category,SubCategory,Product
from django.http import JsonResponse ,HttpResponse
from django.core import serializers
import os
from crud.settings import BASE_DIR
from django.contrib.auth import authenticate, login, logout

from .froms import UserRegistrationFrom,LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(View):
    def get(self, request):
        data = Product.objects.all()
        return render(request, 'app/home.html',{'data':data})


class Registreton(View):
    def get(self, request):
        form = UserRegistrationFrom()
        return render(request, "app/Registreton.html",{'form':form})

    def post(self,request):
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registretion Successfuly")
            # return redirect('home')
        return render(request, "app/Registreton.html",{'form':form})    
   

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


# def category(request):
#     return render(request, 'app/category.html')
@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request):
        return render(request, 'app/category.html')

    def post(self, request):
        if request.method == 'POST':

         data = request.POST
         cat_name = data.get('cat_name')
         Category.objects.create(
            cat_name=cat_name
         )
         
         return redirect('home')

@login_required
def subcategory(request):

    if request.method == "POST":
        data = request.POST
        # cat_id = int(data.get('cat_id'))
        cat_id = data.get('cat_id')
        category_instance = Category.objects.get(id=cat_id)
        subcat_name = data.get('subcat_name')

        SubCategory.objects.create(
            cat=category_instance,
            subcat_name=subcat_name,
        )
        return redirect('home')

    cat = Category.objects.all()
    subcats = SubCategory.objects.all()
    contex = {'cat':cat,'subcats':subcats}
    return render(request, 'app/subcategory.html',contex)


def fatchsubcatgeory(request, id):
        subcat = SubCategory.objects.filter(cat=id)

        filtered_data_list = [{'id': item.id, 'subcat_name': item.subcat_name} for item in subcat]

        # Return the filtered data as JSON
        return JsonResponse({'data': filtered_data_list})
    
# Create Data 
@login_required
def create(request):
    if request.method == 'POST':
        data = request.POST

        cat_id =data.get('cat_id')
        subcat_id =data.get('subcat_id')
        cat = Category.objects.get(id=cat_id)
        subcat = SubCategory.objects.get(id=subcat_id)

        title =data.get('title')
        discription =data.get('discription')
        image = request.FILES.get('image')


        Product.objects.create(
            cat=cat,
            subcat=subcat,
            title=title,
            discription=discription,
            image=image,

        )
        return redirect('home')

    cats = Category.objects.all()
    contex = {'cats':cats}
    return render(request, 'app/create.html',contex)

@login_required
def edit(request, id):
    #data Upate code
    queryset = Product.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        
        cat_id =data.get('cat_id')
        subcat_id =data.get('subcat_id')
        title =data.get('title')
        discription =data.get('discription')
        image = request.FILES.get('image')


        # get cat and subcat id by instenc
        cat = Category.objects.get(id=cat_id)
        subcat = SubCategory.objects.get(id=subcat_id)

        queryset.cat =cat
        queryset.subcat =subcat
        queryset.title =title
        queryset.discription =discription

   
        # if file in selected
        if image:
           old_image_path = queryset.image.path

           if os.path.exists(old_image_path):
               os.remove(old_image_path)
        queryset.image = image

        queryset.save()   
        return redirect('home')
    #data Upate code end

    data = Product.objects.get(id=id)
    cats = Category.objects.all()
    subcats = SubCategory.objects.all()
    return render(request, 'app/edit.html',{'data':data,'cats':cats ,'subcats':subcats})

@login_required
def delete(request, id):
    data = Product.objects.get(id=id)
    old_image_path = data.image.path
    if os.path.exists(old_image_path):
            os.remove(old_image_path)
    data.delete()
    

    return redirect('home')







