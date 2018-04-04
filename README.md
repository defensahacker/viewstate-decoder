
## INTRO ##

VIEWSTATE module and decoder was copied from https://github.com/yuvadm/viewstate.git and all kudos go to yuvadm.

I just wrote a wrapper to easily decode ASP.NET ```__VIEWSTATE``` variables without having
to install the viewstate module into the system with administrative privileges and be able to decode the variables with a small script.

Sometimes when doing webpentesting against a ASP web application is useful a tool like this.

## USAGE ##

```
$ ./decoder.py "/wEPDwUKMTU5MTA2ODYwOWRkoCvvBWgUOH7PD446qvEOF6GTCq0="
** ASP.NET __VIEWSTATE decoder **

[*] Decoding __VIEWSTATE:
/wEPDwUKMTU5MTA2ODYwOWRkoCvvBWgUOH7PD446qvEOF6GTCq0=
(('1591068609', None), None)
```


## DISCLAIMER ##
Use at your own risk in an environment that you are allowed to attack.


~
(c) spinfoo

