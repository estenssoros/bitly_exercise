from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^loc_detail/(?P<loc_id>[0-9.]+)/$', views.loc_detail),
    url(r'^api/geo_data/$', views.GeoDataAPI.as_view()),
    url(r'^api/loc_data/$', views.LocAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
