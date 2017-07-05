from django.conf.urls import include, url
from django.contrib import admin

from landing.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^race_average/', include('race_average.urls')),
    url(r'^maxmind/', include('maxmind.urls')),

]
