"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import TaskViewSet, SecureHelloView

# Set up the DRF router
router = DefaultRouter()
router.register('tasks', TaskViewSet)  # 'tasks' will be the endpoint, e.g., /api/tasks/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  
    path('api/todos/', include('myapp.urls')),  
    # Removed legacy token auth endpoint to avoid confusion
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('access-denied/', SecureHelloView.as_view(), name='access-denied'),
]

