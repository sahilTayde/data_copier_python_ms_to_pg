import os

DB_DETAILS={

    'dev': {
        'SOURCE_DB_DETAILS' :{
                 'DB_TYPE': 'mysql',
                 'DB_HOST': 'localhost',
                 'DB_NAME': 'retail',
                 'DB_USER': os.environ.get('SOURCE_DB_USER'),
                 'DB_PASS': os.environ.get('SOURCE_DB_PASS'),
                 'DB_PORT': '3306'
        },
        'TARGET_DB_DETAILS' :{
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('TARGET_DB_USER'),
            'DB_PASS': os.environ.get('TARGET_DB_PASS'),
            'DB_PORT': '5534'
        }
    }
}

