#!/usr/bin/python
import csv
octet2 = raw_input("What is the second octet: ")
csvfile = 'dhcp.csv'
dhcp = csv.DictReader(open(csvfile, 'rb'), delimiter=',', quotechar='"')
for row in dhcp:
        print "# " + row['name']
        print "shared-network " + row['name'] + " {"
        print " subnet 10." + octet2 + "." + row['index'] + ".0 netmask 255.255.255.0 {"
        print "  range 10." + octet2 + "." + row['index'] + ".2 10." + octet2 + "." + row['index'] + ".254;"
        print "  authoritative;"
        print "  option routers 10." + octet2 + "." + row['index'] + ".1;"
        print "  option subnet-mask 255.255.255.0;"
        print "  option broadcast-address 10." + octet2 + "." + row['index'] + ".255;"
        print " }"
        print "}"
