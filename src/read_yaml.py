import yaml


def read_yaml(job_type, y, output_files, search_key):
    etl_jobs_list = []
    bq_jobs_list = []
    opfile = output_files["all"]
    # opfile_etl = output_files["etl"]
    opfile_bq = output_files["bq"]

    for k1, v1 in y.items():
        if k1 == 'jobs':
            print(">> Found jobs")
            for items in v1:
                for k2, v2 in items.items():
                    print("Found " + k2)
                    if k2 == search_key:
                        print(">>> found search_key " + search_key)
                        opfile.write('>> Job type %s\n' % k2)
                        s = 0
                        for item1 in v2:
                            for k3, v3 in item1.items():
                                s = s + 1
                                opfile.write('Serial: %s\n' % s)
                                opfile.write('Job-name: %s\n' % k3)
                                for k4, v4 in v3.items():
                                    if k4 == "profile":
                                        opfile.write('Config-name: %s\n' % v4)
                                        print(v4)
                                        pos_slash = v4.index("/") + 1
                                        file = v4[pos_slash:len(v4)]
                                        var_dict = fetch_config(file, opfile)
                                    if k4 == "dataSourceUrl":
                                        question_pos = v4.index("_qa?")  # take the correct region name from jobs.yaml file
                                        port_pos = v4.index(":3306/") + 6
                                        db_name = v4[port_pos:question_pos]
                                        opfile.write('Db-name: %s\n' % db_name)
                                        opfile.write('Table-name : %s\n' % var_dict["tab_name"])
                                        load_to_BQ_job_name = db_name + "_" + var_dict["tab_name"]
                                        opfile.write('Load-to-bq-Job-name: %s\n' % load_to_BQ_job_name)
                                        opfile.write('Where-condition : %s\n' % var_dict['where_condition'])
                                        etl_jobs_list.append(k3)
                                        bq_jobs_list.append(load_to_BQ_job_name)
                                        opfile_bq.write('\n%s, %s, %s, %s, %s' % (job_type, db_name, var_dict["tab_name"], load_to_BQ_job_name, k3 ))
    # write_to_file(etl_jobs_list, opfile_etl)
    # write_to_file(bq_jobs_list, opfile_bq)


# def write_to_file(list, outfile):
#     for items in list:
#         outfie.write('%s' % list)



def fetch_config(file, opfile):
    config_path = "/Users/parth/Documents/bitbuckets/acm-dp-eq-etl-config/ETL/config/acm-eq/"
    # file = "rule_action/"
    # file = ""
    config_file = open(config_path + file + "/config.properties", 'r')
    # load_to_bq = ''
    for line in config_file:
        if "etl.output.storage" in line:
            eol = len(line) - 1
            string_storage = line[1:eol]
        if "where=" in line:
            eol = len(line) - 1
            string_where = line[1:eol]
        if "etl.input.schema" in line:
            pos = line.index("=")
            eol = len(line) - 1
            string_tab = line[pos+1:eol]
    config_file.close()
    var_dict = {'storage_path': string_storage, 'where_condition': string_where, 'tab_name': string_tab}
    return var_dict


def write_opfile(string, opfile):
    opfile.write('%s' % string)


def main():
    opfile = open('temp/dict-eq-qa-1.txt', 'w')
    opfile_etl = open('temp/eq-qa-etl-jobs-list.txt', 'w')
    opfile_bq = open('temp/eq-qa-load-to-bq-jobs-list.csv', 'w')
    output_files = {"all": opfile, "etl": opfile_etl, "bq": opfile_bq }
    bitbucket_path = "/Users/parth/Documents/bitbuckets/"
    repo_path = "acm-dp-eq-etl-config/"           # Change the project name and point to correct repo
    env = "qa"                                    # Change the env parameter to grab specific dsl script
    fileyml = open(bitbucket_path + repo_path + 'DSL/' + env + '/jobs.yaml', 'r')
    y = yaml.load(fileyml, Loader=yaml.FullLoader)

    opfile_bq.write('Job-type, DB-name, Tab-name, Load-to-bq, etl-Job')
    # search_key="ETL-Hourly"
    for search_key in ("ETL-Hourly", "ETL-Daily"):
        read_yaml(search_key, y,output_files,search_key)
    fileyml.close()
    opfile.close()
    opfile_etl.close()
    opfile_bq.close()


if __name__ == '__main__':
    print(">>>>> Started")
    main()
    # fetch_config()
    print(">>>>> Ended")

