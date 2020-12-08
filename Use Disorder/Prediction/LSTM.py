import csv
import numpy as np
from datetime import datetime
from collections import Counter
from sklearn.preprocessing import OneHotEncoder
import os
from keras.models import Sequential
from keras.layers import Dense,Dropout,normalization,BatchNormalization,LSTM,GRU
from keras import backend as K
os.environ['KMP_DUPLICATE_LIB_OK']='True'
os.environ['CUDA_VISIBLE_DEVICES']='4'


lstm = Sequential()
lstm.add(LSTM(512, input_shape=(trainx.shape[1], trainx.shape[2]),return_sequences=True))
lstm.add(LSTM(512))
lstm.add(Dense(8))
lstm.add(Dense(1))
lstm.compile(loss='binary_crossentropy',optimizer='adam',metrics=['mae', 'acc'])
lstm.fit(trainx,trainy,epochs=100,batch_size=64,verbose=1)

proba=lstm.predict(testx)

