import logging
import numpy as np

class Input_builder(object):
    def __init__(self):
        pass

    def __call__(self, model,x,y=None,train_window=20,train_window_2=None):
        if model=='weibull':
            return self.create_weibull_input(x,y,train_window)

    def create_weibull_input(self,x,y,train_windows=20):
        index_end=len(y)-1
        y=list(y)
        for yy in y[::-1]:
            if yy!=y[-1]:
                index_end=y.index(yy)
                break
        index_begin=index_end-train_windows if (index_end-train_windows>0) else 1
        x,y=x[index_begin:index_end],y[index_begin:index_end]
        logging.info("Weibull train data {}".format(len(x)))
        return np.array(x),np.array(y)
