# import pandas as pd
import requests
def lambda_handler(event, context):
    d = {'col1': [1,2], 'col2': [3,4]}
    # df = pd.DataFrame(data=d)
    print(d)
    print('Done x1')
    return d
