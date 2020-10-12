# TensorFlow 2.x
# https://github.com/daynebatten/keras-wtte-rnn


import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense, GRUCell, LSTMCell, RNN


class Activate(Layer):
    def __init__(self):
        super(Activate, self).__init__()

    def call(self, x):
        a = tf.math.exp(x[:, 0])
        b = tf.math.softplus(x[:, 1])

        a = tf.reshape(a, [tf.shape(a)[0], 1])
        b = tf.reshape(b, [tf.shape(b)[0], 1])
        return tf.concat([a, b], axis=1)


class WTTE(object):
    def __init__(self, params):
        cell = GRUCell(units=params['rnn_units'])
        self.rnn = RNN(cell, return_state=True, return_sequences=True)
        self.dense = Dense(units=2)
        self.activate = Activate()

    def __call__(self, x):
        output, state = self.rnn(x)
        output = self.dense(output)
        output = self.activate(output)
        return output


def weibull_discrete(y_true, y_pred):
    y_ = y_true[:, 0]
    u_ = y_true[:, 1]
    a_ = y_pred[:, 0]
    b_ = y_pred[:, 1]

    hazard0 = tf.math.pow((y_ + 1e-35) / a_, b_)
    hazard1 = tf.math.pow((y_ + 1) / a_, b_)
    return -1 * tf.reduce_mean(u_ * tf.math.log(tf.math.exp(hazard1 - hazard0) - 1.0) - hazard1)


def weibull_continuous(y_true, y_pred):
    y_ = y_true[:, 0]
    u_ = y_true[:, 1]
    a_ = y_pred[:, 0]
    b_ = y_pred[:, 1]

    ya = (y_ + 1e-35) / a_
    return -1 * tf.reduce_mean(u_ * (tf.math.log(b_) + b_ * tf.math.log(ya)) - tf.math.pow(ya, b_))


class Trainer(object):
    def __init__(self):
        pass

    def train(self, train_dataset, valid_dataset=None):
        pass

    def train_step(self):
        pass

    def distribute_train_step(self):
        pass

    def valid_step(self):
        pass

    def export_model(self):
        pass
