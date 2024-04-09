
from app_livraria import views
from django.urls import path, include 
from django.contrib import admin

urlpatterns = [
   path('admin/' , admin.site.urls),
   path('auth/', include('app_livraria.urls'))
    
        
    
]

