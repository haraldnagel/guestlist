#!/usr/bin/python3

from datetime import datetime
import os
import sqlite3
import sys

if(len(sys.argv) < 4):
    print("not enough arguments!")
    sys.exit()

action = sys.argv[1]
mac = sys.argv[2]
ip = sys.argv[3]
hostname = ''
if(len(sys.argv) > 4):
    hostname = sys.argv[4]

print("action %s for ip %s (mac %s), hostname %s" % (action, ip, mac, hostname))

suppliedHostname = os.getenv('DNSMASQ_SUPPLIED_HOSTNAME', '')
clientId = os.getenv('DNSMASQ_CLIENT_ID', '')

conn = sqlite3.connect('/guestlist/guestlist.db')

c = conn.cursor()

cur = conn.cursor()
cur.execute('SELECT COUNT(mac) FROM guests WHERE mac = ?', (mac,))
data = cur.fetchone()
print("Data is %d" % data[0])
if(data[0] == 0):
    print('Performing insert...')
    c.execute('INSERT INTO guests VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (mac, ip, action, hostname, suppliedHostname, clientId, datetime.now(), ''))
else:
    print('Performing update...')
    c.execute('UPDATE guests SET ip = ?, hostname = ?, supplied_hostname = ?, clientid = ?, lastupdate = ? WHERE mac = ?', (ip, hostname, suppliedHostname, clientId, datetime.now(), mac))

conn.commit()

#c.execute('''CREATE TABLE guests (lastactivity text, mac text, ip text, hostname text, supplied_hostname text, clientid text, timestamp text, notes text)''')
