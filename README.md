# Bitly exercise

Backend Engineer

# Django Respt API Framework and Leaflet

***

## getting started

make sure you have wget installed

```
$ apt-get wget
$ brew install wget
```

run startup script

```
$ ./start.sh
```

- downloads and unzips maxmind dataset
- copies static files from my cdn
- installs requirements
- migrates Django admin tables to sqlite database
- runs script to upload maxmind data to sqlite3
- starts webserver

***

## Race Average
Given an array of strings or race completion times, parse for total time since beginning of race.

see **race_average/scripts/tests/*.txt** and **race_average/scripts/race_averages.py**

***

## Maxmind

powered by leaflet and leaflet-markcluster

makes ajax calls to **/maxmind/api/geo_data** and **/maxmind/api/loc_data**

returns the first 2000 data entries
```
curl 'http://127.0.0.1:8000/maxmind/api/geo_data/'
[{
  "city": null,
  "loc_id": 1,
  "country": "O1",
  "region": null,
  "area_code": null,
  "longitude": 0.0,
  "metro_code": null,
  "postal_code": null,
  "latitude": 0.0,
  "id": 0
}, {
  "city": null,
  "loc_id": 2,
  "country": "AP",
  "region": null,
  "area_code": null,
  "longitude": 105.0,
  "metro_code": null,
  "postal_code": null,
  "latitude": 35.0,
  "id": 1
},...]
```

```
$ curl 'http://127.0.0.1:8000/maxmind/api/loc_data/?loc_id=206'
{
  "start_loc": {
    "city": null,
    "loc_id": 206,
    "country": "TD",
    "region": null,
    "area_code": null,
    "longitude": 19.0,
    "metro_code": null,
    "postal_code": null,
    "latitude": 15.0,
    "id": 205
  },
  "children": []
}
```

***

# TO DO

- include pagination in api/geodata
- examine database further for parent-child connections
