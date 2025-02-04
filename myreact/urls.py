"""myreact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView



urlpatterns = [
    # path('',FoodsListView.as_view()),
    # path('<pk>',FoodsDetailView.as_view()),
    # path('',RestaurantsListView.as_view()),
    # path('<pk>',RestaurantsDetailView.as_view())

    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', include('restaurant.api.urls')),
    # path('Foods/', include('restaurant.api.urls')),
    path('admin/', admin.site.urls),


    re_path('.*', TemplateView.as_view(template_name='index.html')),
]
