from urllib.request import urlopen
from bs4 import BeautifulSoup

import datetime
import time
import smtplib


while True:
    url="https://www.un.org/sc/suborg/en/sanctions/1267/press-releases"
    html= urlopen(url)
    soup= BeautifulSoup(html.read(), features='html.parser');
    info =soup.find('td', attrs={'class': 'views-field views-field-field-date-of-press-release'})
    if info == datetime.date.today:
        msg= 'Subject: Check UNSC press release page at : https://www.un.org/sc/suborg/en/sanctions/1267/press-releases!'
        fromaddr= 'your_email'
        toaddrs= 'your_email'

        server= smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email', 'your_password')
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        server.sendmail(fromaddr,toaddrs,msg)
        server.quit()
    else:
        time.sleep(1200)
        continue
