from __future__ import division

import datetime as dt
import os
import re

TEST_DIR = 'tests'
START_DT = '08:00 AM, DAY 1'

time_re = re.compile(r'(?P<hour>\d{2}):(?P<minute>\d{2}) (?P<period>\S{2}), DAY (?P<day>\d+)')


class RaceAverage(object):
    def __init__(self, race_start):
        self.start = self._to_minutes(**self._string_to_dict(race_start))

    def _string_to_dict(self, time_string):
        return [r.groupdict() for r in time_re.finditer(time_string)][0]

    def _to_minutes(self, day, hour, minute, period):
        day, hour, minute = int(day), int(hour), int(minute)
        if period == 'PM' and hour != 12:
            hour += 12
        if (period, hour) == ('AM', 12):
            hour = 0
        return day * 60 * 24 + hour * 60 + minute

    def avgMinutes(self, times):
        times = [self._string_to_dict(t) for t in times]
        times = [self._to_minutes(**t) for t in times]
        times = [t - self.start for t in times]
        return int(round(reduce(lambda x, y: x + y, times) / len(times)))


def test():
    race_average = RaceAverage(START_DT)
    files = os.listdir(TEST_DIR)
    for f in files:
        times = [line.strip() for line in open(os.path.join(TEST_DIR, f))]
        expected, _ = os.path.splitext(f)
        assert int(expected) == race_average.avgMinutes(times)


def main():
    test()


if __name__ == '__main__':
    main()
