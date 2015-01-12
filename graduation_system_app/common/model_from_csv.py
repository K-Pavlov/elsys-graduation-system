import unicodecsv as csv
import codecs

def save_csvfile(csvfile):
    with open('some/file/generateMeAName.csv', 'wb+') as destination:
        for chunk in csvfile.chunks():
            destination.write(chunk)