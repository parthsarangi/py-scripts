import os
import json


def read_file(file_name):
    with open(file_name) as json_file:
        data = json.loads(json_file)
        for p in data:
            print('ID : ' + p['id'])
            # print('Website: ' + p['website'])
            # print('From: ' + p['from'])
            # print('')


def read_schema(schema_name):
    with open(schema_name) as json_file:
        data = json.load(json_file)
        for p in data:
            print('Name: ' + p['name'])


if __name__ == '__main__':
    print("Started")
    file_name = '/Users/parth/Documents/work/vn/customer_profile_20190101_1.json'
    read_file(file_name)
    schema_file = '/Users/parth/Documents/work/vn/customer_profile_20190101.schema'
    # read_schema(schema_file)
    print('Ended')
