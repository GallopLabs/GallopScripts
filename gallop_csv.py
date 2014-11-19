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


class Data:

    def __init__(self, file):

        data = open(file)
        column = defaultdict(list) # each value in each column is appended to a list

        with data as f:
            reader = csv.DictReader(f) # read rows into a dictionary format
            for row in reader: # read a row as {column1: value1, column2: value2,...}
                for (k, v) in row.items(): # go over each column name and value
                    column[k].append(v) # append the value into the appropriate list
                                         # based on column name k

        self.campaign_name = column['Campaign Name']
        self.start_date = column['Start Date']
        self.end_date = column['End Date']
        self.reach = column['Reach']

    def occurences(s, ch):
        """
        Gets all the occurences of a string in a string.
        :param s: The string to look in.
        :param ch: The string to find.
        :return: A list of all indexes of occurence (ch) in s.
        """
        return [i for i, letter in enumerate(s) if letter == ch]


class Device:

    def __init__(self, data, device):
            """
            Returns a list of all the values needed to organize Gallop data.
            :param device: this is the case insensitive name of the device to search for. All other returned values are in the
            same
            row as
            the device.
            :return: List of companies, campaigners, audiences, impressions
            """


            self.rows = []
            i = 0
            self.companies = []
            self.campaigners = []
            self.audiences = []
            self.impressions = 0
            self.total_dl = 0
            self.spent = 0

            for row in data.campaign_name:
                audience = row[data.occurences(row, '-')[1]:data.occurences(row, '-')[2]].strip(' -') # filters by
                # audience
                i += 1 # Index of the matching row to audience

                if audience.lower() == device.lower():
                    company = row[:data.occurences(row, '-')[0]].strip()
                    campaigner = row[data.occurences(row, '-')[0]:data.occurences(row, '-')[1]].strip(' -')
                    self.impressions += float(data.column['Impressions'][i - 1])
                    # total_dl += int(column['Total Downloads'])
                    self.spent += float(data.column['Amount Spent (USD)'][i - 1])

                    self.companies.append(company)
                    self.campaigners.append(campaigner)
                    self.audiences.append(audience)

            tuple = self.companies, self.campaigners, self.audiences, "{0:.2f}".format(self.impressions), "{0:.2f}".format(self.spent)

            return list(tuple)


if __name__ == 'main':

    nyt = Data('gdata.csv')
    Iphone = Device(nyt, 'IPHONE')

    print(Iphone)