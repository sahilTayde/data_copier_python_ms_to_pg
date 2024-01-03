import sys
import os
from config import *
from util import *
import pandas as pd
from read import *
from write import *

def main():
    """ Program takes atleast one argument"""
    env = sys.argv[1]
    if env is not None :
       db_details = load_db_details(env)
    table_to_load=get_tables("table_list.config")
    for i in table_to_load['table_name'] :
        data,column_names = read_table(db_details,i,10)
        for rec in data :
            print(rec)
    load_table(env)
    

    
   
       


if __name__ == "__main__":
    main()
