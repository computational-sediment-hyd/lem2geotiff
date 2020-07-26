#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import glob 
import os
import xarray as xr
import rioxarray
from pathlib import Path


# In[ ]:


def translate(filepath, valm1111=60000, valm9999=50000, dtype=np.uint16 ):
    """
    translate lem file to geotiff file

    Parameters
    ----------
    filepath : str
        a full path of a lem file
    valm1111 : float, default 60000
        value of the flag -1111 outside the data creation area
    valm9999 : float, default 50000
        value of the flag -9999 for the sea and land and water sections
    dtype : type, default np.uint16
        data type of a geotiff file
    """
    
    fpath = Path(filepath)
    
    # reading csv file
    df = pd.read_csv(fpath.with_suffix('.csv'), encoding='ShiftJIS',header=None, index_col=0)
    
    nx = int(df.loc['東西方向の点数'].values[0])
    ny = int(df.loc['南北方向の点数'].values[0])
    y1 = float(df.loc['区画左下X座標'].values[0])
    x0 = float(df.loc['区画左下Y座標'].values[0])
    y0 = float(df.loc['区画右上X座標'].values[0])
    x1 = float(df.loc['区画右上Y座標'].values[0])
    dx = float(df.loc['東西方向のデータ間隔'].values[0])
    dy = float(df.loc['南北方向のデータ間隔'].values[0])
    nepsg = int(df.loc['平面直角座標系番号'].values[0])
    
    # reading lem file
    with open(filepath, "r") as f:
        lines = f.readlines()
    
    # Important: The dimensions of the array must be in the order from y to x.
    arr = np.empty((ny, nx))
    for i, l in enumerate(lines) :
        ll = l.replace('\n','')
        s = ll[10:]
        v = [s[i: i+5] for i in range(0, len(s), 5)]
        arr[i,:] = np.array(v)
    
    # make xarray
    val = np.array(arr, np.float)
    
    # Changing the flag -9999 for the sea and land and water sections and the flag -1111 outside the data creation area into any given value.
    # dafault : -9999 to 50000, -1111 to 60000
    val = np.where(val == -1111, valm1111, val)
    val = np.where(val == -9999, valm9999, val)
    
    # changing data type(default uint16)
    val = val.astype(dtype)
    
    dx *= 100
    dy *= 100
    xarr = np.arange(x0,x1,dx)
    xarr = xarr + dx/2
    yarr = np.arange(y0,y1,-dy)
    yarr = yarr - dy/2
    
    epsg = str(6668 + nepsg)
    
    ds = xr.Dataset({'z': (['y','x'], val) }, coords={'x': xarr/100, 'y': yarr/100}) 
    ds = ds.rio.write_crs('EPSG:' + epsg, inplace = True)
    # ds.rio.reproject("epsg:****")
    
    # export geotiff file
    ds['z'].rio.to_raster( fpath.stem + '.tif')

