# This script checks the webpage for the existence of ecommerce functionality. 
# We had a Pimcore website that connected to a Magento API to introduce Ecommerce. 
# The API didn't always return the expected results (for various reasons) and wasn't always throwing the error in the application log, 
# So to track down the errors I ran this script to check which products were actually erroring so we could find the differences. 

from PyWebRunner import WebRunner
import csv
wr = WebRunner()
wr.start()
with open("2020_06_22_08_29_05am.csv") as f:
    count = 0
    urls = [row.split(',') for row in f]
    for url in urls:
        if count != 0:
            wr.go(url[0])
            wr.wait(3)
            if wr.is_text_on_page('Add to Cart'):
                continue
            else:
                print(url[1], url[2], url[3])
        count += 1
wr.stop()