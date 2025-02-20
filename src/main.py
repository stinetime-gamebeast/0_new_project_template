# Use main.py to write the key functionality of your program
## See how functions from utils.py are imported
## Libraries specific to main.py must be imported (i.e., pandas), but libraries specific to utils.py (i.e., itertools) are handled by the utils import

import pandas as pd
from utils import all_column_combos

def df_column_combos(df):
    if isinstance(df, pd.DataFrame):
        columns_list = list(df.columns)
        return all_column_combos(range(0, len(columns_list)))
    else:
        print('Input is not a DataFrame. Please convert your input to a DataFrame and try again.')