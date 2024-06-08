from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import Home,Signin,Register,Signout,user,Upload,search,filters,Pic,update,dlt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('signin/',Signin,name='signin'),
    path('register',Register,name='register'),
    path('signout',Signout,name='signout'),
    path('user/<int:id>',user,name='user'),
    path('upload/<int:id>',Upload,name='upload'),
    path('search',search,name='search'),
    path('user/search',search,name='search'),
    path('filters',filters,name='filters'),
    path('user/pic/<int:upload_id>/', Pic, name='pic'),
    path('pic/<int:upload_id>/',Pic,name='pic'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',dlt,name='delete'),
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)