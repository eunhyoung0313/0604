"""listproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from todolist import views

urlpatterns = [
    path('logout/',views.logout,name="logout"),
    path('edit_comment/<int:post_pk>/<int:comment_pk>',views.edit_comment, name="edit_comment"),
    path('mypage',views.mypage, name="mypage"),
    path('registration/signup', views.signup, name="signup"),
    path('registration/login', views.login, name = "login"),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('detail_url/<int:post_pk>', views.detail, name="detail"),
    path('edit_url/<int:post_pk>', views.edit, name="edit"),
    path('delete/<int:post_pk>', views.delete, name="delete"),
    path('delete_comment/<int:post_pk>/<int:comment_pk>', views.delete_comment, name="delete_comment"),
    path('accounts/', include('allauth.urls')),
]
