import urllib.request

u = urllib.request.urlopen('http://www.ctabustracker.com/bustime/api/v2/getpredictions?key=gdC4QGkXRRyZwUbq4XHuSGth5&rt=22&stpid=14791')

from xml.etree.ElementTree import parse
doc = parse(u)


print("arrival time in minutes:")
for pt in doc.findall('.//prdctdn'):
    print(pt.text)

