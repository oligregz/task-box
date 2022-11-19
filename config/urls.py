from django.contrib import admin
from django.urls import path, include

#  esse arquivo serve para "avisar" que as rotas foram implementadas 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('taskbox.urls'))
]
