from util import get_connection

def read_table(db_details,table_name,limit=0):
    SOURCE_DB_DETAILS=db_details['SOURCE_DB_DETAILS']
    
    connection = get_connection(

        db_type=SOURCE_DB_DETAILS['DB_TYPE'],
        db_user=SOURCE_DB_DETAILS['DB_USER'], 
        db_pass=SOURCE_DB_DETAILS['DB_PASS'],
        db_host=SOURCE_DB_DETAILS['DB_HOST'],
        db_name=SOURCE_DB_DETAILS['DB_NAME'],
        db_port=SOURCE_DB_DETAILS['DB_PORT']
        
    )
    print(connection)
    cursor = connection.cursor()
    if limit ==0:
        query = f'select * from {table_name}'
    else :
        query = f'select * from {table_name} limit {limit}'
    cursor.execute(query)
    data = cursor.fetchall()
    column_names=cursor.column_names
    connection.close()
    return data,column_names