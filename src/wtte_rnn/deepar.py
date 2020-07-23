
# -*- coding: utf-8 -*-
# @author: Longxing Tan, tanlongxing888@163.com
# @date: 2020-03
# paper: https://arxiv.org/abs/1704.04110
# other implementations: https://github.com/arrigonialberto86/deepar


import tensorflow as tf
from tensorflow.keras.layers import (Input, LSTM, LSTMCell)
from deepts.layers.deepar_layer import GaussianLayer


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

