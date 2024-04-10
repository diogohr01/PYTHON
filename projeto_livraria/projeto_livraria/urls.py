from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    #rota, view responsavel, nome de referencia
    path('admin/', admin.site.urls),
    path('', include('app_livraria.urls'))
      # Redirecione a URL raiz para o aplicativo de autenticação    
    
]

