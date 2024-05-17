
dhcp_serveur = 'INTERFACESv4="eth3"'
dhcp_conf = 'default-lease-time 600;\nmax-lease-time 7200;\noption subnet-mask '+str(input('masque : '))+';\noption routers '+str(input('routeur par default attribue : '))+';\noption domain-name-servers '+str(input('DNS attribue : '))+';\nsubnet '+str(input('reseau : '))+' netmask '+str(input('masque : '))+' {\n range '+str(input('range (x.x.x.x x.x.x.x)'))+'; \n}'

f = open("/etc/default/isc-dhcp-server", "w")
f.write(dhcp_serveur)
f.close()


f = open("/etc/dhcp/dhcpd.conf", "w")
f.write(dhcp_conf)
f.close()
