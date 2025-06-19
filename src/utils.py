# GCP read/write functions

from google.cloud import storage
from io import StringIO

import pandas as pd

def gcp_read_csv(gcp_client_obj, bucket_name, csv_file_name):
    file = gcp_client_obj.bucket(bucket_name).blob(csv_file_name)
    data = file.download_as_text()
    df = pd.read_csv(StringIO(data))

    return df

def gcp_write_csv(gcp_client_obj, dataframe, bucket_name, csv_file_name):
    file = gcp_client_obj.bucket(bucket_name).blob(csv_file_name)

    test = ''
    if file.exists():
        while test not in ['y', 'n']:
            test = input("You are attempting an overwrite. Proceed? Y/n").lower()

    if test == 'n':
            print('Write canceled.')
    else: 
        csv_buffer = StringIO()
        dataframe.to_csv(csv_buffer, index = False)
        file.upload_from_string(csv_buffer.getvalue(), content_type = 'text/csv')
        print('Write complete.')