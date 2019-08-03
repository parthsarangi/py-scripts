
def compare():
    path='/Users/parth/Documents/work/vn/payment_tr_order/missing/'
    file1=open(path+'agent_transaction_2706.csv','r')
    file2=open(path+'results-20190711-175414.csv','r')
    for row in file2:
        for id in file1:
            if row != id:
                print('Not found : '+id)
                break


compare()
