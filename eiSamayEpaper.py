import urllib.request
from PyPDF2 import PdfFileMerger, PdfFileReader
import os
import shutil

ipDate = input("Please enter date in DDMMYYYY format: ")
noOfPages = input("Please enter the total number of pages: ")

home = os.path.expanduser("~")
folderPath = home + "\ePaper\eiSamay\\" + ipDate
pageImagePath = home + "\ePaper\eiSamay\\" + ipDate + "\\img\\"

directory = os.path.dirname(pageImagePath)
if not os.path.exists(directory):
    print("Inside mkdir. Creating directory: " + pageImagePath)
    os.makedirs(directory)

pageNumber = 1
print("Downloading pages from site...")
while (pageNumber <= int(noOfPages)):
    try:
        urllib.request.urlretrieve("https://www.epaper.eisamay.com/epaperimages/" + str(ipDate) + "/" 
        + str(ipDate) + "-md-em-" + str(pageNumber) + ".pdf", pageImagePath + "\page" + str(pageNumber) + ".pdf")
        print("Downloaded page" + str(pageNumber))
        pageNumber += 1
    except (urllib.error.HTTPError) as err:
        if err.code == 404:
            print("Page not found! Or the download might have completed")
        elif err.code == 403:
            print("Access denied!")
        else:
            print("Something happened! Error code - " + str(err.code))
        break
    except (urllib.error.URLError) as err:
        print("Some other error happened: Error code - " + str(err.code) + " Error reason - " + err.reason)
        break

print("Merging all PDFs into 1.....")
mergedObject = PdfFileMerger()
counter = 1

while (counter < pageNumber):
    mergedObject.append(PdfFileReader(pageImagePath + "\\page" + str(counter) + '.pdf', 'rb'))    
    counter += 1

mergedObject.write(folderPath + "\\eiSamay-" + str(ipDate) + ".pdf")

print("Merging done! Enjoy!!")

print("Removing junk....")
shutil.rmtree(pageImagePath)
print("Done!!")
