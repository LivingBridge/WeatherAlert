# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 18:23:44 2015

@author: Ian Gagnon
"""

from matplotlib import numpy as np
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import pywapi
import string
import smtplib

#You must change PrivateData.txt to a txt file containing your private data.
#An example PrivateData.txt file is given in the repository and titled "PrivateDataEx.txt"
fromaddr,toaddr,pswd = np.genfromtxt('PrivateData.txt',
                                  dtype= 'str',
                                  delimiter = ',')
                                  
noaa_result = pywapi.get_weather_from_noaa('KPSM')
temp = noaa_result['temp_c']
wind_speed = noaa_result['wind_mph']
if wind_speed > 5:
    
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Latest Weather"
    
    body = "NOAA Portsmouth, NH: Temp={}C\n Wind{}mph\n".format(temp, wind_speed)
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, pswd)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()