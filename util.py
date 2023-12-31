import pandas as pd


def get_tables(path):
    tables=pd.read_csv(path,sep=":",header = 0)
    return tables.map(lambda x : x.strip() ).query("to_be_loaded == 'yes'" )