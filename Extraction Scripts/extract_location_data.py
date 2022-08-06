import json
import pprint
import pandas as pd

import_dir = r'./Data/Raw Data/tagaddod-d8ffe--MsZkGFSCtYxntenMuVF-export.json'
export_dir = r'./Data/Transformed Data/Tagaddod_json_data.csv'

def import_json_data_into_df(import_dir: str) -> dict:
    json_file = open(import_dir)
    json_data_dict = json.load(json_file)
    return pd.DataFrame.from_dict(json_data_dict, orient = 'index')

def export_json_data_into_csv(export_dir: str):
    import_json_data_into_df(import_dir).to_csv(export_dir, index = False, header = True)
