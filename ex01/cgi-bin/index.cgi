#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()

print "Content-type:text/html\r\n\r\n"

import phpinfo

print (phpinfo.pyinfo())