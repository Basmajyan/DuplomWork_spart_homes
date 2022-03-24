
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.adminRedirect),
    path('register', views.registration),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('solution', views.solution),
    path('clients', views.clients),
    path('utilites', views.utilites),
    path('connects', views.homeConnect),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)