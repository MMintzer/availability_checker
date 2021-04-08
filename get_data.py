#!/usr/bin/env python3

import json
import requests
import smtplib

headers = {'Referer': 'https://www.cvs.com/immunizations/covid-19-vaccine'}

r = requests.get('https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.NY.json?vaccineinfo', headers=headers)
    #print(r.text)
dict_data = json.loads(r.text)
locations = dict_data['responsePayloadData']['data']['NY']

for pharmacy in locations:
     if pharmacy['city'] == 'LONG BEACH':
        if pharmacy['status'] != 'Fully Booked':
            #TODO: SEND ME A TEXT MESSAGE
            print(pharmacy)
            print('send a text message')
            send_email()
        else:
            print(pharmacy)
            print('not available right now')



def send_email():
    sender = '' # ADD GMAIL ACCOUNT HERE
    sender_password = '' # ADD GMAIL PASSWORD HERE
    to = ''#ADD EMAIL HERE
    body = 'AVAILABILITY TO GET COVID VACCINE'
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, sender_password)
        server.sendmail(sender, to, body)
    except:
        print('something went wrong')