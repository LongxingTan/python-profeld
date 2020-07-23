
# -*- coding: utf-8 -*-
# @author: Longxing Tan, tanlongxing888@163.com
# @date: 2020-03


import tensorflow as tf
from tensorflow.keras.layers import Dense


class GaussianLayer(tf.keras.layers.Layer):
    def __init__(self,output_dim):
        super(GaussianLayer,self).__init__()
        self.output_dim=output_dim

    def build(self,inputs_shape):
        self.fc1 = Dense(units=self.output_dim,
                         kernel_initializer='glorot_normal',
                         bias_initializer='glorot_normal')
        self.fc2 = Dense(units=self.output_dim,
                         kernel_initializer='glorot_normal',
                         bias_initializer='glorot_normal')
        super(GaussianLayer.self).build(inputs_shape)

    def call(self, x):
        output_mu= self.fc1(x)
        output_sig= self.fc2(x)
        output_sig_pos= tf.math.log(1+tf.math.exp(output_sig)) + 1e-6
        return output_mu, output_sig_pos

