# import pandas as pd
# import requests
import os
def lambda_handler(event, context):
    d = {'col1': [1,2], 'col2': [3,4]}
    # df = pd.DataFrame(data=d)
    print(os.getenv("URI"))
    print('Done x1')
    return d
