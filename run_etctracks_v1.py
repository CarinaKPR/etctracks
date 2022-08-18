#! /usr/bin/env python

import os
from define_data import info_data
from ident_etc import ident_etc
from track_etc import track_etc
from select_area import area_events
from include_mslp_wind2 import include_mslp,include_wind
from generate_table import mytable_etc0,mytable_etc1,mytable_etc2,mytable_etc3

### Output directory:

OPATH = os.getcwd()
print(OPATH)
ODIR = os.path.join(OPATH,'OUTPUT')
if not os.path.exists(ODIR):
   os.mkdir(ODIR)

print('Output files goes to the path OUTPUT.')

### Get imput data:

IDO=str()
print('You need to download the data from ECMWF and than start the program.')
IDO = input('Do you have the data yet(Y or N)?')
D1,DL,NT,data_path_str,data_path,file_name = info_data(IDO)

My_file = str(data_path_str+file_name)

### Get the limiar of vorticity:

LIMINAR = input('What liminar do you want to use (ex. 1.0e-5 or 1.5e-5)?')
LIM = float(LIMINAR)
print('The program will select events with the liminar of 850 hPa relative vorticity:',LIM,' s-1')

### Get the events:

ident = ident_etc(LIM,data_path,file_name,OPATH) #events of each time

track = track_etc() #join the times and track the events


### Get the area of interest:
print('Current working directory:',format(os.getcwd()))
AREA_Q = input('Do you want to select a restrict area of the events (Y/N)?')
if AREA_Q == 'Y':
   
   LON_MIN = input('Give the limits. Minimun longitude (just positive values):')
   LON_MAX = input('Maximun longitude (just positive values):')
   LAT_MIN = input('Minimun latitude (south):')
   LAT_MAX = input('Maximun latitude (north):')
   selec = area_events(LON_MIN,LON_MAX,LAT_MIN,LAT_MAX)   
else:
   print('OK.')
### Imput wind and pressure data:

WI_MSP_Q = input('Do you have a file of surface winds and mean sea level pressure similar to vorticity (spacial and temporal size) (Y/N)?')
if WI_MSP_Q == 'Y' and AREA_Q == 'Y':
   FILE_AREA = 'OUTPUT/etc_vort_area.npz'
   FILE_MSP = input('Give the mean sea level data:')
   FILE_WID = input('Give the 10 meter wind data:')
   IN_MSLP = include_mslp(FILE_MSP,FILE_AREA)
   FILE_G = 'OUTPUT/etc_vort_area_mslp.npz'
   IN_WIND = include_wind(FILE_WID,FILE_G)
   FILE_GW = 'OUTPUT/etc_vort_area_mslp_wind.npz'
   TABLE = mytable_etc3(FILE_GW,My_file,LON_MIN,LON_MAX,LAT_MIN,LAT_MAX)
elif WI_MSP_Q == 'Y' and AREA_Q == 'N':
   FILE_ = 'OUTPUT/etc_track.npz'
   FILE_MSP = input('Give the mean sea level data:')
   FILE_WID = input('Give the 10 meter wind data:')
   IN_MSLP = include_mslp(FILE_MSP,FILE_)
   FILE_G = 'OUTPUT/etc_vort_area_mslp.npz'
   IN_WIND = include_wind(FILE_WID,FILE_G)
   FILE_GW = 'OUTPUT/etc_vort_area_mslp_wind.npz'
   TABLE = mytable_etc2(FILE_GW,My_file)
elif WI_MSP_Q == 'N' and AREA_Q == 'Y':
   FILE_ = 'OUTPUT/etc_vort_area.npz'
   TABLE = mytable_etc1(FILE_,My_file,LON_MIN,LON_MAX,LAT_MIN,LAT_MAX)
elif WI_MSP_Q == 'N' and AREA_Q == 'N':
   FILE_ = 'OUTPUT/etc_track.npz'
   TABLE = mytable_etc0(FILE_,My_file)
### Generate a table of the events:
#if WI_MSP_Q == 'Y':
#   GEN_TABLE = 'generate table with pressure and wind data'
#elif WI_MSP_Q == 'N':
 #  GEN_TABLE = 'generate table without pressure and wind data'







