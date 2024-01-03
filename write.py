from util import *
from config import *

def load_table(db_details):
    
    TARGET_DB_DETAILS=load_db_details(db_details)['TARGET_DB_DETAILS']
    connection = get_connection(

        db_type=TARGET_DB_DETAILS['DB_TYPE'],
        db_user=TARGET_DB_DETAILS['DB_USER'], 
        db_pass=TARGET_DB_DETAILS['DB_PASS'],
        db_host=TARGET_DB_DETAILS['DB_HOST'],
        db_name=TARGET_DB_DETAILS['DB_NAME'],
        db_port=TARGET_DB_DETAILS['DB_PORT']
        
    )

    cursor = connection.cursor()
    query='select * from departments'
    cursor.execute(query)
    data = cursor.fetchall()
    for i in data:
        print(i)





