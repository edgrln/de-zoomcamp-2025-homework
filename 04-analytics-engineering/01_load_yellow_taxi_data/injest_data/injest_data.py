from concurrent.futures import ThreadPoolExecutor
from google.oauth2 import service_account
import pandas_gbq
import pandas as pd


CREDENTIALS_FILE = "gcp_cred/gcp_cred.json"  

project_id = "de-zoomcamp-450307"
table_id = 'zoomcamp.fhv_tripdata'


BASE_URL =  "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/"

credentials = service_account.Credentials.from_service_account_file(
    CREDENTIALS_FILE,
)



years = [2019, 2020]
YEARS_MONTHS = [f"{year}-{i:02d}" for year in years for i in range(1, 13)] 

csv_name = f"{BASE_URL}fhv_tripdata_{YEARS_MONTHS[0]}.csv.gz"
table_name = table_id

# print(csv_name)


df = pd.read_csv(csv_name,  encoding='utf-8', compression='gzip', nrows=1)
df = df.head(n=0)
pandas_gbq.to_gbq(df, table_id, project_id, credentials=credentials, if_exists='replace')





def upload_to_bg(year_month):
    csv_name = f"{BASE_URL}fhv_tripdata_{year_month}.csv.gz"
    
    if csv_name.split('.')[-1] in "gz":
        df_iter = pd.read_csv(csv_name,  encoding='utf-8', compression='gzip', iterator=True, chunksize=100000)
    elif csv_name.split('.')[-1] in "csv":
        df_iter = pd.read_csv(csv_name,  encoding='utf-8', iterator=True, chunksize=100000)
    else:
         print(f"Your url is not correct: {BASE_URL}", f"End your link: {csv_name.split('.')[-1]}")
    
    while True:
        df = next(df_iter)
        pandas_gbq.to_gbq(df, table_id, project_id, credentials=credentials, if_exists='append')

# with ThreadPoolExecutor(max_workers=1) as executor:
#     executor.map(upload_to_bg, YEARS_MONTHS)


for year_month in YEARS_MONTHS:
    upload_to_bg(year_month)