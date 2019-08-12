import os
import json


def readfile(path):
    files = []
    sql = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if "file" in file:
                files.append(file)
            if "sql" in file:
                sql.append(file)

    counter = 1
    for file in files:
        folder = file.replace("file_", "")
        print(repr(counter) + " : " + folder)

        dest = '/Users/parth/Documents/bitbuckets/acn-dp-mart-transformation/profile/acm-mm-staging/'

        try:
            os.mkdir(dest + folder)
        except:
            print("Folder exists")

        dict = getdict(path + "/" + file, dest + file)

        outfile = open(dest + folder + "/config.ini", 'w')
        pre_write(outfile, folder)

        for lines in dict:
            outfile.write("\t" + lines["name"] + ":" + lines["type"] + "," + "\n")
            # print(lines["name"] + ":" + lines["type"] + ",")
        counter = counter + 1

        post_write(outfile, folder)
        get_sql(outfile, path, sql)

        outfile.close()


def pre_write(op, tab):
       op.write("[profile]" + "\n")
       op.write("#mode = append | truncate" + "\n")
       op.write("mode=truncate" + "\n\n")
       op.write("# sql type" + "\n")
       op.write("use_legacy_sql=false" + "\n\n")
       op.write("# project_id:database.table_name" + "\n")
       op.write("table=acm-mm-staging:source_eq_test." + tab + "\n")
       op.write("partition_enable = true" + "\n")
       op.write("partition_field = DATE_KEY" + "\n\n")
       op.write("schema=")


def post_write(op, tab):
    op.write("\n\n" + "# sql to create mart" + "\n")
    op.write("query =")


# Read the SQL of the mart view from folder
def get_sql(op, path, files):
    for file in files:
        f = open(path + "/" + file, 'r')
        for records in f:
            if " Query " not in records:
                if "---------" not in records:
                    if "Table acm-mm-staging" not in records:
                        op.write(records)


def getdict(f, p):
    file = open(f, "r")
    dict = json.load(file)
    file.close()
    return dict


if __name__ == '__main__':
    print("Started")
    path = "/Users/parth/Documents/work/mm-staging/eq/marts"
    readfile(path)
    print("Ended")
