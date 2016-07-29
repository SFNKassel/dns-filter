install:
	echo "$(awk 'NR==1{print; print "include \"/etc/bind/blacklisted.zones\";"} NR!=1' /etc/univention/templates/files/etc/bind/named.conf.samba4)" > /etc/univention/templates/files/etc/bind/named.conf.samba4
	univention-config-registry commit /etc/bind/named.conf.samba4
	python3 merge.py
	python3 gen_dns_zones.py
	cp blockeddomains.db /etc/bind
	cp blacklisted.zones /etc/bind
