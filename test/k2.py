'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-14 10:53:39
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-14 11:03:07
'''

'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-11 08:49:25
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-11 17:31:28
'''
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from IPython.display import SVG as SVGImg
from keras.utils.vis_utils import model_to_dot

# 生成虚拟数据
import numpy as np
x_train = np.random.random((1000, 20))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(1000, 1)), num_classes=10)
x_test = np.random.random((100, 20))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)

model = Sequential()
# Dense(64) 是一个具有 64 个隐藏神经元的全连接层。
# 在第一层必须指定所期望的输入数据尺寸：
# 在这里，是一个 20 维的向量。
model.add(Dense(64, activation='relu', input_dim=20))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

# json_string = model.to_json()
# with open('mlp_model.json','w') as of:
#     of.write(json_string)
# plot_model(model, to_file='model.png')
SVGImg(model_to_dot(model).create(prog='dot', format='svg'))
model.fit(x_train, y_train,
          epochs=200,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)
