from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Block, Location


def home(request):
    return render(request, 'maxmind/home.html')


class GeoDataAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        blocks = Location.objects.all().order_by('?')[:2000].values()
        return Response(blocks)
