import sys
import os
from config import *
from util import *
import pandas as pd

def main():
    """ Program takes atleast one argument"""
    env = sys.argv[1]
    if env is not None :
       db_details = DB_DETAILS[env] 
    table_to_load=get_tables("table_list.config")
    for i in table_to_load['table_name'] :
        table_name = i;
    print(table_name)

    
   
       


if __name__ == "__main__":
    main()
