import pandas as pd
import json
from pandas import json_normalize
class Joiner:
    def __init__(self, df1, df2,joinType,joiningKeys):
        self.df1 = df1
        self.df2 = df2
        self.joinType = joinType
        self.joiningKeys = joiningKeys
    
    def join_dataframes(self):
        result = pd.merge(self.df1,self.df2, how=self.joinType,on=self.joiningKeys)
        print(self.df1,self.df2,self.joinType,self.joiningKeys)
        return result


