import obspy as obs
from yaml import dump
from datetime import datetime as dt

dlsv = "dataless/*"
net = "IR"
dlsv = obs.read_inventory(dlsv)
date = dt.now().strftime("%Y%m%d")

data = {}
for network in dlsv:
    for station in network:
        code = station.code
        lat = station.latitude.real
        lon = station.longitude.real
        elv = station.elevation.real
        st = station.start_date
        et = station.end_date
        st = st.isoformat() if st else None
        et = et.isoformat() if et else None
        d = {"starttime": st,
             "endtime": et,
             "latitude":lat,
             "longitude":lon,
             "elevation":elv}
        if code not in data:
            data[code] = []
        data[code].append(d)
        
with open(f"{net}_{date}.yml", "w") as outfile:
    dump(data, outfile, default_flow_style=False, sort_keys=False)
