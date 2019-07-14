import yaml

def read_yaml(y,opfile,search_key):
    for k1, v1 in y.items():
        if k1 == 'jobs':
            for items in v1:
                for k2,v2 in items.items():
                    if k2==search_key:
                        for item1 in v2:
                            for k3,v3 in item1.items():
                                # print(k2,'/',k3)
                                opfile.write('            - name: "%s%s%s"\n' % (k2, '/', k3))


def main():
    opfile = open('temp/dict.txt', 'w')
    fileyml = open('/Users/parth/Documents/bitbuckets/acm-dp-eq-mm-etl-config/DSL/staging/jobs.yaml', 'r')
    y = yaml.load(fileyml, Loader=yaml.FullLoader)
    search_key="ETL-History"
    read_yaml(y,opfile,search_key)
    fileyml.close()
    opfile.close()


main()
