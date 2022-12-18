import csv
from django.conf import settings


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

                project_list.append(data)
            row_count += 1

    return project_list
