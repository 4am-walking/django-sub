from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"tasks", views.AuthView, "task")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/login/", include(router.urls)),
]
