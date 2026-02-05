from django.urls import path
from Adminapp import views
from .views import ExportExcelPayment

urlpatterns = [
   path('index/',views.index,name="index"),
   path('district/',views.district,name='district'),
   path('district_process/',views.district_process,name='district_process'),
   path('location',views.location,name='location'),
   path('location_process',views.location_process,name='location_process'),
   path('category/',views.category,name='category'),
   path('category_process',views.category_process, name="category_process"),
   path('viewdistrict',views.viewdistrict,name='viewdistrict'),
   path('deletedistrict/<districtid>',views.deletedistrict,name="deletedistrict"),
   path('viewcategory',views.viewcategory,name='viewcategory'),
   path('deletecategory/<categoryid>',views.deletecategory,name="deletecategory"),
   path('viewlocation',views.viewlocation,name='viewlocation'),
   path('deletelocation/<locationid>',views.deletelocation,name="deletelocation"),
   path( 'filllocation', views. filllocation, name= 'filllocation'),
   path( 'studioverification', views. studioverification, name= 'studioverification'),
   path('studioaccept/<loginid>',views.studioaccept,name="studioaccept"),
   path('studioreject/<loginid>',views.studioreject,name="studioreject"),
   path('editdistrict/<districtid>',views.editdistrict,name="editdistrict"),
   path('editcategory/<categoryid>',views.editcategory,name="editcategory"),
   path('editlocation/<locationid>',views.editlocation,name="editlocation"),
   path('all_payments',views.all_payments,name="all_payments"),
   path('pie_chart',views.pie_chart,name="pie_chart"),
   path('excelreport',views.excelreport,name="excelreport"),
   path('export_excel/', ExportExcelPayment.as_view(), name='export_excel'),
   path('logout',views.logout,name="logout"),

   

]
