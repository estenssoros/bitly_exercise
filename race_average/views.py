import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from scripts.race_averages import RaceAverage


def home(request):
    context = {'race_start': '08:00 AM, DAY 1'}
    race_average = RaceAverage(**context)
    test_dir = os.path.join(settings.BASE_DIR, 'race_average', 'scripts', 'tests')
    test_strings = []
    for f in os.listdir(test_dir):
        times = [line.strip() for line in open(os.path.join(test_dir, f))]
        test_strings.append({'string': str(times),
                             'result': race_average.avgMinutes(times)})
    context['test_strings'] = test_strings
    return render(request, 'race_average/home.html', context)
