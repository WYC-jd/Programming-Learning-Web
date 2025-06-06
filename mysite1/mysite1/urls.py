"""
URL configuration for mysite1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from videos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('videos/login/', views.user_login, name='login'),
    path('videos/logout/', views.user_logout, name='logout'),
    path('videos/upload_video/', views.upload_video, name='upload_video'),
    path('videos/video_list/', views.video_list, name='video_list'),
    path('videos/<int:video_id>/like/', views.like_video, name='like_video'),
    path('videos/<int:video_id>/comment/', views.comment_video, name='comment_video'),
    path('videos/announcement/', views.announcement, name='announcement'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
