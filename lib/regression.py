import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
import json
from sklearn import linear_model

def regression(filename,threshold,target):
    df = pd.read_csv(filename)
    reg = linear_model.LinearRegression()
    reg.fit(df[['volume']], df.emission)
    res = reg.predict([[target]])
    result = res[0]
    if (result/target)*100 > 30:
        flag = False
    else:
        flag = True

    df = df.sort_values(by=['volume'], axis=0, ascending=True)
    result = jsonify({"predicted":result,"flag":flag, "data":{"volume":df['volume'].to_list(),"emission":df['emission'].to_list()}})
    return result
