from django.db import connections
from tqdm import tqdm

import common_env

curs = connections['default'].cursor()

sql = '''select end_ip_num from blocks where start_ip_num={}'''


def find_children(start_ip):
    results = []
    curs.execute(sql.format(start_ip))
    end_ip = [x[0] for x in curs.fetchall()][0]
    if end_ip == start_ip:
        return []
    if end_ip:
        results.extend(end_ip)
        results.extend(find_children(end_ip[0]))
    return results



curs.execute('select start_ip_num from blocks')
start_ips = [x[0] for x in curs.fetchall()]
print find_children(16874805)
