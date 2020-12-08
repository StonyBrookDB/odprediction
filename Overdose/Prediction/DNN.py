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



model = Sequential()
model.add(Dense(512, activation='relu',input_shape=(trainx.shape[1]*trainx.shape[2],)))
model.add(Dropout(0.3))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(8, activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['mae', 'acc'])
model.fit(trainx.reshape((trainx.shape[0],5*4610)),trainy,epochs=20)

