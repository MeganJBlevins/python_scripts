import json
import csv
with open('LansaFeed.json') as f:
  data = json.loads(f.read())
  products = data['products']
with open('LansaNoImages.csv', 'w', newline='') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  spamwriter.writerow(['GTIN'] + ['Name'])
  for product in products:
    if not product['NM_ImageUrls']:
      spamwriter.writerow([product['GTIN']] + [product['X_Name']])
