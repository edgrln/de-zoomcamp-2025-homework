#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from time import time
import argparse
import sys 
import os



def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    print(params)
    print(url.split('.')[-1])
   
    csv_name = 'output.csv'

    os.system(f'wget {url} -O {csv_name}')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    if url.split('.')[-1] in "gz":
        df_iter = pd.read_csv(csv_name,  encoding='utf-8', compression='gzip', iterator=True, chunksize=100000)
    elif url.split('.')[-1] in "csv":
        df_iter = pd.read_csv(csv_name,  encoding='utf-8', iterator=True, chunksize=100000)
    else:
         print(f"Your url is not correct: {url}", f"End your link: {url.split('.')[-1]}")
    df = next(df_iter)
    if 'tpep_pickup_datetime' in list(df.columns):
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')

    while True:
        t_start = time()
        df = next(df_iter)
        if 'tpep_pickup_datetime' in list(df.columns):
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        df.to_sql(name=table_name, con=engine, if_exists='append')

        t_end = time()

        print(f'inserted another chunk ...{t_end - t_start}')




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Injest CSV data to PostgreSQL')

    # user 
    # password
    # host
    # database name
    # table name
    # url of the csv
    # print(sys.argv)
    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='table name for postgres')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    main(args)


