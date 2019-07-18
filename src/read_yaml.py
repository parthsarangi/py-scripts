import yaml


def read_yaml(y,opfile,search_key):
    for k1, v1 in y.items():
        if k1 == 'jobs':
            print(">> Found jobs")
            for items in v1:
                for k2,v2 in items.items():
                    print("Found " + k2)
                    if k2==search_key:
                        print(">>> found search_key " + search_key)
                        opfile.write('>> Job type "%s"\n' % (k2))
                        for item1 in v2:
                            for k3,v3 in item1.items():
                                # print(k2,'/',k3)
                                opfile.write('>>      "%s"\n' % (k3))
                                for k4,v4 in v3.items():
                                    if k4 == "profile":
                                        opfile.write('>>          "%s"\n' % (v4))
                                        print(v4)
                                        pos_slash = v4.index("/") + 1
                                        file = v4[pos_slash:len(v4)]
                                        fetch_config(file)
                                    if k4 == "dataSourceUrl":
                                        question_pos = v4.index("_qa?")
                                        port_pos = v4.index(":3306/") + 6
                                        db_name = v4[port_pos:question_pos]
                                        opfile.write('>>       Db-name  : "%s"\n' % (db_name))


def fetch_config(file):
    config_path = "/Users/parth/Documents/bitbuckets/acm-dp-eq-etl-config/ETL/config/acm-eq/"
    # file = "rule_action"
    config_file = open(config_path + file + "/config.properties", 'r')
    for line in config_file:
        if "etl.output.storage" in line:
            print(">> " + line)
    config_file.close()


def main():
    opfile = open('temp/dict.txt', 'w')
    bitbucket_path = "/Users/parth/Documents/bitbuckets/"
    repo_path = "acm-dp-eq-etl-config/"
    fileyml = open(bitbucket_path + repo_path + 'DSL/qa/jobs.yaml', 'r')
    y = yaml.load(fileyml, Loader=yaml.FullLoader)
    search_key="ETL-Hourly"
    read_yaml(y,opfile,search_key)
    fileyml.close()
    opfile.close()


if __name__ == '__main__':
    print(">>>>> Started")
    main()
    # fetch_config()
    print(">>>>> Ended")
