# import os
# import json
import pandas as pd

def read_json(dir):
    # file1 = open(dir+'tr_order_20190704_000915_1.csv', 'r')
    file1 = pd.read_csv(dir + 'tr_order_20190704_000915_1.csv')
    if_valu = file1['order_id']=='19070323092898061140500'
    print(if_valu.head())


if __name__ == '__main__':
    path = '/Users/parth/Documents/work/vn/payment_tr_order/csv/0704/'
    read_json(path)