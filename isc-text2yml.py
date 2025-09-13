from numpy import nan
from yaml import dump
from datetime import datetime as dt

'''
you can download all stations info registered in ISC using:
 "https://www.isc.ac.uk/registries/"
and run this script to convert them.
'''

data = []
codes = []
now = dt.now()

with open("station.txt") as f, open(f"ISC_{now.strftime('%Y%m%d')}.yml", "w") as g:
    next(f)
    for l in f:
        code = l[4:9]
        if code in codes:
            continue
        codes.append(code)
        lat = float(l[10:19].strip()) if l[10:19].strip() else nan
        lon = float(l[20:29]) if l[20:29].strip() else nan
        elv = float(l[30:35]) if l[30:35].strip() else nan
        st = l[48:68] if l[48:68].strip() else nan
        et = l[74:94] if l[74:74].strip() else nan
        info = {"code": code,
             "starttime": st,
             "endtime": et,
             "latitude": lat,
             "longitude": lon,
             "elevation": elv}
        data.append(info)
    dump(data, g, default_flow_style=False, sort_keys=False)
    
        
