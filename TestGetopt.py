import sys, argparse

searchString = ""
startDate = ''
endDate = ''

parser = argparse.ArgumentParser()
parser.add_argument("searchString", help="String to search")
parser.add_argument("-s", "--startDate", help="Start Date")
parser.add_argument("-e", "--endDate", help="End Date")
args = parser.parse_args()

searchString = args.searchString

if args.startDate is not None:
	startDate = args.startDate

if args.endDate is not None:
	endDate = args.endDate
	
print ("Search String - "+searchString)
print ("Start Date - "+startDate)
print ("End Date - "+endDate)