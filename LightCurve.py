import requests
from io import StringIO
import pandas as pd

url = 'https://catalogs.mast.stsci.edu/api/v0.1/panstarrs/dr2/detection.csv'

class LightCurve:
    def __init__(self,id):
        try:
            self.objid = id
            r = requests.get(url,params={'objID':self.objid})
            if r.status_code != 200:
                raise Exception(f'An issue occured with the request. Status code {r.status_code}!')
            if not r.text:
                raise Exception(f'The ID you provided did not map to a single detection object.')

            self.stream = StringIO(r.text)
        except:
            raise Exception('Some error with the ID you passed in occured. Please check your ID.')

    # returns a pandas dataframe of detections
    def to_dataframe(self):
        self.stream.seek(0)
        df = pd.read_csv(self.stream)
        return df
    
    # returns a CSV file
    def to_csv(self,path):
        df = self.to_dataframe()
        df.to_csv(path)


    
