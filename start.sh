#!/bin/bash
zip="GeoLiteCity-latest.zip"
wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity_CSV/$zip
unzip -o -d maxmind/db $zip
rm $zip

static_dir="maxmind/static/maxmind"
mkdir -p $static_dir/js
mkdir -p $static_dir/css
wget -O $static_dir/js/leaflet.markercluster-src.js https://s3.amazonaws.com/sebsbucket/cdn/leaflet.markercluster-src.js
wget -O $static_dir/css/MarkerCluster.Default.css https://s3.amazonaws.com/sebsbucket/cdn/MarkerCluster.Default.css
wget -O $static_dir/css/MarkerCluster.css https://s3.amazonaws.com/sebsbucket/cdn/MarkerCluster.css

pip install -r requirements.txt

python manage.py migrate
python maxmind/scripts/make_db.py
python manage.py runserver 0.0.0.0:8000
