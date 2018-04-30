import csv
import os
import re
import requests

with open('nypd-discipline.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    for line in reader:
        match = re.search('[0-9].*?\.', line['URL'])
        filename = '../text/' +  line['URL'][match.start():match.end()] + 'txt'
        if os.path.exists(filename):
            continue
        line['URL'] = re.sub('www.documentcloud', 'assets.documentcloud', line['URL'])
        line['URL'] = re.sub('.html', '.txt', line['URL'])
        line['URL'] = re.sub('-nypd', '/nypd', line['URL'])
        print line['URL']
        r = requests.get(line['URL'])
        text_file = open(filename, 'w')
        text_file.write(r.text)
        text_file.close()
