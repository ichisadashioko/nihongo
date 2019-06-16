# encoding=utf-8
# import os
# import math
# import re

import numpy as np
import pandas as pd

if __name__ == "__main__":
    csv_filename = 'ruby_furigana.csv'
    pd_df = pd.read_csv(csv_filename, encoding='utf-8')
    pd_df = pd_df.sort_values(['word'])
    pd_df.to_csv(csv_filename, encoding='utf-8', index=False)
