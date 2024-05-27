localconf = 'zone "mon.lan" {\n type master; \nfile "/etc/bind/db.mon.lan";\n};'
monlan = '$TTL 3h\n@ IN SOA ns.mon.lan. mailaddress.mon.lan. (\n2021051701\n6H\n1H\n5D\n1D )\n@ IN NS ns.mon.lan.\n@ IN MX 10 mail.mon.lan.\nns A 10.200.XX.1\nserveur A 10.200.XX.1\nclient A 10.200.XX. ?\nrouteurXX A 10.200.XX.254\ncommutXX A 10.200.XX.253'

f = open("/etc/bind/named.conf.local", "w")
f.write(localconf)
f.close()


f = open("/etc/bind/db.mon.lan", "w")
f.write(monlan)
f.close()

