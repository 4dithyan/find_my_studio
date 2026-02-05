from django.urls import path
from Customerapp import views
urlpatterns = [
    path('customerhome/',views.customerhome,name='customerhome'),
    path('studioview',views.studioview,name="studioview"),
    path('filllocations',views.filllocations,name="filllocations"),
    path('fillstudios',views.fillstudios,name="fillstudios"),
    path('studioview',views.studioview,name="studioview"),
    path('categoryview/<int:studioid>/', views.categoryview, name='categoryview'),
    path('work/<int:studioid>/<int:categoryid>', views.work, name='work'),
    path('package/<int:studioid>/<int:categoryid>', views.package, name='package'),
    path('workimage/<studioid>/<categoryid>/<workid>',views.workimage,name="workimage"),
    path('packagesingleview/<studioid>/<packageid>',views.packagesingleview,name="packagesingleview"),
    path('bookingprocess/<packageid>',views.bookingprocess,name="bookingprocess"),
    path('confirmation',views.confirmation,name="confirmation"),
    path('payment/<requestid>',views.payment,name="payment"),
    path('logout',views.logout,name="logout"),
    path('cpaymentview',views.cpaymentview,name="cpaymentview"),
    path('feedback/<requestid>',views.feedback,name="feedback"),
    path('fetchreviews/', views.fetchreviews, name='fetchreviews'),

]