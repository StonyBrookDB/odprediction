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


bilstm = Sequential()
bilstm.add(Bidirectional(LSTM(512, input_shape=(trainx3.shape[1], trainx3.shape[2]),return_sequences=True)))
bilstm.add(Bidirectional(LSTM(512)))
bilstm.add(Dense(1))
bilstm.compile(loss='binary_crossentropy',optimizer='adam',metrics=['mae', 'acc'])
bilstm.fit(trainx3,trainy2,epochs=1,batch_size=64,verbose=1)
