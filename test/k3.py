'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-14 14:43:19
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-14 15:05:41
'''
from keras.optimizers import SGD

from keras.layers import Dense,Dropout


from keras.models import Sequential
import numpy as np


model = Sequential()
model.add(Dense(22,activation='relu',input_dim=1212))
sgd = SGD(lr=0.001,decay=1e-06, momentum=0.9, nesterov=True)
model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy'])
model.add(Dropout(0.5))                             # 新增
model.add(Dense(1, activation='sigmoid'))           # 新增
x_train = np.random.random((1000,1212))
x_test = np.random.random((100,1212))
y_train = np.random.randint(2, size=(1000, 1))
y_test = np.random.randint(2, size=(100, 1))
model.fit(x_train, y_train, batch_size=32, epochs=10)
score = model.evaluate(x_test, y_test, batch_size=64)

print(score)