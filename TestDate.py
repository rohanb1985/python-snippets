import datetime

print ("Date: "  +str(datetime.datetime.today()))
print (datetime.datetime.today())
oldDate = datetime.datetime.today() - datetime.timedelta(6*365/12)
print (oldDate)
print (oldDate.strftime("%Y/%m/%d"))