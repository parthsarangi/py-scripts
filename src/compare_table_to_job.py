import yaml
import glob

def compare(repo):
    config_path = '/Users/parth/Documents/bitbuckets/' + repo + '/ETL/config/acm-eq/'
    dsl_path = '/Users/parth/Documents/bitbuckets/' + repo + 'DSL/qa/jobs.yaml'
    fileyml = open(dsl_path, 'r')
    y = yaml.load(fileyml, Loader=yaml.FullLoader)
    fileyml.close()

    tables = (glob.glob(config_path + "*"))
    for table in tables:


if __name__ == '__main__':
    print(">>> Started")
    repo = "acm-dp-eq-etl-config"
    compare(repo)
    print(">>> Ended")
