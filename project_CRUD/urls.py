"""project_CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main.views import index, blog, posting, new_post, remove_post

# 이미지 업로드
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지, url이름은 index
    path('', index, name='index'),
    # URL:8000/blog에 접속하면 blog 페이지, url이름은 blog
    path('blog/', blog, name='blog'),
    # URL:8000/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>', posting, name='posting'),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)