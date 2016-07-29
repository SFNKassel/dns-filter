import os

i = open("list")
o = open("blacklisted.zones", "w")

for a in i:
		if len(a.split("/")) > 1:
			continue
		if len(a.split("/")[0].split(".")) == 1: 
			continue
		if a.split("/")[0].strip() == ".tumblr.com":
			print(a)
		devNull = o.write("zone \"" + a.split("/")[0].strip() + "\" {type master; file \"/etc/bind/blockeddomains.db\";};\n")
i.close()
o.close()

os.system("echo \"$(sort -f blacklisted.zones | uniq -i)\" > blacklisted.zones")

