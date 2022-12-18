import csv
from django.conf import settings
from datetime import datetime


def read_data():
    project_list = []
    with open(settings.BASE_DIR / 'projects.csv', 'r') as file:
        reader = csv.reader(file)
        row_count = 0
        for row in reader:
            if row_count == 0:
                attributes = row
            else:
                data = {}
                for i in range(len(attributes)):
                    data[attributes[i]] = row[i]
                data['id'] = row_count

                locs = data['location_coordinates']
                data['location_coordinates'] = []

                while locs:
                    l = locs.find('(')
                    if l == -1:
                        break
                    r = locs.find(')')
                    coord = [float(x) for x in locs[l+1:r].split(', ')]
                    data['location_coordinates'].append(coord)
                    locs = locs[r+1:]

                data['project_start_time'] = datetime.strptime(data['project_start_time'], '%Y-%m-%d')
                data['project_completion_time'] = datetime.strptime(data['project_completion_time'], '%Y-%m-%d')
                data['completion_percentage'] = float(data['completion_percentage'][:-1])

                project_list.append(data)
            row_count += 1

    return project_list
