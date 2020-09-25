import csv
with open('international_unit_page_url.csv') as unit_url_csv:
    readCSV = csv.reader(unit_url_csv)


    for row in readCSV:

        print(row[0][41:51])