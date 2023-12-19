from django.contrib import admin
from django.urls import path

from todos.views import todos_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", todos_list),
]
