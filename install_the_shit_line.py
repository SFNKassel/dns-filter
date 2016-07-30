#!/usr/bin/env python3

THE_FILE = "/etc/univention/templates/files/etc/bind/named.conf.samba4"

infile = open(THE_FILE)

text = ""

text += infile.readline()
text += "include \"/etc/bind/blacklisted.zones\";"

for l in infile:
	text += l	

infile.close()

outfile = open(THE_FILE, "w")
outfile.write(text)
outfile.close()
