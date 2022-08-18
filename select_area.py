## This program select the extratropical cyclones of an area em save at a file.
## Carina Padilha Reinke
## Data:23/03/2022
## Use the file output/etc_track.npz at OUTPUT path
## File saved:output/etc_track_area.npz

import numpy as np
from deepdiff import DeepDiff

def area_events(LONMIN,LONMAX,LATMIN,LATMAX):
    fname = 'OUTPUT/etc_track.npz'
    LON_MIN = float(LONMIN)
    LON_MAX = float(LONMAX)
    LAT_MIN = float(LATMIN)
    LAT_MAX = float(LATMAX)
    #np_load_old = np.load
    #np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
    data_eve = np.load(fname)
    events = data_eve['events']
    event2 = []
    for ed in range(len(events)):
        numb = events[ed]['age']
        for ad in range(numb):
            lon_i = events[ed]['lon'][ad]
            if (LON_MIN <= lon_i) and (LON_MAX >= lon_i):
               event2.append(events[ed])
    event3 = []
    for ed in range(1,len(event2)):
        ed_ = ed - 1
        m_event2 = event2[ed_]
        n_event2 = event2[ed]
        diferenca = DeepDiff(m_event2,n_event2)
        if diferenca != {}:
            event3.append(event2[ed])
    event4 = []
    for ed in range(len(event3)):
        numb2 = event3[ed]['age']
        for ad in range(numb2):
            lat_i = event3[ed]['lat'][ad]
            if (LAT_MIN <= lat_i) and (LAT_MAX >= lat_i):
               event4.append(event3[ed])
    event5 = []
    for ed in range(1,len(event4)):
        ed_ = ed - 1
        m_event4 = event4[ed_]
        n_event4 = event4[ed]
        diferenca = DeepDiff(m_event4,n_event4)
        if diferenca != {}:
           event5.append(event4[ed])
    etc_area = 'OUTPUT/etc_vort_area'
    np.savez(etc_area, events=event5)
    print('Number of events of the area:',len(event5))
    print('The events are saved at the file:',etc_area)
    return event5
