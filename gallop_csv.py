#   ________       .__  .__                 _________            .__        __
#  /  _____/_____  |  | |  |   ____ ______ /   _____/ ___________|__|______/  |_  ______
# /   \  ___\__  \ |  | |  |  /  _ \\____ \\_____  \_/ ___\_  __ \  \____ \   __\/  ___/
# \    \_\  \/ __ \|  |_|  |_(  <_> )  |_> >        \  \___|  | \/  |  |_> >  |  \___ \
#  \______  (____  /____/____/\____/|   __/_______  /\___  >__|  |__|   __/|__| /____  >
#         \/     \/                 |__|          \/     \/         |__|             \/
# -- Gallop CSV
# - Andy Fang


import csv
from collections import defaultdict


class Data:

    column = defaultdict(list)  # each value in each column is appended to a list

    def __init__(self, file):

        self.data = open(file)

        with self.data as f:
            reader = csv.DictReader(f)  # read rows into a dictionary format
            for row in reader: # read a row as {column1: value1, column2: value2,...}
                for (k, v) in row.items():  # go over each column name and value
                    self.column[k].append(v)  # append the value into the appropriate list based on column number k

        self.campaign_name = self.column['Campaign Name']
        self.start_date = self.column['Start Date']
        self.end_date = self.column['End Date']
        self.reach = self.column['Reach']
        self.action = self.column['Actions']


    def occurences(self, s, ch):
        """
        Gets all the occurences of a string in a string.
        :param s: The string to look in.
        :param ch: The string to find.
        :return: A list of all indexes of occurence (ch) in s.
        """
        return [i for i, letter in enumerate(s) if letter == ch]

    def device(self, device):
        """
        Returns a list of all the values needed to organize Gallop data.
        :param device: this is the case insensitive name of the device to search for. All other returned values are in the
        same
        row as
        the device.
        :return: List of companies, campaigners, audiences, impressions
        """

        i = 0
        self.rows = []
        self.companies = []
        self.campaigners = []
        self.audiences = []
        self.impressions = 0
        self.total_dl = 0
        self.spent = 0
        self.placement = []
        self.actions = 0
        self.starts = []
        self.start_dates = []

        for row in self.campaign_name:
            audience = row[self.occurences(row, '-')[1]:self.occurences(row, '-')[2]].strip(' -') # filters by

            if 'IPAD' not in row[self.occurences(row, '-')[2]:].strip('- ') and 'IPHONE' not in row[self.occurences(
                    row, '-')[2]:].strip('- ') and 'ANDROID' not in row[self.occurences(row, '-')[2]:].strip('- '):
                self.placement.append(row[self.occurences(row, '-')[2]:].strip('- '))

            i += 1
            if audience.lower() == device.lower():
                company = row[:self.occurences(row, '-')[0]].strip()
                campaigner = row[self.occurences(row, '-')[0]:self.occurences(row, '-')[1]].strip(' -')

                self.impressions += float(self.column['Impressions'][i - 1])
                # total_dl += int(column['Total Downloads'])
                self.spent += float(self.column['Amount Spent (USD)'][i - 1])

                self.companies.append(company)
                self.campaigners.append(campaigner)
                self.audiences.append(audience)


                # self.actions.append(self.action[i])
                self.actions += int(self.action[i - 1])
                self.start_dates.append(self.start_date[i - 1])


        # Number of rows in column for debugging
        # print('Actions: ' + str(len(self.action)))
        # print('Reach: ' + str(len(self.reach)))
        # print('Start Date: ' + str(len(self.start_date)))
        #
        # print('Companies: ' + str(len(self.companies)))
        # print('Campaigner: ' + str(len(self.campaigners)))
        # print('Audiences: ' + str(len(self.audiences)))

        self.cpi = int(self.spent / self.actions)
        self.starts = int(len(set(self.start_dates)))
        self.cps = int(self.spent / self.starts)
        self.dltostart = int(self.spent / self.actions)


        def get_impressions():
            pass

        tuple = self.companies, self.campaigners, self.audiences, "{0:.2f}".format(self.impressions), \
                "{0:.2f}".format(self.spent), self.actions, self.cpi, self.starts, self.cps, self.dltostart

        return list(tuple)


if __name__ == "__main__":

    nyt = Data('gdata.csv')
    device = 'IPHONE'

    impressions = nyt.device(device)[3]
    spend = nyt.device(device)[4]
    actions = nyt.device(device)[5]
    cpi = nyt.device(device)[6]
    starts = nyt.device(device)[7]
    cps = nyt.device(device)[8]
    dltostart = nyt.device(device)[9]


    print(actions)
    print(impressions)
    print(spend)
    print(actions)
    print(cpi)
    print(starts)
    print(cps)
    print(dltostart)