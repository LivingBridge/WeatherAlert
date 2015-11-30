# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:52:19 2015

@author: Localadmin
"""

from matplotlib import numpy as np
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import pywapi
import string
import smtplib
import time

#You must change PrivateData.txt to a txt file containing your private data.
#An example PrivateData.txt file is given in the repository and titled "PrivateDataEx.txt"
fromaddr,toaddr,pswd = np.genfromtxt('PrivateData.txt',
                                  dtype= 'str',
                                  delimiter = ',')
wind_threshold = 20
run = 1
wind = []
#if run == 1:#change to while to make an infinite loop for server
weather_com_result = pywapi.get_weather_from_weather_com('USNH0191') 
for i in range(len(weather_com_result['forecasts'])):
    wind.append(weather_com_result['forecasts'][i]['day']['wind']['speed'])
for i in range(len(wind)):
    if wind[i] > wind_threshold:   
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Latest Weather"
        body = "Weather.com Portsmouth, NH:\n Windspeed:{}km/h\n Days out:{}".format(str(wind[i]), str(i+1))
        print wind[i]
        print wind_threshold        
        print body
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, pswd)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        time.sleep(0)