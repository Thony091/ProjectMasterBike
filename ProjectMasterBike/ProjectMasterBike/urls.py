"""
URL configuration for ProjectMasterBike project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # path('', include('seguridad.urls')),
    path('api/', include('rest_producto.urls')),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
]

#La ruta admin/ se mapea al panel de administración de Django.
#La ruta base '' se redirige a las URLs definidas en la aplicación core.
#La ruta api/ se mapea a las URLs definidas en la aplicación rest_producto.
#La ruta accounts/login/ utiliza la vista de inicio de sesión LoginView provista por Django, y se asigna el nombre login.
#Además, se especifica la plantilla registration/login.html para la vista de inicio de sesión.