import yaml


def read_yaml(y,opfile,search_key):
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
                                # print(k2,'/',k3)
                                s = s + 1
                                opfile.write('Serial: %s\n' % s)
                                opfile.write('Job-name: %s\n' % k3)
                                for k4, v4 in v3.items():
                                    if k4 == "profile":
                                        opfile.write('Config-name: %s\n' % v4)
                                        print(v4)
                                        pos_slash = v4.index("/") + 1
                                        file = v4[pos_slash:len(v4)]
                                        fetch_config(file, opfile)
                                    if k4 == "dataSourceUrl":
                                        question_pos = v4.index("_qa?")  # take the correct region name from jobs.yaml file
                                        port_pos = v4.index(":3306/") + 6
                                        db_name = v4[port_pos:question_pos]
                                        opfile.write('Db-name: %s\n' % (db_name))
                                        opfile.write('\n')


def fetch_config(file, opfile):
    config_path = "/Users/parth/Documents/bitbuckets/acm-dp-eq-etl-config/ETL/config/acm-eq/"
    # file = "rule_action"
    config_file = open(config_path + file + "/config.properties", 'r')
    for line in config_file:
        if "etl.input.schema" in line:
            pos = line.index("=")
            opfile.write('Table-name: %s' % line[pos+1:len(line)])
        if "etl.output.storage" in line:
            # print(">> " + line)
            opfile.write('Storage-path: %s' % line)

    config_file.close()


def main():
    opfile = open('temp/dict-eq-qa.txt', 'w')
    bitbucket_path = "/Users/parth/Documents/bitbuckets/"
    repo_path = "acm-dp-eq-etl-config/"           # Change the project name and point to correct repo
    env = "qa"                                    # Change the env parameter to grab specific dsl script
    fileyml = open(bitbucket_path + repo_path + 'DSL/' + env + '/jobs.yaml', 'r')
    y = yaml.load(fileyml, Loader=yaml.FullLoader)
    # search_key="ETL-Hourly"
    for search_key in ("ETL-Hourly", "ETL-Daily"):
        read_yaml(y,opfile,search_key)
    fileyml.close()
    opfile.close()


if __name__ == '__main__':
    print(">>>>> Started")
    main()
    # fetch_config()
    print(">>>>> Ended")
