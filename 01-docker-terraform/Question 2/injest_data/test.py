

url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

if url.split('.')[-1] == 'gz':
    print('yes')
else:
    print('no')


print(url.split('.')[-1] )