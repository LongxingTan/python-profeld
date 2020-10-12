
# -*- coding: utf-8 -*-
# @author: Longxing Tan, tanlongxing888@163.com
# @date: 2020-03
# paper: https://arxiv.org/abs/1704.04110
# other implementations: https://github.com/arrigonialberto86/deepar


import tensorflow as tf
from tensorflow.keras.layers import (Input, LSTM, LSTMCell)


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


class DeepAR(object):
    def __init__(self):
        pass

    def __call__(self, inputs_shape, training):
        inputs = Input(inputs_shape)
        x = LSTM(units=4, return_sequence=True)(inputs)
        x = Dense(units=3, activation='relu')(x)
        loc, scale = GaussianLayer(1)(x)
        return tf.keras.Model(inputs,[loc,scale])


class GaussianLoss(object):
    def __init__(self):
        pass

    def __call__(self, y_true, y_pred, sigma):
        return tf.reduce_mean(0.5 * tf.math.log(sigma) +
                              0.5 * tf.math.divide(tf.math.square(y_true-y_pred),sigma))+1e-6+6

