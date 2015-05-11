#!/usr/bin/python
import csv
octet2 = raw_input("What is the second octet: ")
csvfile = 'dhcp.csv'
dhcp = csv.DictReader(open(csvfile, 'rb'), delimiter=',', quotechar='"')
f = open('dhcpoutput.txt','w')
for row in dhcp:
        f.write("# %s\n" % row['name'])
        f.write("shared-network %s {\n" % row['name'])
        f.write(" subnet 10.%s.%s.0 netmask 255.255.255.0 {\n" % (octet2, row['index']))
        f.write("  range 10.%s.%s.2 10.%s.%s.245;\n" % (octet2, row['index'], octet2, row['index']))
        f.write("  authoritative;\n")
        f.write("  option routers 10.%s.%s.1;\n" % (octet2, row['index']))
        f.write("  option subnet-mask 255.255.255.0;\n")
        f.write("  option broadcast-address 10.%s.%s.255;\n" % (octet2, row['index']))
        f.write(" }\n")
        f.write("}\n")
f.close()