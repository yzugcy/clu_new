"""cultch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from .views import HomePageView, GameView
from .translations import set_language

urlpatterns = [
    path('management/', admin.site.urls),
    path('setlang/', set_language, name='set_language'),
    path('', GameView.as_view(), name='game'),

]

# Language Translation
urlpatterns += i18n_patterns(
    path('', HomePageView.as_view(), name='home'),
    path('user/', include('customauth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('courses/', include('course.urls')),
    path('blogs/', include('blog.urls')),
    path('virtualtour/', include('virtualtour.urls')),
    path('history/', include('history.urls')),
    path('readclassic/', include('readclassic.urls')),
    path('diago/', include('diago.urls')),
    path('west/', include('west.urls')),

)

# rosetta urls ------------------------------
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

# serve media files in development environment --------------------------------
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
