
## INTRO ##

VIEWSTATE module and decoder was copied from https://github.com/yuvadm/viewstate.git and all kudos go to yuvadm.

I just wrote a small tool to easily decode ASP.NET ```__VIEWSTATE``` variables without having
to install the viewstate module into the system with administrative privileges and be able to decode the variables with a small script using a terminal, without writting python code.

Sometimes when doing webpentesting against a ASP web application is useful a tool like this.

## USAGE ##

```
$ ./decoder.py "/wEPDwUKMTU5MTA2ODYwOWRkoCvvBWgUOH7PD446qvEOF6GTCq0="
** ASP.NET __VIEWSTATE decoder **

[*] Decoding __VIEWSTATE:
/wEPDwUKMTU5MTA2ODYwOWRkoCvvBWgUOH7PD446qvEOF6GTCq0=
(('1591068609', None), None)
```

## DEFENSE ##

To protect against this attacks turn ```EnableViewStateMac``` property to ```True``` in the ```machine.config``` file.
To encrypt turn property ```validation``` to ```3DES```.


## DISCLAIMER ##
Use at your own risk in an environment that you are allowed to attack.


~
(c) defensahacker

