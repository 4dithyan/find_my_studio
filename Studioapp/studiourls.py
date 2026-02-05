from django.urls import path
from Studioapp import views
urlpatterns = [
    path('studiohome/',views.studiohome,name='studiohome'),
    path('workdetails/',views.workdetails,name='workdetails'),
    path('work_process/',views.work_process,name='work_process'),
    path('workimage/',views.workimage,name='workimage'),
    path('workimage_process/',views.workimage_process,name='workimage_process'),
    path('package/',views.package,name='package'),
    path('package_process/',views.package_process,name='package_process'),
    path('requestview/', views.requestview, name='requestview'),
    path('accept/<int:requestid>/', views.accept_request, name='accept_request'),
    path('reject/<int:requestid>/', views.reject_request, name='reject_request'),
    path('viewworkdetails',views.viewworkdetails,name="viewworkdetails"),
    path('work_image_view',views.work_image_view,name="work_image_view"),
    path('edit-work/<int:workid>/', views.edit_work, name='edit_work'),
    path('delete-work/<int:workid>/', views.delete_work, name='delete_work'),    
    path('edit-work-image/<int:workimageid>/', views.edit_work_image, name='edit_work_image'),
    path('delete-work-image/<int:workimageid>/', views.delete_work_image, name='delete_work_image'),
    path('package_details_view',views.package_details_view,name="package_details_view"),
    path('edit-package/<int:packageid>/', views.edit_package, name='edit_package'),
    path('delete-package/<int:packageid>/',views.delete_package, name='delete_package'),
    path('viewpayment',views.viewpayment,name="viewpayment"),
    path('logout',views.logout,name="logout"),

]
