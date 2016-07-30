install:
	./install_the_shit_line.py	
	univention-config-registry commit /etc/bind/named.conf.samba4
	python3 merge.py
	python3 gen_dns_zones.py
	cp blockeddomains.db /etc/bind
	cp blacklisted.zones /etc/bind
	service univention-bind restart
