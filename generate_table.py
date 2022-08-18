import numpy as np
from define_functions import latlon2km
from define_timax import timax

FILE_AREA1 = 'OUTPUT/etc_vort_area_mslp.npz'

def mytable_etc0(file_etc, file_name):
    #np_load_old = np.load
    #np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
    my_data = np.load(file_etc)
    file_dat = str(file_name)
    events = my_data['events']
    fil=open('OUTPUT/table_etcs', 'w+')
    fil.write('Table of extratropical cyclones of '+file_dat+'\n')
    fil.write('Number of event\t\tFirst Date\t\tLast Date\t\tDuration(h)\t\tTraveled distance(Km)\t\tSpeed(Km/h)\n')
    T_T,D_0,H_0,D_L,H_L = timax(file_name)
    if H_L == 23:
        delta = 1
    elif H_L == 18:
        delta = 6
    for xx in range(len(events)):
        number_event = str(xx + 1)
        first_date = str(events[xx]['day'][0]+'/'+events[xx]['month'][0]+'/'+events[xx]['year'][0]+' - '+events[xx]['hour'][0])
        last_date = str(events[xx]['day'][-1]+'/'+events[xx]['month'][-1]+'/'+events[xx]['year'][-1]+' - '+events[xx]['hour'][-1])
        duration = int(events[xx]['age'])
        duration_h = duration*delta
        dist_event = 0
        for zz in range(duration-1):
             ww = zz + 1
             lat1 = events[xx]['lat'][zz]
             lon1 = events[xx]['lon'][zz]
             lat2 = events[xx]['lat'][ww]
             lon2 = events[xx]['lon'][ww]
             dist_zz = latlon2km(lon1,lat1,lon2,lat2)
             dist_event = dist_event + dist_zz
        dist_event_r = round(dist_event, 1)
        speed_r = round(dist_event/duration_h,1)
        fil.write('%s:\t\t%s\t\t%s\t\t%i\t\t%f\t\t%f\n' % (number_event,first_date,last_date,duration_h,dist_event_r,speed_r))

def mytable_etc1(file_etc, file_name,lon_min,lon_max,lat_min,lat_max):
    #np_load_old = np.load
    #np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
    my_data = np.load(file_etc)
    file_dat = str(file_name)
    lon_min_ = str(lon_min)
    lon_max_ = str(lon_max)
    lat_min_ = str(lat_min)
    lat_max_ = str(lat_max)
    events = my_data['events']
    fil=open('OUTPUT/table_etcs_area', 'w+')
    fil.write('Table of extratropical cyclones of '+file_dat+', area: longitude:'+lon_min_+' to '+lon_max_+' and latitude: '+lat_min_+' to '+lat_max_+'\n')
    fil.write('Number of event\t\tFirst Date\t\tLast Date\t\tDuration(h)\t\tTraveled distance(Km)\t\tSpeed(Km/h)\n')
    T_T,D_0,H_0,D_L,H_L = timax(file_name)
    if H_L == 23:
        delta = 1
    elif H_L == 18:
        delta = 6
    for xx in range(len(events)):
        number_event = str(xx + 1)
        first_date = str(events[xx]['day'][0]+'/'+events[xx]['month'][0]+'/'+events[xx]['year'][0]+' - '+events[xx]['hour'][0])
        last_date = str(events[xx]['day'][-1]+'/'+events[xx]['month'][-1]+'/'+events[xx]['year'][-1]+' - '+events[xx]['hour'][-1])
        duration = int(events[xx]['age'])
        duration_h = duration*delta
        dist_event = 0
        for zz in range(duration-1):
             ww = zz + 1
             lat1 = events[xx]['lat'][zz]
             lon1 = events[xx]['lon'][zz]
             lat2 = events[xx]['lat'][ww]
             lon2 = events[xx]['lon'][ww]
             dist_zz = latlon2km(lon1,lat1,lon2,lat2)             
             dist_event = dist_event + dist_zz
        dist_event_r = round(dist_event, 1)
        speed_r = round(dist_event/duration_h,1)
        fil.write('%s:\t\t%s\t\t%s\t\t%i\t\t%f\t\t%f\n' % (number_event,first_date,last_date,duration_h,dist_event_r,speed_r))

def mytable_etc2(file_etc, file_name):
    #np_load_old = np.load
    #np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
    my_data = np.load(file_etc)
    file_dat = str(file_name)
    events = my_data['events']
    fil=open('OUTPUT/table_etcs_mslp_wind', 'w+')
    fil.write('Table of extratropical cyclones of '+file_dat+'\n')
    fil.write('Number of event\t\tFirst Date\t\tLast Date\t\tMinimun Pressure\t\tDuration(h)\t\tTraveled distance(Km)\t\tSpeed(Km/h)\t\tMaximun Wind(Km/h)\n')
    T_T,D_0,H_0,D_L,H_L = timax(file_name)
    if H_L == 23:
        delta = 1
    elif H_L == 18:
        delta = 6
    for xx in range(len(events)):
        number_event = str(xx + 1)
        first_date = str(events[xx]['day'][0]+'/'+events[xx]['month'][0]+'/'+events[xx]['year'][0]+' - '+events[xx]['hour'][0])
        last_date = str(events[xx]['day'][-1]+'/'+events[xx]['month'][-1]+'/'+events[xx]['year'][-1]+' - '+events[xx]['hour'][-1])
        duration = int(events[xx]['age'])
        duration_h = duration*delta
        p_min = []
        for yy in range(duration):
             p_min.append(float(events[xx]['min_mslp'][yy]))
        min_press = int(min(p_min)*0.01)
        w_max = []
        for kk in range(duration):
             w_max.append(float(events[xx]['max_wind'][kk]))
        max_win = int(max(w_max)*3.6)
        dist_event = 0
        for zz in range(duration-1):
             ww = zz + 1
             lat1 = events[xx]['lat'][zz]
             lon1 = events[xx]['lon'][zz]
             lat2 = events[xx]['lat'][ww]
             lon2 = events[xx]['lon'][ww]
             dist_zz = latlon2km(lon1,lat1,lon2,lat2)             
             dist_event = dist_event + dist_zz
        dist_event_r = round(dist_event, 1)
        speed_r = round(dist_event/duration_h,1)
        fil.write('%s:\t\t%s\t\t%s\t\t%i\t\t%i\t\t%f\t\t%f\t\t%f\n' % (number_event,first_date,last_date,min_press,duration_h,dist_event_r,speed_r,max_win))

def mytable_etc3(file_etc, file_name,lon_min,lon_max,lat_min,lat_max):
    #np_load_old = np.load
    #np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
    my_data = np.load(file_etc)
    file_dat = str(file_name)
    lon_min_ = str(lon_min)
    lon_max_ = str(lon_max)
    lat_min_ = str(lat_min)
    lat_max_ = str(lat_max)
    events = my_data['events']
    fil=open('OUTPUT/table_etcs_area', 'w+')
    fil.write('Table of extratropical cyclones of '+file_dat+', area: longitude:'+lon_min_+' to '+lon_max_+' and latitude: '+lat_min_+' to '+lat_max_+'\n')
    fil.write('Number of event\t\tFirst Date\t\tLast Date\t\tMinimun Pressure\t\tDuration(h)\t\tTraveled distance(Km)\t\tSpeed(Km/h)\t\tMaximun Wind(Km/h)\n')
    T_T,D_0,H_0,D_L,H_L = timax(file_name)
    if H_L == 23:
        delta = 1
    elif H_L == 18:
        delta = 6
    for xx in range(len(events)):
        number_event = str(xx + 1)
        first_date = str(events[xx]['day'][0]+'/'+events[xx]['month'][0]+'/'+events[xx]['year'][0]+' - '+events[xx]['hour'][0])
        last_date = str(events[xx]['day'][-1]+'/'+events[xx]['month'][-1]+'/'+events[xx]['year'][-1]+' - '+events[xx]['hour'][-1])
        duration = int(events[xx]['age'])
        duration_h = duration*delta
        p_min = []
        for yy in range(duration):
             p_min.append(float(events[xx]['min_mslp'][yy]))
        min_press = int(min(p_min)*0.01)
        w_max = []
        for kk in range(duration):
             w_max.append(float(events[xx]['max_wind'][kk]))
        max_win = int(max(w_max)*3.6)
        dist_event = 0
        for zz in range(duration-1):
             ww = zz + 1
             lat1 = events[xx]['lat'][zz]
             lon1 = events[xx]['lon'][zz]
             lat2 = events[xx]['lat'][ww]
             lon2 = events[xx]['lon'][ww]
             dist_zz = latlon2km(lon1,lat1,lon2,lat2)             
             dist_event = dist_event + dist_zz
        dist_event_r = round(dist_event, 1)
        speed_r = round(dist_event/duration_h,1)
        fil.write('%s:\t\t%s\t\t%s\t\t%i\t\t%i\t\t%f\t\t%f\t\t%f\n' % (number_event,first_date,last_date,min_press,duration_h,dist_event_r,speed_r,max_win))

