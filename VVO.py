#!/usr/bin/python
import httplib
import json

con = httplib.HTTPConnection("widgets.vvo-online.de")
con.request("GET", "/abfahrtsmonitor/Abfahrten.do?ort=Dresden&hst=Hp%20Dobritz")
res = con.getresponse()
data = json.loads(res.read())
# data [0][0] Linie
# data [0][1] Richtung
# data [0][2] Abfahrt in Minuten
print data[0][1]
