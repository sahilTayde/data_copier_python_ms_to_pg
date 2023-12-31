import pandas as pd
from config import *
import mysql.connector as mc 
from mysql.connector import errorcode as ec

def load_db_details(env):
    return DB_DETAILS[env]

def get_connection(db_type,db_host,db_pass,db_port,db_name,db_user):
        connection=None
        if db_type=='mysql':
                try:
                    connection = mc.connect(
                        
                        user=db_user, 
                        password=db_pass,
                        host=db_host,
                        database=db_name,
                        port=db_port
                    )
                    print(connection)
                except mc.Error as error  :
                    if error.errno == ec.ER_ACCESS_DENIED_ERROR:
                        print("Invalid Credentials")
                    else:
                        print(error)
                
        return connection
                    

def get_tables(path):
    tables=pd.read_csv(path,sep=":",header = 0)
    return tables.map(lambda x : x.strip() ).query("to_be_loaded == 'yes'" )