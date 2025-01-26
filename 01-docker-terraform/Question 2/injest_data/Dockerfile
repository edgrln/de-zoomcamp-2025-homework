FROM python:3.11


WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# CMD python3 injest_data.py --user=root --password=root --host=pgdatabase --port=5432 --db=ny_taxi --table_name=yellow_taxi_trips --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

ARG user
ARG password
ARG host
ARG port
ARG db
ARG table_name 
ARG url



ENV user=${user} password=${password} host=${host} port=${port} db=${db} table_name=${table_name} url=${url}

ENTRYPOINT python3 injest_data.py --user=$user --password=$password --host=$host --port=$port --db=$db --table_name=$table_name --url=$url

