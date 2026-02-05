from django.shortcuts import render,redirect
from Guestapp.models import Tbl_studio,Tbl_customer
from Adminapp.models import tbl_district,tbl_location,Tbl_category
from Studioapp.models import Tbl_work,Tbl_workimage,Tbl_package
from Customerapp.models import Tbl_feedback, Tbl_request,Tbl_payment
from django.http import JsonResponse,HttpResponse
from django.views.decorators.cache import cache_control

from email.message import EmailMessage
import smtplib
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def customerhome(request):
    logid = request.session.get('loginid')
    if logid:
        return render(request,'Customer/customerhome.html')
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studioview(request):
    logid = request.session.get('loginid')
    if logid:
        district=tbl_district.objects.all()
        return render(request,'Customer/studioview.html',{'district':district})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def filllocations(request) :
    logid = request.session.get('loginid')
    if logid:
        did=int(request.POST.get ("did"))
        location = tbl_location.objects.filter(districtid=did) .values()
        return JsonResponse(list(location), safe=False)
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def fillstudios(request):
    logid = request.session.get('loginid')
    if logid:
        location_id = request.POST.get('lid')
        
        if location_id:
            studios = Tbl_studio.objects.filter(locationid=location_id)
            studios_data = []
            for studio in studios:
                studio_data = {
                    'studioid': studio.studioid,
                    'studioname': studio.studioname,
                    'simage': studio.simage.url if studio.simage else None  # Handle the image if exists
                }
                studios_data.append(studio_data)
            return JsonResponse(studios_data, safe=False)
        else:
            return JsonResponse([], safe=False)
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def categoryview(request, studioid):
    logid = request.session.get('loginid')
    if logid:
        category = Tbl_category.objects.all()  # Get all categories
        studio = Tbl_studio.objects.get(studioid=studioid)  # Get the selected studio
        return render(request, 'Customer/categoryview.html', {'category': category, 'studio': studio})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def work(request, studioid, categoryid):
    logid = request.session.get('loginid')
    if logid:
        studio = Tbl_studio.objects.get(studioid=studioid)    
        category = Tbl_category.objects.get(categoryid=categoryid)    
        work = Tbl_work.objects.filter(studioid=studioid,category_id=categoryid)
        #return HttpResponse(work)
        return render(request, 'Customer/work.html', {'work': work, 'studio': studio, 'category': category})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
def package(request, studioid,categoryid):
    logid = request.session.get('loginid')
    if logid:
        studio = Tbl_studio.objects.get(studioid=studioid)
        category = Tbl_category.objects.get(categoryid=categoryid)
        package = Tbl_package.objects.filter(studioid=studioid,category_id=categoryid)
        return render(request, 'Customer/package.html', {'category': category, 'studio': studio,'package':package})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def workimage(request,studioid,categoryid,workid):
    logid = request.session.get('loginid')
    if logid:
        studio = Tbl_studio.objects.get(studioid=studioid)
        category = Tbl_category.objects.get(categoryid=categoryid)    
        work = Tbl_work.objects.get(workid=workid)
        workimage = Tbl_workimage.objects.filter(work_id=work)
        return render(request, 'Customer/workimage.html', {'studio':studio,'category':category, 'work':work,'workimage':workimage})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def packagesingleview(request,studioid,packageid):
    logid = request.session.get('loginid')
    if logid:
        package = Tbl_package.objects.get(packageid=packageid)
        studio = Tbl_studio.objects.get(studioid=studioid)
        return render(request,'Customer/packagesingleview.html',{'package':package,'studio':studio})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def bookingprocess(request,packageid):
    logid = request.session.get('loginid')
    if logid:
        package=Tbl_package.objects.get(packageid=packageid)
        if request.method == "POST":
            r=Tbl_request()
            r.packageid=package
            r.requireddate=request.POST.get("reqdate")
            r.noofdays=request.POST.get("noofdays")
            r.description=request.POST.get("description")
            r.status="Booked"
            r.customerid=Tbl_customer.objects.get(loginid=request.session['loginid'])
            r.save()
            return HttpResponse("<script>alert('Booking request send...');window.location='/customerapp/confirmation';</script>")
        return render(request,"Customer/packagesingleview.html",{'package':package})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def confirmation(request):
    logid = request.session.get('loginid')
    if logid:
        customer = Tbl_customer.objects.get(loginid=request.session['loginid'])
        r = Tbl_request.objects.filter(customerid=customer)

        for req in r:
            # Get package amount
            package_amount = req.packageid.amount
            
            # Calculate total amount (package amount + additional amount)
            req.total_amount = package_amount + (req.aamount if req.aamount else 0)

            # Corrected calculation of initial payment (total amount + additional amount) / 2
            req.initial_payment = (package_amount + (req.aamount if req.aamount else 0)) / 2

            # Fetch studio name, location, and contact via the package
            studio = req.packageid.studioid
            req.studio_name = studio.studioname
            req.studio_location = studio.locationid.locationname  # Assuming 'location' is a field in Tbl_studio
            req.studio_contact = studio.phone  # Assuming 'contact' is a field in Tbl_studio

        return render(request, "Customer/confirmation.html", {'r': r})
    else:
        return HttpResponse("<script>alert('Authentication Required. Please Login first');window.location='/login';</script>")

    
from decimal import Decimal

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def payment(request, requestid):
    logid = request.session.get('loginid')
    if logid:
        # Retrieve the request based on the requestid
        r = Tbl_request.objects.get(requestid=requestid)
        
        # Get the package amount and additional amount
        tamount = r.packageid.amount + (r.aamount if r.aamount else 0)  # Total amount = package amount + additional amount
        aamount = r.aamount  # Additional amount
        iamount = tamount / Decimal(2)  # Initial amount to be paid by the customer
        camount = iamount * Decimal(0.1)  # 10% of initial amount is the camount
        
        if request.method == "POST":
            # Save the payment record
            p = Tbl_payment()
            p.iamount = iamount
            p.tamount = tamount
            p.camount = camount
            p.status = "Paid"
            p.requestid = r
            p.save()
            
            # Update the request's total amount field and status
            r.total_amount = tamount  # Save the calculated total amount
            r.status = "Paid"  # Update status to Paid
            r.save()

            # Send email notification
            Email = r.customerid.email
            msg = EmailMessage()
            msg.set_content('Payment Successful')
            msg['Subject'] = "Registration Completed"
            msg['from'] = 'mailforadithyan@gmail.com'
            msg['To'] = {Email}
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('mailforadithyan@gmail.com', 'your_app_password')
                smtp.send_message(msg)
            
            return HttpResponse("<script>alert('Payment Successful!');window.location='/customerapp/confirmation';</script>")
        
        # Render the payment page and pass iamount to the template
        return render(request, 'Customer/payment.html', {'request': r, 'iamount': iamount})
    
    else:
        return HttpResponse("<script>alert('Authentication Required! Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def cpaymentview(request):
    logid = request.session.get('loginid')
    if logid:
        customer=Tbl_customer.objects.get(loginid=request.session['loginid'])
        requests=Tbl_request.objects.filter(customerid=customer)
        payments = Tbl_payment.objects.filter(requestid__in=requests)  # Fetch all payment details
        return render(request, 'Customer/cpaymentview.html', {'payments': payments})
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

def feedback(request, requestid):
    request_instance = Tbl_request.objects.get(requestid=requestid)

    if request.method == "POST":
        description = request.POST.get('description')
        rating = request.POST.get('rating')

        Tbl_feedback.objects.create(
            description=description,
            rating=rating,
            customerid=request_instance.customerid,
            packageid=request_instance.packageid
        )
        return redirect('confirmation')

    return render(request, 'Customer/feedback.html', {'requestid': requestid})

def fetchreviews(request):
    """ Fetches reviews for the selected studio via AJAX. """
    if request.method == "POST":
        studio_id = request.POST.get('studioid')
        feedbacks = Tbl_feedback.objects.filter(packageid__studioid=studio_id).select_related('customerid')

        review_data = [
            {
                "customername": feedback.customerid.customername,
                "description": feedback.description,
                "rating": feedback.rating
            }
            for feedback in feedbacks
        ]

        return JsonResponse(review_data, safe=False)


