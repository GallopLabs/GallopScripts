''''
  ________       .__  .__                 _________            .__        __
 /  _____/_____  |  | |  |   ____ ______ /   _____/ ___________|__|______/  |_  ______
/   \  ___\__  \ |  | |  |  /  _ \\____ \\_____  \_/ ___\_  __ \  \____ \   __\/  ___/
\    \_\  \/ __ \|  |_|  |_(  <_> )  |_> >        \  \___|  | \/  |  |_> >  |  \___ \
 \______  (____  /____/____/\____/|   __/_______  /\___  >__|  |__|   __/|__| /____  >
        \/     \/                 |__|          \/     \/         |__|             \/
-- Gallop CSV
- Andy Fang
'''

import csv
from collections import defaultdict

data = open('gdata.csv')
column = defaultdict(list) # each value in each column is appended to a list

with data as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value
            column[k].append(v) # append the value into the appropriate list
                                 # based on column name k


campaign_name = column['Campaign Name']
impressions = column['Impressions']

def occurances(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def parse(device):
    """
    Returns a list of all the values needed to organize Gallop data.
    :param device: this is the name of the device to search for. All other returned values are in the same row as
    the device.
    :return: List of companies, campaigners, audiences, impressions
    """
    rows = []
    i = 0

    companies = []
    campaigners = []
    audiences = []
    impressions = 0
    total_dl = 0
    spent = 0

    for row in campaign_name:
        audience = row[occurances(row, '-')[1]:occurances(row, '-')[2]].strip(' -') # filters by audience
        i += 1 # Index of the matching row to audience

        if audience.lower() == device.lower():
            company = row[:occurances(row, '-')[0]].strip()
            campaigner = row[occurances(row, '-')[0]:occurances(row, '-')[1]].strip(' -')
            impressions += float(column['Impressions'][i - 1])
            # total_dl += int(column['Total Downloads'])
            spent += float(column['Amount Spent (USD)'][i - 1])



            companies.append(company)
            campaigners.append(campaigner)
            audiences.append(audience)





    tuple = companies, campaigners, audiences, "{0:.2f}".format(impressions), "{0:.2f}".format(spent)

    return list(tuple)

print(parse('IPHONE'))

help(parse)