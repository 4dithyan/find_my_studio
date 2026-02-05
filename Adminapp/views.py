from django.shortcuts import redirect,render
from Adminapp.models import tbl_district,tbl_location,Tbl_category
from django.http import HttpResponse,JsonResponse
from Guestapp.models import Tbl_studio,Tbl_login
from Customerapp.models import Tbl_payment
from django.views.decorators.cache import cache_control
from email.message import EmailMessage
import smtplib
import xlwt
from django.views.generic import View
from django.db.models import Sum

from datetime import datetime

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def index(request):
    logid = request.session.get('loginid')

    # 🔹 Payments per Studio (Pie Chart)
    studio_labels = []
    studio_data = []
    studio_query = Tbl_payment.objects.values('requestid__packageid__studioid__studioname').annotate(total_payments=Count('paymentid'))

    for payment in studio_query:
        studio_labels.append(payment['requestid__packageid__studioid__studioname'])
        studio_data.append(payment['total_payments'])

    # 🔹 Payments per Category (Bar Graph)
    category_labels = []
    category_data = []
    category_query = Tbl_payment.objects.values('requestid__packageid__category_id__categoryname').annotate(total_payments=Count('paymentid'))

    for category in category_query:
        category_labels.append(category['requestid__packageid__category_id__categoryname'])
        category_data.append(category['total_payments'])

    # 🔹 Payments per Package (Pie Chart)
    package_labels = []
    package_data = []
    package_query = Tbl_payment.objects.values('requestid__packageid__packagename').annotate(total_payments=Count('paymentid'))

    for package in package_query:
        package_labels.append(package['requestid__packageid__packagename'])
        package_data.append(package['total_payments'])

    # 🔹 Total Amount Gained by Studios (Bar Graph) ✅ FIXED ✅
    studio_amount_labels = []
    studio_amount_data = []
    amount_query = Tbl_payment.objects.values('requestid__packageid__studioid__studioname').annotate(total_amount=Sum('tamount'))

    for studio in amount_query:
        studio_amount_labels.append(studio['requestid__packageid__studioid__studioname'])
        studio_amount_data.append(float(studio['total_amount']))  # Convert to float to ensure JS compatibility

    if logid:
        return render(request, 'Admin/index.html', {
            'studio_labels': studio_labels,
            'studio_data': studio_data,
            'category_labels': category_labels,
            'category_data': category_data,
            'package_labels': package_labels,
            'package_data': package_data,
            'studio_amount_labels': studio_amount_labels,
            'studio_amount_data': studio_amount_data,  # ✅ Now correctly formatted ✅
        })
    else:
        return HttpResponse("<script>alert('Authentication Required. Please log in first'); window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def district(request):
    logid = request.session.get('loginid')
    if logid:
        return render(request,'Admin/district.html')
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def district_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            dname=request.POST.get("districtname") #textboxname
            dob = tbl_district()
            dob.districtname = dname   #cob.categoryname = fieldname in table
            if tbl_district.objects.filter(districtname=dname).exists():
                return HttpResponse("<script>alert('Aldready Exists...');window.location='/studio/district';</script>")
            else:
                dob.save()
                return HttpResponse("<script>alert('Succesfully inserted');window.location='/studio/district/';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def location(request):
    logid = request.session.get('loginid')
    if logid:
        district=tbl_district.objects.all()
        return render(request,'Admin/location.html',{'district':district})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def location_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            districtid=request.POST.get("districtid") 
            lname=request.POST.get("locationname") 
            lob = tbl_location()
            lob.locationname = lname  
            lob.districtid = tbl_district.objects.get(districtid=districtid)
            if tbl_location.objects.filter(locationname=lname,districtid=districtid).exists():
                return HttpResponse("<script>alert('Aldready Exists...');window.location='/studio/location';</script>")
            else:
                lob.save()
                return HttpResponse("<script>alert('Succesfully inserted');window.location='/studio/location';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def category(request):
    logid = request.session.get('loginid')
    if logid:
        return render(request,'Admin/category.html')
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def category_process(request):
    logid = request.session.get('loginid')
    if logid:
        if request.method == "POST":
            cname=request.POST.get("categoryname") #textboxname
            cimage=request.FILES["categoryimage"] #filename
            cob = Tbl_category()
            cob.categoryname = cname   #cob.categoryname = fieldname in table
            cob.categoryimage = cimage
            if Tbl_category.objects.filter(categoryname=cname).exists():
                return HttpResponse("<script>alert('Aldready Exists...');window.location='/studio/category';</script>")
            else:
                cob.save()
                return HttpResponse("<script>alert('Succesfully inserted');window.location='/studio/category';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewdistrict(request):
    logid = request.session.get('loginid')
    if logid:
        district=tbl_district.objects.all()
        return render(request,'Admin/viewdistrict.html',{'district':district})
    else:
            return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletedistrict(request,districtid):
    logid = request.session.get('loginid')
    if logid:
        dob=tbl_district.objects.get(districtid=districtid)
        dob.delete()
        return  HttpResponse("<script>alert('successfully deleted..');window.location='/studio/viewdistrict';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcategory(request):
    logid = request.session.get('loginid')
    if logid:
        category=Tbl_category.objects.all()
        return render(request,'Admin/viewcategory.html',{'category':category})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletecategory(request,categoryid):
    logid = request.session.get('loginid')
    if logid:
        cob=Tbl_category.objects.get(categoryid=categoryid)
        cob.delete()
        return  HttpResponse("<script>alert('successfully deleted..');window.location='/studio/viewcategory';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewlocation(request):
    logid = request.session.get('loginid')
    if logid:
        district=tbl_district.objects.all()
        return render(request,'Admin/viewlocation.html',{'districts':district})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def deletelocation(request,locationid):
    logid = request.session.get('loginid')
    if logid:
        lob=tbl_location.objects.get(locationid=locationid)
        lob.delete()
        return  HttpResponse("<script>alert('successfully deleted..');window.location='/studio/viewlocation';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def filllocation (request) :
    logid = request.session.get('loginid')
    if logid:
        did=int(request.POST.get ("did"))
        location = tbl_location.objects.filter(districtid=did) .values()
        return JsonResponse(list(location), safe=False)
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studioverification(request):
    logid = request.session.get('loginid')
    if logid:
        studio=Tbl_studio.objects.filter(loginid__status="Not confirmed")
        return render(request,'Admin/studioverification.html',{'studio':studio})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studioaccept(request, loginid):
    logid = request.session.get('loginid')
    if logid:
        lob = Tbl_studio.objects.get(loginid=loginid)  
        login_instance = lob.loginid                   
        login_instance.status = "Accepted"            
        login_instance.save()                          
        lob.save()  
        
        Email=lob.email # to address
        msg = EmailMessage()
        msg.set_content('Accepted')
        msg['Subject'] = "Registration Completed"
        msg['from'] = 'mailforadithyan@gmail.com'
        msg['To'] = {Email}
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('mailforadithyan@gmail.com','your_app_password')
            smtp.send_message(msg)
        return  HttpResponse("<script>alert('Accepted...');window.location='/studio/studioverification';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studioreject(request,loginid):
    logid = request.session.get('loginid')
    if logid:
        lob = Tbl_studio.objects.get(loginid=loginid)  
        login_instance = lob.loginid                   
        login_instance.status = "Rejected"            
        login_instance.save()                         
        lob.save()  
        Email=lob.email  # to address
        msg = EmailMessage()
        msg.set_content('Rejected')
        msg['Subject'] = "Registration Completed"
        msg['from'] = 'mailforadithyan@gmail.com'
        msg['To'] = {Email}
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('mailforadithyan@gmail.com','your_app_password')
            smtp.send_message(msg)
        return  HttpResponse("<script>alert('Rejected...');window.location='/studio/studioverification';</script>")
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editdistrict(request,districtid):
    logid = request.session.get('loginid')
    if logid:
        if request.method=='POST':
            districtname=request.POST.get("districtname")
            cat = tbl_district.objects.get(districtid=districtid)
            cat.districtname = districtname
            cat.save()
            return viewdistrict(request)
        cat = tbl_district.objects.get(districtid=districtid)
        return render(request,"Admin/editdistrict.html",{'c':cat})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editcategory(request, categoryid):
    logid = request.session.get('loginid')
    if logid:
        cob = Tbl_category.objects.get(categoryid=categoryid)  
        if request.method == 'POST':
            categoryname = request.POST.get("categoryname")
            cob.categoryname = categoryname
            if 'categoryimage' in request.FILES:
                cob.categoryimage = request.FILES['categoryimage'] 
            cob.save()
            return viewcategory(request)
        return render(request, "Admin/editcategory.html", {'c': cob})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def editlocation(request,locationid):
    logid = request.session.get('loginid')
    if logid:
        if request.method=='POST':
            locationname=request.POST.get("locationname")
            cat = tbl_location.objects.get(locationid=locationid)
            cat.locationname = locationname
            cat.save()
            return viewlocation(request)
        cat = tbl_location.objects.get(locationid=locationid)
        return render(request,"Admin/editlocation.html",{'c':cat})
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def all_payments(request):
    logid = request.session.get('loginid')
    if logid:
        payments = Tbl_payment.objects.select_related(
            'requestid__packageid__studioid',
            'requestid__customerid'  
        ).all()
        context = {'payments': payments}
        return render(request, 'Admin/viewpayment.html', context)
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")

from django.db.models import Count
def pie_chart(request):
    labels = []
    data = []

    # Query the number of payments received by each studio
    queryset = Tbl_payment.objects.values('requestid__packageid__studioid__studioname').annotate(total_payments=Count('paymentid'))

    for payment in queryset:
        labels.append(payment['requestid__packageid__studioid__studioname'])  # studio name
        data.append(payment['total_payments'])  # total payments per studio

    return render(request, 'Admin/piechart.html', {
        'labels': labels,
        'data': data,
    })

def excelreport(request):
    return render(request,"Admin/excelreport.html")

class ExportExcelPayment(View):
    def get(self, request):
        from_date = request.GET.get('from_date')
        to_date = request.GET.get('to_date')

        # Filter payments within the selected date range
        queryset = Tbl_payment.objects.filter(
            paymentdate__range=[from_date, to_date]
        ).values_list(
            'requestid__customerid__customername', 
            'requestid__customerid__email',
            'requestid__customerid__phone',
            'requestid__packageid__studioid__studioname',
            'requestid__requireddate',
            'requestid__noofdays',
            'iamount',
            'tamount',
            'camount',
            'paymentdate',
            'status'
        )

        # Excel File Configuration
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="payment_details.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Payments')

        # Define column headings
        row_num = 0
        columns = [
            'Customer Name', 'Email', 'Phone', 
            'Studio Name', 'Required Date', 'No. of Days',
            'Initial Amount', 'Total Amount', 'Commission Amount',
            'Payment Date', 'Status'
        ]

        # Add headers
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)

        # Date formatting style
        date_style = xlwt.XFStyle()
        date_style.num_format_str = 'DD-MM-YYYY'

        # Add data rows
        for row in queryset:
            row_num += 1
            for col_num, cell_value in enumerate(row):
                # Apply date formatting for date fields
                if col_num in [4, 9]:  # 'Required Date' and 'Payment Date'
                    if isinstance(cell_value, str):
                        try:
                            cell_value = datetime.strptime(cell_value, '%Y-%m-%d').date()
                        except ValueError:
                            pass  # If date format is incorrect, keep original
                    ws.write(row_num, col_num, cell_value, date_style)
                else:
                    ws.write(row_num, col_num, cell_value)

        wb.save(response)
        return response


def logout(request):
    logid = request.session.get('loginid')
    if logid:
        request.session.clear()
        return redirect('/')
    else:
        return HttpResponse("<script>alert('Authentication Requierd Please Login first');window.location='/login';</script>")