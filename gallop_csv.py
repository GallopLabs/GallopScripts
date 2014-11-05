''''
  ________       .__  .__                 _________            .__        __
 /  _____/_____  |  | |  |   ____ ______ /   _____/ ___________|__|______/  |_  ______
/   \  ___\__  \ |  | |  |  /  _ \\____ \\_____  \_/ ___\_  __ \  \____ \   __\/  ___/
\    \_\  \/ __ \|  |_|  |_(  <_> )  |_> >        \  \___|  | \/  |  |_> >  |  \___ \
 \______  (____  /____/____/\____/|   __/_______  /\___  >__|  |__|   __/|__| /____  >
        \/     \/                 |__|          \/     \/         |__|             \/
-- CSV Prettify
- Andy Fang
'''

import csv

# with open('data.csv') as f:
#     reader = csv.reader(f)
#     data = [row[0] for row in reader]
#
# print(data[0])

data = csv.reader(open('data.csv', 'rt'), delimiter=' ')

row = []
for rows in data:
    row.append(rows)

print(row[1])