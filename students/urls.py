"""students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from studentsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('listone/', views.listone),
	path('listall/', views.listall),
    path('', views.index),
    path('index/', views.index),
    
	path('post/', views.post), # POST 傳送表單
	path('post1/', views.post1), #資料新增，資料不驗證
	path('post2/', views.post2), #資料新增，資料作驗證

	path('delete/<int:id>/', views.delete),
	
	path('edit/<int:id>/', views.edit), # 由 瀏覽器 開啟
	path('edit/<int:id>/<str:mode>', views.edit), # 由 edit.html 按 送出 鈕

	path('edit2/<int:id>/<str:mode>', views.edit2),
	path('postform/', views.postform), # 表單驗證
]
