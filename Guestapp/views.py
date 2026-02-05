import random
import string
from django.shortcuts import render,redirect
from Guestapp.models import Tbl_login
from Guestapp.models import Tbl_studio,Tbl_customer
from Adminapp.models import tbl_district,tbl_location
from django.http import JsonResponse,HttpResponse

from email.message import EmailMessage
import smtplib

# Create your views here.
def login(request):
    return render(request,'Guest/login.html')

def login_process(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if Tbl_login.objects.filter(username=username,password=password).exists():
            logindata = Tbl_login.objects.get(username=username,password=password)
            request.session['loginid']=logindata.loginid
            role = logindata.role
            if role == "admin":
                return redirect('/studio/index')
            elif role =='studio':
                if logindata.status =='Accepted':
                    return redirect('/studioapp/studiohome')
                else:
                    return HttpResponse("<script>alert('Request not accepted');window.location='/login/';</script>")
            elif role =='customer':
                if logindata.status =='confirmed':
                    return redirect('/customerapp/customerhome')
                else:
                    return HttpResponse("<script>alert('Request not accepted');window.location='/login/';</script>")
            else:
                return HttpResponse("<script>alert('Not an authorized person');window.location='/login/';</script>")
        else:
            return HttpResponse("<script>alert('Invalid username or password');window.location='/login/';</script>")
                   
                
            

def guesthome(request):
        return render(request,'Guest/guesthome.html')
   
def studioreg(request):
    district=tbl_district.objects.all()
    return render(request,'Guest/studioreg.html',{'district':district})

def studioreg_process(request):
    if request.method =="POST":
        lob = Tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "studio"
        lob.status='Not confirmed'
        if Tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Alredy Exists...');window.location='/guestapp/studioreg';</script>")
        else:
            lob.save()
            sob = Tbl_studio()
            sob.studioname = request.POST.get("name")
            sob.address = request.POST.get("address")
            sob.email = request.POST.get("email")
            sob.phone = request.POST.get("phonenumber")
            sob.landmark = request.POST.get("landmark")
            sob.idproof = request.FILES["idproof"]
            sob.simage = request.FILES["simage"]
            sob.pincode = request.POST.get("pincode")
            sob.locationid = tbl_location.objects.get(locationid=request.POST.get("location"))
            sob.loginid = lob
            sob.save()
            return HttpResponse("<script>alert('Successfully registered');window.location='/studioreg/';</script>")

def filllocations(request):
    did=int(request.POST.get("did"))
    location =tbl_location.objects.filter(districtid=did).values()
    return JsonResponse(list(location),safe=False)
        
def customerreg(request):
    district=tbl_district.objects.all()
    return render(request,'Guest/customerreg.html',{'district':district})

def customerreg_process(request):
    if request.method =="POST":
        lob = Tbl_login()
        lob.username = request.POST.get("username")
        lob.password = request.POST.get("password")
        lob.role = "customer"
        lob.status='confirmed'
        if Tbl_login.objects.filter(username=request.POST.get("username")).exists():
            return HttpResponse("<script>alert('Alredy Exists...');window.location='/guestapp/customerreg';</script>")
        else:
            lob.save()
            cob = Tbl_customer()
            cob.customername = request.POST.get("name")
            cob.address = request.POST.get("address")
            cob.email = request.POST.get("email")
            cob.phone = request.POST.get("phonenumber")
            cob.pincode = request.POST.get("pincode")
            cob.locationid = tbl_location.objects.get(locationid=request.POST.get("location"))
            cob.loginid = lob
            cob.save()
            
            Email=request.POST.get('email')  # to address
            msg = EmailMessage()
            msg.set_content('Thank you for registering!!')
            msg['Subject'] = "Registration Completed"
            msg['from'] = 'mailforadithyan@gmail.com'
            msg['To'] = {Email}
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('mailforadithyan@gmail.com','your_app_password')
                smtp.send_message(msg)
            return HttpResponse("<script>alert('Successfully registered');window.location='/customerreg/';</script>")
        
def forgotpassword(request):
    if request.method == 'POST':
        uname = request.POST.get("name")

        # Check if the user is a customer
        if Tbl_customer.objects.filter(loginid__username=uname).exists():
            cust = Tbl_customer.objects.get(loginid__username=uname)
            email = cust.email
            customer_name = cust.customername
            user_type = 'user'
            login_instance = cust.loginid  # Get the login details of the customer

        # Check if the user is a studio (instead of turf)
        elif Tbl_studio.objects.filter(loginid__username=uname).exists():
            studio = Tbl_studio.objects.get(loginid__username=uname)
            email = studio.email
            studio_name = studio.studioname  # Get the studio name from the studio record
            user_type = 'studio'
            login_instance = studio.loginid  # Get the login details of the studio

        else:
            return HttpResponse(
                "<script>alert('No user found with this username.');window.location='/forgotpassword';</script>")

        # Generate a random password
        characters = string.ascii_letters + string.digits
        random_number = ''.join(random.choice(characters) for _ in range(8))

        # Update password for the user (either customer or studio)
        try:
            login_instance.password = random_number
            login_instance.save()

            # Email configuration
            msg = EmailMessage()
            if user_type == 'user':
                msg.set_content(f'Hi {customer_name}, Your new password to login is {random_number}')
            elif user_type == 'studio':
                msg.set_content(f'Hi {studio_name}, Your new password to login is {random_number}')
            
            msg['Subject'] = "Forgot Password"
            msg['From'] = 'jaidengillj@gmail.com'
            msg['To'] = email
            
            # SMTP connection and sending email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('mailforadithyan@gmail.com', 'your_app_password')  # Use app password instead of regular Gmail password
                smtp.send_message(msg)

            return HttpResponse(
                "<script>alert('Login with the new password sent to your email.');window.location='/login';</script>")
        
        except Tbl_login.DoesNotExist:
            return HttpResponse(
                "<script>alert('Error: No login instance found for this username.');window.location='/forgotpassword';</script>")

    return render(request, "Guest/forgotpassword.html")