'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-14 16:51:02
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-14 17:01:35
'''
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
import keras

# 生成虚拟数据
x_train = np.random.random((1000, 20))
# y_train = np.random.randint(3, size=(1000, 1))
y_train = keras.utils.to_categorical(np.random.randint(2, size=(1000, 1)), num_classes=2)
x_test = np.random.random((100, 20))
# y_test = np.random.randint(3, size=(100, 1))
y_test = keras.utils.to_categorical(np.random.randint(2, size=(100, 1)), num_classes=2)

# print(y_test)

model = Sequential()
model.add(Dense(64, input_dim=20, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=1000,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)

print(score)