from django.shortcuts import render,redirect
from django.http import HttpResponse
from Adminapp.models import Tbl_category
from Guestapp.models import Tbl_login,Tbl_studio
from Studioapp.models import Tbl_work,Tbl_workimage,Tbl_package
from Customerapp.models import Tbl_request,Tbl_payment
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studiohome(request):
    logid = request.session.get('loginid')
    if logid:
        return render(request,'Studio/studiohome.html')
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def workdetails(request):
    logid = request.session.get('loginid')
    if logid:
        category=Tbl_category.objects.all()
        return render(request,'Studio/workdetails.html',{'category':category})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def work_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            category_id = request.POST.get("categoryid") 
            wname = request.POST.get("workname")  
            wdes = request.POST.get("Description") 
            wimg = request.FILES["workimg"]   
            wob = Tbl_work()
            wob.workname = wname
            wob.description = wdes
            wob.workimg=wimg
            wob.category_id = Tbl_category.objects.get(categoryid=category_id)  
            wob.studioid = Tbl_studio.objects.get(loginid=request.session['loginid'])
            if Tbl_work.objects.filter(workname=wname, category_id=category_id).exists():
                return HttpResponse("<script>alert('Already Exists...');window.location='/studioapp/workdetails';</script>")
            else:
                wob.save()  
                return HttpResponse("<script>alert('Successfully inserted');window.location='/studioapp/workdetails';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def workimage(request):
    logid = request.session.get('loginid')
    if logid:
        studio=Tbl_studio.objects.get(loginid=request.session['loginid'])
        workname=Tbl_work.objects.filter(studioid=studio)
        return render(request,'Studio/workimage.html',{'work':workname})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def workimage_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            work_id= request.POST.get("workid") 
            img1 = request.FILES["image1"]
            img2 = request.FILES["image2"]
            img3 = request.FILES["image3"]
            img4 = request.FILES["image4"]
            img5 = request.FILES["image5"]
            img6 = request.FILES["image6"]
            iob = Tbl_workimage()
            iob.image1 = img1
            iob.image2 = img2
            iob.image3 = img3
            iob.image4 = img4
            iob.image5 = img5
            iob.image6 = img6
            iob.work_id = Tbl_work.objects.get(workid=work_id)  
            
            iob.save()  
            return HttpResponse("<script>alert('Successfully inserted');window.location='/studioapp/workimage';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def package(request):
    logid = request.session.get('loginid')
    if logid:
        category=Tbl_category.objects.all()
        return render(request,'Studio/package.html',{'category':category})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def package_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            category_id = request.POST.get("categoryid") 
            pname = request.POST.get("packagename")  
            pdes = request.POST.get("Description")  
            pamount = request.POST.get("amount")  
            pob = Tbl_package()
            pob.packagename = pname
            pob.description = pdes
            pob.amount = pamount
            pob.category_id = Tbl_category.objects.get(categoryid=category_id)  
            pob.studioid = Tbl_studio.objects.get(loginid=request.session['loginid'])
            if Tbl_package.objects.filter(packagename=pname).exists():
                return HttpResponse("<script>alert('Already Exists...');window.location='/studioapp/package';</script>")
            else:
                pob.save()  
                return HttpResponse("<script>alert('Successfully inserted');window.location='/studioapp/package';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

            
@cache_control(no_cache=True,must_revalidate=True,no_store=True)        
def requestview(request):
    logid = request.session.get('loginid')
    if logid:
        studio=Tbl_studio.objects.get(loginid=request.session['loginid'])
        package=Tbl_package.objects.filter(studioid=studio)
        r=Tbl_request.objects.filter(packageid__in=package,status="Booked")
        return render(request,"Studio/requestview.html",{'r':r})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def accept_request(request, requestid):
    logid = request.session.get('loginid')
    if logid:
        tbl_request = Tbl_request.objects.get(requestid=requestid)

        # Check if additional charge is provided
        additional_charge = request.POST.get('aamount')
        if additional_charge:
            tbl_request.aamount = additional_charge  # Set the additional charge

        tbl_request.status = 'Accepted'
        tbl_request.save()
        return redirect('requestview')  
    else:
        return HttpResponse("<script>alert('Authentication Required. Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def reject_request(request, requestid):
    logid = request.session.get('loginid')
    if logid:
        tbl_request = Tbl_request.objects.get(requestid=requestid)
        tbl_request.status = 'Rejected'
        remark = request.POST.get("remark")
        tbl_request.remark = remark
        tbl_request.save()
        return redirect('requestview')
    else:
        return HttpResponse("<script>alert('Authentication Required. Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewworkdetails(request):
    logid = request.session.get('loginid')
    if logid:
        studio=Tbl_studio.objects.get(loginid=request.session['loginid'])
        works = Tbl_work.objects.filter(studioid=studio)  # Fetch all records from Tbl_work
        return render(request, 'Studio/viewworkdetails.html', {'works': works})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def edit_work(request, workid):
    logid = request.session.get('loginid')
    if logid:
        work = Tbl_work.objects.get(pk=workid)
        
        if request.method == 'POST':
            work.workname = request.POST['workname']
            work.description = request.POST['description']
            work.save()
            return redirect('workdetails')
        
        return render(request, 'Studio/editwork.html', {'work': work})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


# Delete Work View
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def delete_work(request, workid):
    logid = request.session.get('loginid')
    if logid:
        work = Tbl_work.objects.get(pk=workid)
        work.delete()
        return redirect('workdetails')
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def work_image_view(request):
    logid = request.session.get('loginid')
    if logid:
        studio=Tbl_studio.objects.get(loginid=request.session['loginid'])
        works = Tbl_work.objects.filter(studioid=studio)   
        work_images =Tbl_workimage.objects.filter(work_id__in=works)
        return render(request, 'Studio/viewworkimage.html', {'work_images': work_images})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


# Edit Work Image View
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def edit_work_image(request, workimageid):
    logid = request.session.get('loginid')
    if logid:
        work_image = Tbl_workimage.objects.get(pk=workimageid)
        if request.method == 'POST':
            work_image.image1 = request.FILES.get('image1', work_image.image1)
            work_image.image2 = request.FILES.get('image2', work_image.image2)
            work_image.image3 = request.FILES.get('image3', work_image.image3)
            work_image.image4 = request.FILES.get('image4', work_image.image4)
            work_image.image5 = request.FILES.get('image5', work_image.image5)
            work_image.image6 = request.FILES.get('image6', work_image.image6)
            work_image.save()
            return redirect('workimage')
        return render(request, 'Studio/editworkimage.html', {'work_image': work_image})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


# Delete Work Image View
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def delete_work_image(request, workimageid):
    logid = request.session.get('loginid')
    if logid:
        work_image = Tbl_workimage.objects.get( pk=workimageid)
        work_image.delete()
        return redirect('workimage')
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def package_details_view(request):
    logid = request.session.get('loginid')
    if logid:
        studio_id = Tbl_studio.objects.get(loginid=request.session['loginid']) # Assuming studio is linked to the user
        packages = Tbl_package.objects.filter(studioid=studio_id)    
        return render(request, 'Studio/viewpackage.html', {'packages': packages})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def edit_package(request, packageid):
    logid = request.session.get('loginid')
    if logid:
        package = Tbl_package.objects.get(pk=packageid)
        
        if request.method == 'POST':
            package.packagename = request.POST['packagename']
            package.description = request.POST['description']
            package.amount = request.POST['amount']
            package.save()
            return redirect('package_details_view')
        
        return render(request, 'Studio/editpackage.html', {'package': package})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

# Delete Package
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def delete_package(request, packageid):
    logid = request.session.get('loginid')
    if logid:
        package =Tbl_package.objects.get(pk=packageid)
        package.delete()
        return redirect('package_details_view')
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewpayment(request):
    logid = request.session.get('loginid')
    if logid:
        studio=Tbl_studio.objects.get(loginid=request.session['loginid'])
        payments = Tbl_payment.objects.filter(requestid__packageid__studioid=studio).select_related('requestid__packageid')
        context = {'payments': payments}
        return render(request, 'Studio/viewpayment.html', context)
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def logout(request):
    logid = request.session.get('loginid')
    if logid:
        request.session.clear()
        return redirect('/')
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")





