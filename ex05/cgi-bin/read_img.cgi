#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
cgitb.enable()
import cgi

print "Content-type:text/html\r\n\r\n"

with open("./img/42.png") as f:
    data_uri = f.read().encode('base64').replace('\n', '')
    img_tag = '<img src="data:image/jpeg;base64,{0}" alt="" />'.format(data_uri)
    print (img_tag)