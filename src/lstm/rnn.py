
import tensorflow as tf
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout, Activation, GRUCell, RNN



class RNNModel(object):
    def __init__(self, params):
        self.params = params
        cell = GRUCell(units=self.params['rnn_size'])
        self.rnn = RNN(cell, return_state=True, return_sequences=True)
        self.bn = BatchNormalization()
        cell2 = GRUCell(units=self.params['rnn_size2'])
        self.rnn2 = RNN(cell2, return_state=True, return_sequences=True)
        self.dense = Dense(units=self.params['dense_size'])

    def __call__(self, x):
        pass


