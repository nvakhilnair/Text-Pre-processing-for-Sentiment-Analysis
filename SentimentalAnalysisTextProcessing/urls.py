
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = []
if settings.ADMIN_ENABLED is True:
    urlpatterns += [path('admin/', admin.site.urls),]
urlpatterns += [path('', include('textProcessing.urls')),]
