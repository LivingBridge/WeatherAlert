# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 18:23:44 2015

@author: ifh2
"""


from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import pywapi
import string
import smtplib

noaa_result = pywapi.get_weather_from_noaa('KPSM')
temp = noaa_result['temp_c']
wind_speed = noaa_result['wind_mph']

fromaddr = "unhcoreweather@gmail.com"
toaddr = "6036673978@vtext.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Latest Weather"
 
body = "NOAA Portsmouth, NH: Temp={}C\n Wind{}mph\n".format(temp, wind_speed)
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Wo$nik15")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()