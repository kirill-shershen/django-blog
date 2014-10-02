# -*- coding: cp1251 -*-
#!/bin/env python
#__author__ = 'kxekxe'

import sys
from time import localtime, strftime
import urllib
import xml.dom.minidom

sURL="http://www.cbr.ru/scripts/XML_daily.asp?date_req="

def GetCurrentCurrency():
    vDate = strftime("%d.%m.%Y", localtime())
    u=urllib.urlopen(sURL+vDate)
    xmltext = u.read()
    xmldoc = xml.dom.minidom.parseString(xmltext)
    root = xmldoc.documentElement
    for valute in root.childNodes:
        if valute.nodeName == '#text':
            continue
        if valute.attributes['ID'].value == 'R01235':
            for ch in valute.childNodes:
                if ch.nodeName == '#text':
                    continue
                if ch.nodeName == u'Value':
                    return ch.childNodes[0].nodeValue
                    exit
def main():
    print u'Курс доллара - %s' % GetCurrentCurrency()

if __name__ == '__main__' :
    sys.exit( main() )