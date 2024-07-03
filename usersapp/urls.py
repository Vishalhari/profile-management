from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
     path("",views.Homepage,name="home"),
     path("registeruser", views.registeruser, name='registeruser'),
     path("userlogin", views.userlogin, name='userlogin'),
     path("userpanel", views.userpanel, name='userpanel'),
     path("adminpanel", views.adminpanel, name='adminpanel'),
     path("profilelist", views.profilelist, name='profilelist'),
     path("profiledetails/<int:profile_id>/", views.profiledetails),
     path("deleteprofile/<int:profile_id>/", views.deleteprofile),


     path("logout", views.logoutuser,name="logout"),
     # path("deleteuser/<int:user_id>/", views.deleteuser),
] + static(settings.STATIC_URL,doument_root=settings.STATIC_ROOT)
static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
