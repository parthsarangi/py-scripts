import yaml


def main_read_pipelines_yaml():
    input_file = open("/Users/parth/Documents/bitbuckets/acm-dp-eq-mm-etl-config/DSL/staging/pipelines.yaml", 'r')
    inputData = yaml.load(input_file, Loader=yaml.FullLoader)

    searchList = ["ETL-Daily", "ETL-Hourly", "ETL-Initial"]

    for k1, v1 in inputData.items():
        # print("key found : " + k1)
        if k1 == 'jobs':
            for values in v1:
                for k2, v2 in values.items():
                    # print(" 2nd level key :" + k2)
                    return 0
    return 0


def main_read_jobs_yaml():
    input_file = open("/Users/parth/Documents/bitbuckets/acm-dp-eq-mm-etl-config/DSL/staging/jobs.yaml", 'r')
    inputData = yaml.load(input_file, Loader=yaml.FullLoader)

    searchList = ["ETL-Daily", "ETL-Hourly", "ETL-Initial"]
    # searchList = ["ETL-Initial"]

    for k1, v1 in inputData.items():
        # print("key found : " + k1)
        if k1 == 'jobs':
            for values in v1:
                for k2, v2 in values.items():
                    # print(" 2nd level key :" + k2)
                    for searchItem in searchList:
                        if k2 == searchItem:
                            # print("Search Item is :" + searchItem)
                            for jobs in v2:
                                for k3, v3 in jobs.items():
                                    print(k2 + " , " + k3)
                                    # if k3 == "eq.payment.tier-level":
                                    # if 1 == 1:
                                    #     print(searchItem + "," + k3)
                                    #     try:
                                    #         for k4, v4 in v3:
                                    #             # for k4, v4 in items:
                                    #         print(k4 + ": " + v4)
                                    #     except:
                                    #         print("Not found any values")


if __name__ == '__main__':
    print(">>> >>>")
    main_read_jobs_yaml()
    print(">>> >>>")