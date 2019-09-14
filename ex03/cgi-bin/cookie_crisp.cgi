#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()
import cgi
import os
import Cookie

form = cgi.FieldStorage()
variable = ""
value = ""
array = {}

for key in form.keys():
    variable = str(key)
    value = str(form.getvalue(variable))
    array[variable] = value

if (array['action'] == 'set'):
    cookie = Cookie.SimpleCookie()
    cookie[array['name']] = array['value']
    cookie[array['name']]['expires'] = 1*1*3*60*60*40    
    print cookie



if (array['action'] == 'get'):
    print "Content-type: text/html\r\n"
    try:
        cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
        print cookie[array['name']].value
    except:
        print ("cookie is not set")




if (array['action'] == 'del'):
    try:
        cookie = Cookie.SimpleCookie()
        cookie[array['name']] = ''
        cookie[array['name']]['expires']='Thu, 01 Jan 1970 00:00:00 GMT'
        print cookie
    except:
        print "Content-type: text/html\r\n"
        print ("Cookie doesnt")

print ""