from os import listdir
import pandas as pd

# Compare list of id's from missing list to csv files in folder

def read_csv():
    # Output file to write the id's Found
    outfile=open('/Users/parth/Documents/work/vn/payment_order_balance_movement/missing/list_found_0704.txt', 'w')

    # list of missing id's are kept here
    missing = pd.read_csv('/Users/parth/Documents/work/vn/payment_tr_order/missing/agent_transaction_0407.csv')
    missing1 = missing["order_id"].to_list()

    # CSV files to search are kept here
    folder='/Users/parth/Documents/work/vn/payment_order_balance_movement/csv/0704/'
    filenames = listdir(folder)
    n=0
    oldFile = ""
    df = []
    for file in filenames:
        if file.endswith('.csv'):
            print(">>>>  Reading file " + file)
            df_read = pd.read_csv(folder+file)
            df.append(df_read)
            order=df['order_balance_movement_id'].to_list()
            for val in missing1:
                print("Checking value : "+val)
                for row in order:
                    # print(row)
                    if val == row:
                        # print("Found value : "+row)
                        outfile.write('Found : '+row+' in file '+file+'\n')
                        if olfFile != file:
                            print('File name is : '+oldFile)
                            oldFile=file

                        n=n+1
                        break

    print("Found ids : ",n)
    outfile.close()


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
read_csv()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

#end
