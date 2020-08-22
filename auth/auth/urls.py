from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('',include('gateway.urls')),
    path('admin/', admin.site.urls),
    #path to djoser end points
    # path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
	#path to our account's app endpoints
]
