#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()
import cgi

print "Content-type:text/html\r\n\r\n"
form = cgi.FieldStorage()
variable = ""
value = ""
r = ""
for key in form.keys():
        variable = str(key)
        value = str(form.getvalue(variable))
        r += variable +": "+ value + "\n"

fields = str(r) 
print (fields)