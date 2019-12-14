#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('guestlist.db')

c = conn.cursor()

c.execute('''CREATE TABLE guests (mac text PRIMARY KEY, ip text, lastactivity text, hostname text, supplied_hostname text, clientid text, lastupdate text, notes text)''')


