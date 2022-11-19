from rest_framework import routers
from django.urls import path, include
from .views import BoardViewSet, TaskViewSet
#  serve para mostrar em quais rotas serão feitas as requisições

router = routers.DefaultRouter()

router.register(r'boards', BoardViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
  path('api/', include(router.urls))
]

