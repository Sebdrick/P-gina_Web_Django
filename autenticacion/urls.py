from django.urls import path
from .views import VRegistro  
from .views import cerrar_sesion  
from .views import logear                                                 

urlpatterns = [

    path('', VRegistro.as_view(), name="Autenticacion"),      
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"), 
    path('logear', logear, name="logear"),             

]