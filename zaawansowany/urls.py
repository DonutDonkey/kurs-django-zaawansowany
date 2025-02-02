"""zaawansowany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from biblioteka.views import glowny, nowy_form, wysylanie_maila
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetView, PasswordChangeDoneView, PasswordResetConfirmView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('nowy_form', nowy_form, name='nowy_form'),
    path('', glowny),
    # path('email/', wysylanie_maila)
    path('password_reset', PasswordResetView.as_view()),
    path('password_reset_done', PasswordChangeDoneView.as_view()),
    path('password_reset_confirm/<uidb64>/<token>/',  PasswordResetConfirmView.as_view()),
    path('password_reset_complete',  PasswordResetCompleteView.as_view())

]

import debug_toolbar
from django.conf import settings
from django.urls import include, path

# urlpatterns = [
#     path('__debug__/', include(debug_toolbar.urls)),
# ]