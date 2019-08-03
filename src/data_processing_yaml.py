import yaml
from os import listdir

def read_file(path, file):
    file_yml = open(path + file, 'r')
    data = yaml.load(file_yml, Loader=yaml.FullLoader)
    for k1, v1 in data.items:
        if  in line
        print()


if __name__ == '__main__':
    path = '/Users/parth/Documents/bitbuckets/acm-dp-data-processing/profiles/acm-eq-qa'
    file_names = listdir(path)

    for file in file_names:
        read_file(path, file)