"""nodeMcu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from index.api.views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('site/', include('index.urls', namespace='index')),
    path('api/', include('index.api.urls', namespace='index-api')),
    path('schema/', get_schema_view(
        title="Esp-API",
        description="API for the Esp.dev",
        version="1.0.0"
    ), name="esp-schema"),
    path('', include_docs_urls(
        title="Esp-API",
        description="API for the Esp.dev",
    ), name="esp-docs"),

]
