from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^api/geo_data/$', views.GeoDataAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
