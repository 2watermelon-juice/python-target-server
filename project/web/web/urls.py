"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from web.views import HomeView
from web.views import UserCreateView, UserCreateDoneTV		# 추가

# from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),					# 추가
    path('accounts/register/', UserCreateView.as_view(), name='register'),			# 추가
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),		# 추가

    path('', HomeView.as_view(), name='home'),	
    path('bookmark/', include(('bookmark.urls', 'bookmark'))),
    path('blog/', include(('blog.urls', 'blog'))),
    path('photo/', include(('photo.urls', 'photo'))),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

