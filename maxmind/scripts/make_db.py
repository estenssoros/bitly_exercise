# encoding=utf8
import os
import re
import sqlite3

import pandas as pd
from django.conf import settings
from django.db import connections

import common_env


def camel_to_snake(name):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
    return s.replace('__', '_')


class DBMaker(object):
    def __init__(self, db_path):
        self.conn = sqlite3.connect(os.path.join(settings.BASE_DIR, 'db.sqlite3'))
        self.curs = self.conn.cursor()
        self.db_path = db_path

    def insert_sqlite_db(self):
        for path, dirs, files in os.walk(self.db_path):
            for f in files:
                table_name, _ = os.path.splitext(f)
                table_name = table_name.lower().split('-')[-1]
                self.curs.execute('drop table if exists {}'.format(table_name))
                df = pd.read_csv(os.path.join(path, f), skiprows=1)
                cols = {col: camel_to_snake(col) for col in df.columns}
                df = df.rename(columns=cols)
                print 'inserting {} into sqlite...'.format(table_name)
                df = df.reset_index()
                df = df.rename(columns={'index': 'id'})
                groups = df.columns.to_series().groupby(df.dtypes).groups
                groups = {x.name: groups[x].tolist() for x in groups}
                if groups.get('object'):
                    for col in groups['object']:
                        df[col] = df[col].str.decode('cp1252')
                df.to_sql(table_name, self.conn, index=False, chunksize=500)
        self.kill()

    def kill(self):
        self.curs.close()
        self.conn.close()


def main():
    db_path = os.path.join(settings.BASE_DIR, 'maxmind', 'db')
    db_maker = DBMaker(db_path)
    db_maker.insert_sqlite_db()


if __name__ == '__main__':
    main()
