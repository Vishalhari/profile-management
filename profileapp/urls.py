from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
     path("createprofile",views.createprofile,name='createprofile'),
     # path("userslist", views.userlist, name='userslist'),
     # path("userscreate", views.createusers, name='userscreate'),
     # path("editusers/<int:user_id>/", views.updateusers),
     # path("deleteuser/<int:user_id>/", views.deleteuser),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
