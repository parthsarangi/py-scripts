# import os
import json


def read(path, name):
    file_open = open(path + name, 'r')
    lists = file_open.read()
    # lines = len(lists.readlines())
    file_open.close()
    # Get records in file
    # print("records in file : " + repr(lines))

    for list in lists:
        data = json.loads(list)
        print(data[0])


def read_json(path, name):
    file_open = open(path + name, 'r')
    lists = file_open.read()
    lines = len(lists.readlines())
    file_open.close()

    # Get records in file
    print("records iin file : " + repr(lines))

    rec = 1
    for list_rec in lists:
        data = json.loads(list_rec)
        print(data['occupation'])
        rec = rec + 1
        if rec > 1 :
            break
        # for k1 in data:
        #     print(k1)
    return 0


if __name__ == '__main__':
    print('>>>>> Started')

    # file_path = '/Users/parth/Documents/work/vn/'
    # json_file = 'customer_profile_20190101_1.json'

    file_path = "/Users/parth/Documents/work/mm-staging/eq/tables/schemas/"
    json_file = 'agent_agent_accreditation'

    ret = read(file_path, json_file)
    # print('Return Code : ' + repr(ret))

    print('>>>>> Ended')
