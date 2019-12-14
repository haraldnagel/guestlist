#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('guestlist.db')

c = conn.cursor()

guests = c.execute("SELECT * FROM guests")

for guest in guests:
        print(guest)

conn.commit()
