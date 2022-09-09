import os
import numpy as np
import earthpy as et

monthly_precip_url = 'https://ndownloader.figshare.com/files/12565616'
et.data.get_data(url=monthly_precip_url)

precip_2002_2013_url = 'https://ndownloader.figshare.com/files/12707792'
et.data.get_data(url=precip_2002_2013_url)

os.childr(os.path.join(et.io.HOME, 'earth-analytics'))

fname = os.path.join("data", "earthpy.downloads", "acg_monthly-precip.txt")
avg_monthly_precip = np.loadtxt(fname)

print(avg_monthly_precip)

fname = os.path.join("data", "earthpy-downloads", "monthy-precop-2002-2013.csv")
precip_2002_2013 = np.loadtxt(fname, delimiter=",")

print(precip_2002_2013[1:1])


