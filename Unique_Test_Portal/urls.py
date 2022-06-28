"""Unique_Test_Portal URL Configuration

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
from enroll import views
from enroll.entities._class.urls import class_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("liststudent/", views.student_list, name="student_list" ),
    path("", views.load_index, name="load_index"),
    path("add_student/", views.add_student, name="add_student"),
    
    path("delete/<int:id>/", views.deletestudent, name="deletestudent"),
    path("<int:id>/", views.updatestudent, name="updatestudent"),
]
# urlpatterns = [
#      path('delete/<int:obj_id>/',views.deletestudent,name="del_data")
# ]

urlpatterns.extend(class_urlpatterns)
