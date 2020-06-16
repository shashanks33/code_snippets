import tensorflow as tf

class myCallBacks(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        keys = logs.keys()
        if logs.get('acc') > 0.99:
            print('Reached 99'%' accuracy so ending the training.')
            self.model.stop_training = True