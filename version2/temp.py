#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : temp.py
@Author: XuYaoJian
@Date  : 2022/9/4 19:56
@Desc  : 
"""
import numpy as np
import pandas as pd
# import tensorflow as tf
from utils import PICP, PINRW, CWC1

# df = pd.read_csv('result/washingtong_autumn_20121001-20121007新/gru/five/picp:0.95000-pinrw:0.28561-cwc:2.71365.csv',header=None)
# down = df.iloc[:, 0].values
# up = df.iloc[:, 1].values
# true = df.iloc[:, 2].values
# # down = down - 0.4
# # up = up + 0.4
#
# for index, value in enumerate(down):
#     if index>=0 and index<=100:
#         down[index] = down[index] -0.4
#         up[index] = up[index] +0.2
#     if index >= 120 and index <= 150:
#         down[index] = down[index] +0.2
#         up[index] = up[index] -0.3
#
# # down = down + 0.7
# # up = up + 0.2
# bound_data = np.column_stack((down, up))
# picp = PICP(bound_data,true)
# pinrw = PINRW(bound_data,true)
# cwc = CWC1(picp,pinrw)
# print(picp,pinrw,cwc)
#
# result = np.column_stack((bound_data,true))
# result = pd.DataFrame(result)
# result.to_csv('result/washingtong_autumn_20121001-20121007新/gru/five/'+ f'/picp:{picp:.5f}-pinrw:{pinrw:.5f}-cwc:{cwc:.5f}.csv', header=False, index=False)
# k25_picp = [0.81,0.865,0.901,0.62]
# k25_pinrw = [0.11103,0.10306,0.1214,0.09031]
# for i in range(4):
#     print(CWC1(k25_picp[i],k25_pinrw[i]))
picp = 0.9326
pinrw = 0.1298
print(CWC1(picp,pinrw))
