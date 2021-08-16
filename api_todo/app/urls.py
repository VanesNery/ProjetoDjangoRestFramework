#Registro das urls para utilização na chamada da API
from django.db import router
from app.views import TodoViewSet

from rest_framework.routers import DefaultRouter

# from django.urls import path

# #lista de urls que podemos utilizar
# urlpatterns = [
#     path('', TodoListAndCreate.as_view()), #chamada na raiz da url
#     path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
# ]

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls