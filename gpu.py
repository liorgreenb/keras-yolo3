import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

def set_gpu_session():
    # print('Setting gpu session')
    # config = tf.ConfigProto(allow_soft_placement = True)
    # config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU
    # # config.log_device_placement = True  # to log device placement (on which device the operation ran)
    #                                     # (nothing gets printed in Jupyter, only if you run it standalone)
    # sess = tf.Session(config=config)
    # set_session(sess)  # set this TensorFlow session as the default session for Keras
