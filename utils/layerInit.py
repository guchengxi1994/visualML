'''
@lanhuage: python
@Descripttion: 
@version: beta
@Author: xiaoshuyui
@Date: 2020-05-11 17:19:38
@LastEditors: xiaoshuyui
@LastEditTime: 2020-05-15 09:11:50
'''

layers = {
    'Input':"",
    'Dense':"",
    'Dropout':"",
    'Flatten':"",
    'Conv2D':"",
    'MaxPooling2D':"", 
}

all_layers_core = ['Dense','Activation','Dropout','Flatten', \
    'Reshape','Permute','RepeatVector','Lambda','ActivityRegularization', \
    'Masking','SpatialDropout1D','SpatialDropout1D','SpatialDropout1D']

all_layers_conv = ['Conv1D','Conv2D','SeparableConv1D','SeparableConv2D', \
    'DepthwiseConv2D','Conv2DTranspose','Conv3D','Conv3DTranspose','Cropping1D', \
    'Cropping2D','Cropping3D','UpSampling1D','UpSampling2D','UpSampling3D','ZeroPadding1D', \
    'ZeroPadding2D','ZeroPadding3D']

all_layers_pool = ['MaxPooling1D','MaxPooling2D','MaxPooling3D','AveragePooling1D', \
    'AveragePooling2D','AveragePooling3D','GlobalMaxPooling1D','GlobalMaxPooling2D', \
    'GlobalMaxPooling3D', 'GlobalAveragePooling2D','GlobalAveragePooling1D','GlobalAveragePooling3D']

all_activations = ['LeakyReLU','PReLU','ELU','ThresholdedReLU','Softmax','ReLU']

others = ['Input','Layer','InputLayer']

padding = [
    'same',
    'valid',
]