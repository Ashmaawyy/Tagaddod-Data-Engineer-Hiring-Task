import json
import pprint
import pandas as pd

json_file = open('./Data/Raw Data/tagaddod-d8ffe--MsZkGFSCtYxntenMuVF-export.json')
json_data_dict = json.load(json_file)
fields = ['collector_id', 'device_id', 'latitude', 'longitude', 'snapshot_datetime']

json_data_df = pd.DataFrame.from_dict(json_data_dict, orient = 'index')
json_data_df.to_csv(r'./Data/Transformed Data/Tagaddod_json_data.csv', index = False, header = True)
