import csv
import os
import re

with open('../csv/nypd-discipline.csv', 'r') as infile:
    with open('../csv/nypd-discipline-v2.csv', 'w') as outfile:

        # prep relevant objects for I/O
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile,
            fieldnames = reader.fieldnames + ['date1', 'date2'])
        filename = ''

        # pre-compile regexes (faster later)

        # for dates:
        # this regex only matches on mm/dd/yyyy, the format
        # that the docs use. some OCR gives, e.g., mm/dd/yy (erroneous)
        # we'll want to manually fix those anyway, so don't match
        reg_date = re.compile('[0-9]{2}\/[0-9]{2}\/[0-9]{4}')

        # for unique portion (identifier) of URLs
        reg_url = re.compile('[0-9].*?\.')

        for line in reader:

            match = re.search(reg_url, line['URL'])
            # we want to keep files open as long as we're still using them
            # this is how we named the .txt files earler, so look for them
            tmp = '../text/' +  line['URL'][match.start():match.end()] + 'txt'
            # if new file: open, get text, then dates
            if tmp != filename:
                filename = tmp
                if not os.path.exists(filename):
                    print "haven't managed to pull that .txt yet!"
                    continue
                inf = open(filename, 'r')
                text = inf.read()
                matches = re.findall(reg_date, text)
                match_number = 0
                print matches # debug / inspect

            # running into problems with missing dates and how to handle
            # (figure out WHICH are missing). we could do a lot of contingent
            # handlers (eg. does it follow cert. text)?
            # but basically we'll need to manually correct the OCR so it's
            # probably enough to just flag which .txts are not fully filled

            try:
                line['date1'] = matches[match_number]
                line['date2'] = matches[match_number + 1]
                match_number += 2
                writer.writerow(line)
            except:
                line['date1'] = "MISSING DATE IN TXT"
                writer.writerow(line)



