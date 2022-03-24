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
    result = reg.predict([[target]])
    if result[0]/target*100 > 30:
        flag = False
    else:
        flag = True

    result = jsonify({"predicted":result[0],"flag":flag})
    return result
