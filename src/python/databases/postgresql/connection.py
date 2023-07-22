import os
import psycopg2 as pg

def get_conn_url_from_env()->str:
    host=os.getenv('POSTGRES_HOST')
    port=os.getenv("POSTGRES_PORT") 
    dbname=os.getenv("POSTGRES_DB")
    user=os.getenv("POSTGRES_USER")
    password=os.getenv("POSTGRES_PASSWORD")
    return f'postgres://{user}:{password}@{host}:{port}/{dbname}'

def test_db_connection(conn_url:str)->None:
    dbname=os.getenv('POSTGRES_DB')
    with pg.connect(conn_url) as conn:
       cursor=conn.cursor()
       print(f'Database {dbname} connected!')