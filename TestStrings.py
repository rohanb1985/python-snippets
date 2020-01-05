import re

stream = "//ABC/1234_XYZ123_Dr2_2/opt//ABC/com/bb/src/impl/main/java/junk/rohan/ABCD.java"

splitted = stream.split("/")
partitioned = stream.partition("/")
depotHead = "//ABC/"
regExp1 = re.search(r'%s([^/]+)' % depotHead, stream)
regExp2 = re.match(r'%s([^/]+)' % depotHead, stream)

print (regExp1)
print (regExp2)
print (splitted)
print (partitioned)
