import urllib.request
from fpdf import FPDF
import os
import shutil

ipDate = input("Please enter date in YYYYMMDD format: ")

home = os.path.expanduser("~")
folderPath = home + "\ePaper\EconomicTimes\\" + ipDate
pageImagePath = home + "\ePaper\EconomicTimes\\" + ipDate + "\\img\\"

directory = os.path.dirname(pageImagePath)
if not os.path.exists(directory):
    print("Inside mkdir. Creating directory: " + pageImagePath)
    os.makedirs(directory)

pageNumber = 1
print("Downloading pages from site...")
while (pageNumber <= 50):
    try:
        urllib.request.urlretrieve("https://epaperlive.timesofindia.com/Repository/ETE/PNQ/" + str(ipDate) + "/" + str(
            pageNumber) + "/big_page2.jpg", pageImagePath + "\page" + str(pageNumber) + ".jpg")
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

print("Converting to PDF.....")
pdf = FPDF(unit="pt", format=[2200, 3400])

counter = 1
while (counter < pageNumber):
    pdf.add_page()
    pdf.image(pageImagePath + "\\page" + str(counter) + ".jpg", 0, 0)
    counter += 1

pdf.output(folderPath + "\\Epaper.pdf", "F")
print("Convertion done! Enjoy!!")

print("Removing junk....")
shutil.rmtree(pageImagePath)
print("Done!!")
