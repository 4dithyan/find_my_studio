from django.urls import path
from Guestapp import views
urlpatterns = [
   path('login/',views.login,name='login'),
   path('login_process/',views.login_process,name='login_process'),
   path('',views.guesthome,name='guesthome'),
   path('studioreg/',views.studioreg,name='studioreg'),
   path('studioreg_process/',views.studioreg_process,name='studioreg_process'),
   path('customerreg/',views.customerreg,name='customerreg'),
   path('customerreg_process/',views.customerreg_process,name='customerreg_process'),
   path('filllocations',views.filllocations,name="filllocations"),
   path('forgotpassword',views.forgotpassword,name="forgotpassword"),

  
]
