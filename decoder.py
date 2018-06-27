#!/usr/bin/python3

# Small tool to decode ASP.NET __VIEWSTATE variable
#
# VIEWSTATE module from https://github.com/yuvadm/viewstate.git
#
# spinfoo

import viewstate
import exceptions
import sys
import colors as c

#
# @TODO: Pass URL, parse content and print __VIEWSTATE decoded!
#
## Valid format: "/wEPDwU[a-zA-Z0-9=]+"

c.print_red("** ASP.NET __VIEWSTATE decoder **\n")

if len(sys.argv) != 2:
    print("Usage: decoder.py \"<__VIEWSTATE ASP.NET string>\"")
    print("Example: decoder.py \"/wEPDwUKMTU5MTA2ODYwOWRkoCvvBWgUOH7PD446qvEOF6GTCq0=\"")
    sys.exit()

vst= sys.argv[1]

c.print_blue("[*] Decoding __VIEWSTATE:")
print(vst)
try:
    vs= viewstate.ViewState(vst)
    c.print_green(str(vs.decode()))
except exceptions.ViewStateException as e:
    print (e)
except IndexError as e:
    print (e)
