import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def regression(filename,threshold,target):
    df = pd.read_csv(filename)
    reg = linear_model.LinearRegression()
    reg.fit(df[['volume']], df.emission)
    result = reg.predict([[target]])
    return result
