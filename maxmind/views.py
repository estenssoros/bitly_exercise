from pprint import pprint

import pandas as pd
from django.db import connections
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Block, Location

curs = connections['default'].cursor()


def home(request):
    return render(request, 'maxmind/home.html')


def loc_detail(request, loc_id):
    return render(request, 'maxmind/location_detail.html', {'loc_id': loc_id})


class GeoDataAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # blocks = Location.objects.all().order_by('?')[:2000].values()
        blocks = Location.objects.all()[:2000].values()
        return Response(blocks)


def query_sqlite(sql):
    curs.execute(sql)
    desc = [x[0] for x in curs.description]
    rows = [dict(zip(desc, x)) for x in curs.fetchall()]
    if len(rows) == 1:
        return rows[0]
    return rows


class LocAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        loc_id = request.GET.get('loc_id')
        # get start location
        start_loc = query_sqlite('select * from location where loc_id = %s' % loc_id)
        response = {'start_loc': start_loc, 'children': []}
        # get start_ip
        start_ips = query_sqlite('select * from blocks where loc_id = %s' % loc_id)
        children = []
        if len(start_ips) > 0:
            for start_ip in start_ips:
                child = query_sqlite('select * from blocks where start_ip_num = %s' % start_ip['end_ip_num'])
                if child:
                    response['children'].append(query_sqlite('select * from location where loc_id = %s' % child['loc_id']))
        return Response(response)
