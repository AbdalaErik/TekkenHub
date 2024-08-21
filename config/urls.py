"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name = 'index.html'), name = 'index'),
    path("personagens/", PersonagemListView.as_view(), name = 'personagemList'),
    path("personagens/<int:pk>/", PersonagemDetailView.as_view(), name = 'personagemDetail'),
    path("mecanicas/", MecanicaView.as_view(), name = 'mecanicas'),
    path("terminologia/", TermoView.as_view(), name = 'terminologia'),
    path("mapas/", MapaView.as_view(), name = 'mapas'),
    path("patch_notes/", PatchNoteView.as_view(), name = 'patch_notes'),
    path("sobre/", TemplateView.as_view(template_name = 'sobre.html'), name = 'sobre')
]
