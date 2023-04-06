#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : gru.py
@Author: XuYaoJian
@Date  : 2022/9/2 22:24
@Desc  :
"""

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras import Input
from tensorflow.keras.optimizers import Adam

def lstm(seq_len, learning_rate, hidden_size):
    # 建立模型
    optimizer = Adam(learning_rate=learning_rate)
    model = Sequential()
    model.add(Input(shape=(seq_len, 1)))
    model.add(LSTM(units=hidden_size, return_sequences=False, kernel_initializer='glorot_normal'))
    model.add(Dense(int(hidden_size/2), kernel_initializer='he_normal', activation='relu'))
    model.add(Dense(int(hidden_size/4), kernel_initializer='he_normal', activation='relu'))
    model.add(Dense(int(hidden_size/8), kernel_initializer='he_normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='he_normal'))
    model.compile(optimizer=optimizer, loss='mse')
    return model

