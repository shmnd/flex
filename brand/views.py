from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from .models import Brand
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Create your views here.
@cache_control(no_chace=True,must_revalidate=True,no_store=True)
def brand(request):
    if not request.user.is_superuser:
        return redirect('adminsignin')
    brand_data=Brand.objects.all().order_by(id)
    return render(request,'admin/adminbrand.html',{'brand':brand_data})



def createbrand(request):
    if not request.user.is_superuser:
        return redirect('adminsignin')
    
    if request.method=='POST':
        bname=request.POST.get('name')


        # validation
        if bname.strip()=='':
            messages.error(request,'name cannot be blank')
            return redirect('brand')
        
        if Brand.objects.filter(name=bname).exists():
            messages.error(request,'Name already exists')
            return redirect('brand')
        

    brandsave=Brand(name=bname)
    brandsave.save()
    return redirect('brand')


# edit category

def editbrand(request,editbrand_id):
    if not request.user.is_superuser:
        return redirect('adminsignin')
    

    if request.method=='POST':

        bname=request.POST.get('name')

    # validation

    try:
        brandsave=Brand.objects.get(id=editbrand_id)
    except Brand.DoesNotExist:
        messages.error(request,'brand is already exists')
    

    if bname.strip()=='':
        messages.error(request,'Brand name cannodt be empty')
        return redirect('brand')
    
    brands=Brand.objects.get(id=editbrand_id)
    brands.name=bname
    brands.save()
    return redirect('brand')


# delete brand

def deletebrand(request,deletebrand_id):
    if not request.user.is_superuser:
        return redirect('adminsignin')
    
    brands=Brand.objects.get(id=deletebrand_id)
    brands.save()
    return redirect('brand')


# search brand
def searchbrand(request):
    if not request.user.is_superuser:
        return redirect('adminsignin')
    
    if 'keyword' in request.GET:
        keyword=request.GET.get('keyword')
        if keyword:
            bran=Brand.objects.filter(brand)


    
    
    
    
    
    
