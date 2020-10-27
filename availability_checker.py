#!/usr/bin/env python3

import json
import requests
import smtplib

def check_calendar():
    url = 'https://calendly.com/api/booking/event_types/BFEN3HYGXBSSUYOC/calendar/range?timezone=America%2FNew_York&diagnostics=false&range_start=2020-09-09&range_end=2020-12-29&single_use_link_uuid=&embed_domain=projectcupid.cityofnewyork.us&embed_type=Inline'
    r = requests.get(url)
    json_data = json.loads(r.text)
    days = json_data['days']
    
    found_date = False 
    for date in days:
        if date['status'] != 'unavailable':
            found_date = True
            send_email(date['date'], date['spots'])
            break
            
    if not found_date:
        send_email('nothing available', 'checkback tomorrow')

def send_email(date, spots):
    sender = '' # ADD GMAIL ACCOUNT HERE
    sender_password = '' # ADD GMAIL PASSWORD HERE
    to = ''#ADD EMAIL HERE
    body = f'get married on {date} {spots}'
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, sender_password)
        server.sendmail(sender, to, body)
    except:
        print('something went wrong')


def main():
    check_calendar()


if __name__ == '__main__':
    main()
