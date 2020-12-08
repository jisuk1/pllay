# -*- coding: utf-8 -*-
"""mnist_eval

Automatically generated by Colaboratory.
"""

import numpy as np
import tensorflow.compat.v2 as tf
import time

tf.enable_v2_behavior()

from pllay import *

"""# Evaluation"""

nmax_diag = 32


class MNIST_MLP(tf.keras.Model):
    def __init__(self, name='mnistmlp', unitsDense=64, **kwargs):
        super(MNIST_MLP, self).__init__(name=name, **kwargs)
        # self.layer1 = tf.keras.layers.Dense(32, name='dense_1')
        # self.layer1 = TopoWeightLayer(32, m0=0.1, tseq=[v/10. for v in range(31)], KK=list(range(30)), by=1./13.5)
        # self.layer1_1 = TopoWeightLayer(unitsTop, m0=0.05, tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)), by=1./13.5)
        # self.layer1_2 = TopoWeightLayer(unitsTop, m0=0.2, tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)), by=1./13.5)
        # self.layer1_1 = GThetaLayer(unitsTop)
        # self.layer1_2 = GThetaLayer(unitsTop)
        # self.layer2 = tf.keras.layers.Dense(32, activation='relu', name='dense_2') 
        self.layer2 = tf.keras.layers.Dense(unitsDense, activation='relu', name='dense_2') 
        self.layer3 = tf.keras.layers.Dense(10, name='predictions')

    def call(self, x):
        xg, xl1, xl2, xd = tf.split(x, [784, 100, 162, 8*nmax_diag], axis=-1)
        # xl1 = tf.nn.relu(self.layer1_1(xl1))
        # xl2 = tf.nn.relu(self.layer1_2(xl2))
        # x = tf.concat((xg, xl1, xl2), -1)
        x = xg
        x = self.layer2(x)
        x = self.layer3(x)
        print(x.shape)
        return x


class MNIST_MLP_PLLay(tf.keras.Model):
    def __init__(self, name='mnistmlppllay', unitsDense=64, unitsTop=32, **kwargs):
        super(MNIST_MLP_PLLay, self).__init__(name=name, **kwargs)
        # self.layer1 = tf.keras.layers.Dense(32, name='dense_1')
        # self.layer1 = TopoWeightLayer(32, m0=0.1, tseq=[v/10. for v in range(31)], KK=list(range(30)), by=1./13.5)
        # self.layer1_1 = TopoWeightLayer(unitsTop, m0=0.05, tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)), by=1./13.5)
        # self.layer1_2 = TopoWeightLayer(unitsTop, m0=0.2, tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)), by=1./13.5)
        self.layer1_1 = GThetaLayer(unitsTop)
        self.layer1_2 = GThetaLayer(unitsTop)
        # self.layer2 = tf.keras.layers.Dense(32, activation='relu', name='dense_2') 
        self.layer2 = tf.keras.layers.Dense(unitsDense, activation='relu', name='dense_2') 
        self.layer3 = tf.keras.layers.Dense(10, name='predictions')

    def call(self, x):
        xg, xl1, xl2, xd = tf.split(x, [784, 100, 162, 8*nmax_diag], axis=-1)
        xl1 = tf.nn.relu(self.layer1_1(xl1))
        xl2 = tf.nn.relu(self.layer1_2(xl2))
        x = tf.concat((xg, xl1, xl2), -1)
        # x = xg
        x = self.layer2(x)
        x = self.layer3(x)
        print(x.shape)
        return x


class MNIST_CNN(tf.keras.Model):
    def __init__(self, name='mnistcnn', filters=32, kernel_size=3, unitsDense=64, **kwargs):
        super(MNIST_CNN, self).__init__(name=name, **kwargs)
        # self.layer1_1 = tf.keras.layers.Conv2D(32, 3, padding="same", activation='relu')
        # self.layer1_2 = tf.keras.layers.Conv2D(1, 3, padding="same", activation='relu')
        self.layer1_1 = tf.keras.layers.Conv2D(filters, kernel_size, padding="same", activation='relu')
        self.layer1_2 = tf.keras.layers.Conv2D(1, kernel_size, padding="same", activation='relu')
        # self.layer1_3 = TopoWeightLayer(32, m0=0.1, tseq=[v/10. for v in range(31)], KK=list(range(30)), by=1./13.5)
        # self.layer1_3 = TopoWeightLayer(unitsTop, m0=0.05, tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)), by=1./13.5)
        # self.layer1_4 = TopoWeightLayer(unitsTop, m0=0.2, tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)), by=1./13.5)
        # self.layer1_3 = TopoFunLayer(unitsTop, grid_size=[28, 28], tseq=np.linspace(0.05, 0.95, 18), KK=list(range(3)))
        # self.layer2_1 = TopoWeightLayer(unitsTopInput, m0=0.05, tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)), by=1./13.5)
        # self.layer2_2 = TopoWeightLayer(unitsTopInput, m0=0.2, tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)), by=1./13.5)
        # self.layer2_1 = GThetaLayer(unitsTopInput)
        # self.layer2_2 = GThetaLayer(unitsTopInput)
        # self.layer3 = tf.keras.layers.Dense(32, activation='relu', name='dense_2') 
        self.layer3 = tf.keras.layers.Dense(unitsDense, activation='relu', name='dense_2') 
        self.layer4 = tf.keras.layers.Dense(10, name='predictions')

    def call(self, x):
        xg, xl1, xl2, xd = tf.split(x, [784, 100, 162, 8*nmax_diag], axis=-1)
        xg = tf.reshape(xg, [16, 28, 28, 1])
        xg1 = self.layer1_1(xg)
        xg1 = self.layer1_2(xg1)
        #print(x1.shape)
        xg1 = tf.reshape(xg1, [16, 784])
        # xg1_1 = tf.nn.relu(self.layer1_3(xg1))
        # xg1_2 = tf.nn.relu(self.layer1_4(xg1))
        # xg1 = tf.concat((xg1, xg1_1, xg1_2), -1)
        # xg1 = tf.concat((xg1, xg1_1), -1)
        # xl1 = tf.nn.relu(self.layer2_1(xl1))
        # xl2 = tf.nn.relu(self.layer2_2(xl2))
        # x = tf.concat((xg1, xl1, xl2), -1)
        x = xg1
        x = self.layer3(x)
        x = self.layer4(x)
        print(x.shape)
        return x


class MNIST_CNN_PLLay_Input(tf.keras.Model):
    def __init__(self, name='mnistcnnpllayinput', filters=32, kernel_size=3, unitsDense=64, unitsTopInput=32, **kwargs):
        super(MNIST_CNN_PLLay_Input, self).__init__(name=name, **kwargs)
        # self.layer1_1 = tf.keras.layers.Conv2D(32, 3, padding="same", activation='relu')
        # self.layer1_2 = tf.keras.layers.Conv2D(1, 3, padding="same", activation='relu')
        self.layer1_1 = tf.keras.layers.Conv2D(filters, kernel_size, padding="same", activation='relu')
        self.layer1_2 = tf.keras.layers.Conv2D(1, kernel_size, padding="same", activation='relu')
        # self.layer1_3 = TopoWeightLayer(32, m0=0.1, tseq=[v/10. for v in range(31)], KK=list(range(30)), by=1./13.5)
        # self.layer1_3 = TopoWeightLayer(unitsTopMiddle, m0=0.05, tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)), by=1./13.5)
        # self.layer1_4 = TopoWeightLayer(unitsTopMiddle, m0=0.2, tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)), by=1./13.5)
        # self.layer1_3 = TopoFunLayer(unitsTopMiddle, grid_size=[28, 28], tseq=np.linspace(0.05, 0.95, 18), KK=list(range(3)))
        # self.layer2_1 = TopoWeightLayer(unitsTopInput, m0=0.05, tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)), by=1./13.5)
        # self.layer2_2 = TopoWeightLayer(unitsTopInput, m0=0.2, tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)), by=1./13.5)
        self.layer2_1 = GThetaLayer(unitsTopInput)
        self.layer2_2 = GThetaLayer(unitsTopInput)
        # self.layer3 = tf.keras.layers.Dense(32, activation='relu', name='dense_2') 
        self.layer3 = tf.keras.layers.Dense(unitsDense, activation='relu', name='dense_2') 
        self.layer4 = tf.keras.layers.Dense(10, name='predictions')

    def call(self, x):
        xg, xl1, xl2, xd = tf.split(x, [784, 100, 162, 8*nmax_diag], axis=-1)
        xg = tf.reshape(xg, [16, 28, 28, 1])
        xg1 = self.layer1_1(xg)
        xg1 = self.layer1_2(xg1)
        #print(x1.shape)
        xg1 = tf.reshape(xg1, [16, 784])
        # xg1_1 = tf.nn.relu(self.layer1_3(xg1))
        # xg1_2 = tf.nn.relu(self.layer1_4(xg1))
        # xg1 = tf.concat((xg1, xg1_1, xg1_2), -1)
        # xg1 = tf.concat((xg1, xg1_1), -1)
        xl1 = tf.nn.relu(self.layer2_1(xl1))
        xl2 = tf.nn.relu(self.layer2_2(xl2))
        x = tf.concat((xg1, xl1, xl2), -1)
        # x = xg1
        x = self.layer3(x)
        x = self.layer4(x)
        print(x.shape)
        return x


class MNIST_CNN_PLLay(tf.keras.Model):
    def __init__(self, name='mnistcnnpllay', filters=32, kernel_size=3, unitsDense=64, unitsTopInput=32, unitsTopMiddle=64, **kwargs):
        super(MNIST_CNN_PLLay, self).__init__(name=name, **kwargs)
        # self.layer1_1 = tf.keras.layers.Conv2D(32, 3, padding="same", activation='relu')
        # self.layer1_2 = tf.keras.layers.Conv2D(1, 3, padding="same", activation='relu')
        self.layer1_1 = tf.keras.layers.Conv2D(filters, kernel_size, padding="same", activation='relu')
        self.layer1_2 = tf.keras.layers.Conv2D(1, kernel_size, padding="same", activation='relu')
        # self.layer1_3 = TopoWeightLayer(32, m0=0.1, tseq=[v/10. for v in range(31)], KK=list(range(30)), by=1./13.5)
        # self.layer1_3 = TopoWeightLayer(unitsTopMiddle, m0=0.05, tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)), by=1./13.5)
        # self.layer1_4 = TopoWeightLayer(unitsTopMiddle, m0=0.2, tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)), by=1./13.5)
        self.layer1_3 = TopoFunLayer(unitsTopMiddle, grid_size=[28, 28], tseq=np.linspace(0.05, 0.95, 18), KK=list(range(3)))
        # self.layer2_1 = TopoWeightLayer(unitsTopInput, m0=0.05, tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)), by=1./13.5)
        # self.layer2_2 = TopoWeightLayer(unitsTopInput, m0=0.2, tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)), by=1./13.5)
        self.layer2_1 = GThetaLayer(unitsTopInput)
        self.layer2_2 = GThetaLayer(unitsTopInput)
        # self.layer3 = tf.keras.layers.Dense(32, activation='relu', name='dense_2') 
        self.layer3 = tf.keras.layers.Dense(unitsDense, activation='relu', name='dense_2') 
        self.layer4 = tf.keras.layers.Dense(10, name='predictions')

    def call(self, x):
        xg, xl1, xl2, xd = tf.split(x, [784, 100, 162, 8*nmax_diag], axis=-1)
        xg = tf.reshape(xg, [16, 28, 28, 1])
        xg1 = self.layer1_1(xg)
        xg1 = self.layer1_2(xg1)
        #print(x1.shape)
        xg1 = tf.reshape(xg1, [16, 784])
        xg1_1 = tf.nn.relu(self.layer1_3(xg1))
        # xg1_2 = tf.nn.relu(self.layer1_4(xg1))
        # xg1 = tf.concat((xg1, xg1_1, xg1_2), -1)
        xg1 = tf.concat((xg1, xg1_1), -1)
        xl1 = tf.nn.relu(self.layer2_1(xl1))
        xl2 = tf.nn.relu(self.layer2_2(xl2))
        x = tf.concat((xg1, xl1, xl2), -1)
        # x = xg1
        x = self.layer3(x)
        x = self.layer4(x)
        print(x.shape)
        return x


# class MNIST_CNN3(tf.keras.Model):
#   def __init__(self, name='mnistcnn3', filters=32, kernel_size=3, unitsDense=64, unitsTopInput=16, unitsTopMiddle=16, **kwargs):
#     super(MNIST_CNN3, self).__init__(name=name, **kwargs)
#     # self.layer1_1 = tf.keras.layers.Conv2D(32, 3, padding="same", activation='relu')
#     # self.layer1_2 = tf.keras.layers.Conv2D(1, 3, padding="same", activation='relu')
#     self.layer1_1 = tf.keras.layers.Conv2D(filters, kernel_size, padding="same", activation='relu')
#     self.layer1_2 = tf.keras.layers.Conv2D(1, kernel_size, padding="same", activation='relu')
#     # self.layer2_1 = DTMWeightWrapperLayer(m0=0.05, by=1./13.5) 
#     # self.layer2_2 = DTMWeightWrapperLayer(m0=0.2, by=1./13.5) 
#     self.layer3_1 = tf.keras.layers.Conv2D(filters, kernel_size, padding="same", activation='relu')
#     self.layer3_2 = tf.keras.layers.Conv2D(1, kernel_size, padding="same", activation='relu')
#     self.layer4_1 = tf.keras.layers.Conv2D(filters, kernel_size, padding="same", activation='relu')
#     self.layer4_2 = tf.keras.layers.Conv2D(1, kernel_size, padding="same", activation='relu')
#     # self.layer1_3 = TopoWeightLayer(32, m0=0.1, tseq=[v/10. for v in range(31)], KK=list(range(30)), by=1./13.5)
#     # self.layer1_3 = TopoWeightLayer(unitsTop, m0=0.05, tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)), by=1./13.5)Se
#     # self.layer1_4 = TopoWeightLayer(unitsTop, m0=0.2, tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)), by=1./13.5)
#     # self.layer3_3 = TopoFunLayer(unitsTopMiddle, grid_size=[28, 28], tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)))
#     # self.layer4_3 = TopoFunLayer(unitsTopMiddle, grid_size=[28, 28], tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)))
#     # self.layer5 = TopoFunLayer(unitsTopInput, grid_size=[28, 28], tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)))
#     # self.layer6 = TopoFunLayer(unitsTopInput, grid_size=[28, 28], tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)))
#     # self.layer3 = tf.keras.layers.Dense(32, activation='relu', name='dense_2') 
#     self.layer7 = tf.keras.layers.Dense(unitsDense, activation='relu', name='dense_2') 
#     self.layer8 = tf.keras.layers.Dense(10, name='predictions')

#   def call(self, x):
#     x1 = self.layer1_1(x)
#     x1 = self.layer1_2(x1)
#     x1 = tf.reshape(x1, [16, 784])
#     #print(x1.shape)
#     # x2 = tf.reshape(x, [16, 784])
#     # x2_1 = self.layer2_1(x2)
#     # x2_2 = self.layer2_2(x2)
#     # x3 = tf.reshape(x2_1, [16, 28, 28, 1])
#     x3 = x
#     x3 = self.layer3_1(x3)
#     x3 = self.layer3_2(x3)
#     x3 = tf.reshape(x3, [16, 784])
#     # x3 = tf.nn.relu(self.layer3_3(x3))
#     # x4 = tf.reshape(x2_2, [16, 28, 28, 1])
#     x4 = x
#     x4 = self.layer4_1(x4)
#     x4 = self.layer4_2(x4)
#     x4 = tf.reshape(x4, [16, 784])
#     # x4 = tf.nn.relu(self.layer4_3(x4))
#     # x5 = tf.nn.relu(self.layer5(x2_1))
#     # x6 = tf.nn.relu(self.layer6(x2_2))
#     # x = tf.concat((x1, x3, x4, x5, x6), -1)
#     x = tf.concat((x1, x3, x4), -1)
#     x = self.layer7(x)
#     x = self.layer8(x)
#     print(x.shape)
#     return x


class MNIST_CNN_PLLay_CnnTakesDtm(tf.keras.Model):
    def __init__(self, name='mnistcnnpllaycnntakesdtm', filters=32, kernel_size=3, unitsDense=64, unitsTopInput=16, unitsTopMiddle=16, **kwargs):
        super(MNIST_CNN_PLLay_CnnTakesDtm, self).__init__(name=name, **kwargs)
        # self.layer1_1 = tf.keras.layers.Conv2D(32, 3, padding="same", activation='relu')
        # self.layer1_2 = tf.keras.layers.Conv2D(1, 3, padding="same", activation='relu')
        self.layer1_1 = tf.keras.layers.Conv2D(filters, kernel_size, padding="same", activation='relu')
        self.layer1_2 = tf.keras.layers.Conv2D(1, kernel_size, padding="same", activation='relu')
        self.layer2_1 = DTMWeightWrapperLayer(m0=0.05, by=1./13.5) 
        self.layer2_2 = DTMWeightWrapperLayer(m0=0.2, by=1./13.5) 
        self.layer3_1 = tf.keras.layers.Conv2D(filters, kernel_size, padding="same", activation='relu')
        self.layer3_2 = tf.keras.layers.Conv2D(1, kernel_size, padding="same", activation='relu')
        self.layer4_1 = tf.keras.layers.Conv2D(filters, kernel_size, padding="same", activation='relu')
        self.layer4_2 = tf.keras.layers.Conv2D(1, kernel_size, padding="same", activation='relu')
        # self.layer1_3 = TopoWeightLayer(32, m0=0.1, tseq=[v/10. for v in range(31)], KK=list(range(30)), by=1./13.5)
        # self.layer1_3 = TopoWeightLayer(unitsTop, m0=0.05, tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)), by=1./13.5)Se
        # self.layer1_4 = TopoWeightLayer(unitsTop, m0=0.2, tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)), by=1./13.5)
        self.layer3_3 = TopoFunLayer(unitsTopMiddle, grid_size=[28, 28], tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)))
        self.layer4_3 = TopoFunLayer(unitsTopMiddle, grid_size=[28, 28], tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)))
        self.layer5 = TopoFunLayer(unitsTopInput, grid_size=[28, 28], tseq=np.linspace(0.06, 0.3, 25), KK=list(range(2)))
        self.layer6 = TopoFunLayer(unitsTopInput, grid_size=[28, 28], tseq=np.linspace(0.14, 0.4, 27), KK=list(range(3)))
        # self.layer3 = tf.keras.layers.Dense(32, activation='relu', name='dense_2') 
        self.layer7 = tf.keras.layers.Dense(unitsDense, activation='relu', name='dense_2') 
        self.layer8 = tf.keras.layers.Dense(10, name='predictions')

    def call(self, x):
        x1 = self.layer1_1(x)
        x1 = self.layer1_2(x1)
        x1 = tf.reshape(x1, [16, 784])
        #print(x1.shape)
        x2 = tf.reshape(x, [16, 784])
        x2_1 = self.layer2_1(x2)
        x2_2 = self.layer2_2(x2)
        x3 = tf.reshape(x2_1, [16, 28, 28, 1])
        # x3 = x
        x3 = self.layer3_1(x3)
        x3 = self.layer3_2(x3)
        x3 = tf.reshape(x3, [16, 784])
        x3 = tf.nn.relu(self.layer3_3(x3))
        x4 = tf.reshape(x2_2, [16, 28, 28, 1])
        # x4 = x
        x4 = self.layer4_1(x4)
        x4 = self.layer4_2(x4)
        x4 = tf.reshape(x4, [16, 784])
        x4 = tf.nn.relu(self.layer4_3(x4))
        x5 = tf.nn.relu(self.layer5(x2_1))
        x6 = tf.nn.relu(self.layer6(x2_2))
        x = tf.concat((x1, x3, x4, x5, x6), -1)
        # x = tf.concat((x1, x3, x4, -1)
        x = self.layer7(x)
        x = self.layer8(x)
        print(x.shape)
        return x

def mnist_eval(nTimes, corrupt_prob_list, noise_prob_list,
      x_processed_file_list, y_file, model_mlp_file_array,
      model_mlp_pllay_file_array, model_cnn_file_array,
      model_cnn_pllay_file_array, model_cnn_pllay_input_file_array,
      batch_size=16):

    print("nTimes = ", nTimes)

    accuracy_mlp = np.zeros(nTimes)
    accuracy_mlp_pllay = np.zeros(nTimes)
    accuracy_cnn = np.zeros(nTimes)
    accuracy_cnn_pllay = np.zeros(nTimes)
    accuracy_cnn_pllay_input = np.zeros(nTimes)

    (y_train, y_test) = np.load(y_file, allow_pickle=True)

    for iCn in range(nCn):
        start_time = time.time()
        print("--------------------------------------------------------------")
        print("Corruption rate = ", corrupt_prob_list[iCn])
        print("Noise rate = ", noise_prob_list[iCn])
        print("--------------------------------------------------------------") 
        (x_train_processed, x_test_processed) = np.load(
              x_processed_file_list[iCn], allow_pickle=True)
        test_dataset = to_tf_dataset(x=x_test_processed, y=y_test,
              batch_size=batch_size)

        for iTime in range(nTimes):

            # MLP
            start_time_inside = time.time()
            print("MLP")
            model_mlp = MNIST_MLP()
            model_mlp.compile(optimizer=tf.keras.optimizers.RMSprop(),  # Optimizer
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['sparse_categorical_accuracy'])
            model_mlp.load_weights(
                  model_mlp_file_array[iCn][iTime])
            accuracy_mlp[iTime] = model_mlp.evaluate(test_dataset)[1]
            print("--- %s seconds ---" % (time.time() - start_time_inside))

            # MLP + PLLay
            start_time_inside = time.time()
            print("MLP + PLLay")
            model_mlp_pllay = MNIST_MLP_PLLay()
            model_mlp_pllay.compile(optimizer=tf.keras.optimizers.RMSprop(),  # Optimizer
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['sparse_categorical_accuracy'])
            model_mlp_pllay.load_weights(
                  model_mlp_pllay_file_array[iCn][iTime])
            accuracy_mlp_pllay[iTime] = model_mlp_pllay.evaluate(
                  test_dataset)[1]
            print("--- %s seconds ---" % (time.time() - start_time_inside))

            # CNN
            start_time_inside = time.time()
            print("CNN")
            model_cnn = MNIST_CNN()
            model_cnn.compile(optimizer=tf.keras.optimizers.RMSprop(),  # Optimizer
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['sparse_categorical_accuracy'])
            model_cnn.load_weights(
                  model_cnn_file_array[iCn][iTime])
            accuracy_cnn[iTime] = model_cnn.evaluate(test_dataset)[1]
            print("--- %s seconds ---" % (time.time() - start_time_inside))

            # CNN + PLLay
            start_time_inside = time.time()
            print("CNN + PLLay")
            model_cnn_pllay = MNIST_CNN_PLLay()
            model_cnn_pllay.compile(optimizer=tf.keras.optimizers.RMSprop(),  # Optimizer
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['sparse_categorical_accuracy'])
            model_cnn_pllay.load_weights(
                  model_cnn_pllay_file_array[iCn][iTime])
            accuracy_cnn_pllay[iTime] = model_cnn_pllay.evaluate(
                  test_dataset)[1]
            print("--- %s seconds ---" % (time.time() - start_time_inside))

            # CNN + PLLay, input only
            start_time_inside = time.time()
            print("CNN + PLLay, input only")
            model_cnn_pllay_input = MNIST_CNN_PLLay_Input()
            model_cnn_pllay_input.compile(optimizer=tf.keras.optimizers.RMSprop(),  # Optimizer
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['sparse_categorical_accuracy'])
            model_cnn_pllay_input.load_weights(
                  model_cnn_pllay_input_file_array[iCn][iTime])
            accuracy_cnn_pllay_input[iTime] = model_cnn_pllay_input.evaluate(
                  test_dataset)[1]
            print("--- %s seconds ---" % (time.time() - start_time_inside))

        print("--------------------------------------------------------------")
        print("Corruption rate = ", corrupt_prob_list[iCn])
        print("Noise rate = ", noise_prob_list[iCn])
        print("--------------------------------------------------------------") 
        print("Accuracy for MLP : ", accuracy_mlp)
        print("Average Accuracy for MLP : ", sum(accuracy_mlp) / nTimes)
        print("Accuracy for MLP + PLLay :", accuracy_mlp_pllay)
        print("Average Accuracy for MLP + PLLay :",
              sum(accuracy_mlp_pllay) / nTimes)
        print("Accuracy for CNN :", accuracy_cnn)
        print("Average Accuracy for CNN :", sum(accuracy_cnn) / nTimes)
        print("Accuracy for CNN + PLLay :", accuracy_cnn_pllay)
        print("Average Accuracy for CNN + PLLay :",
              sum(accuracy_cnn_pllay) / nTimes)
        print("Accuracy for CNN + PLLay, input only :",
              accuracy_cnn_pllay_input)
        print("Average Accuracy for CNN + PLLay, input only :",
              sum(accuracy_cnn_pllay_input) / nTimes)

        print("--- %s seconds ---" % (time.time() - start_time))
        print("--------------------------------------------------------------")

# corrupt_prob_list = [0.1]
# noise_prob_list = [0.1]
corrupt_prob_list = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
noise_prob_list = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
nCn = len(corrupt_prob_list)
file_cn_list = [None] * nCn
for iCn in range(nCn):
    file_cn_list[iCn] = str(int(corrupt_prob_list[iCn] * 100)).zfill(2) + \
          '_' + str(int(noise_prob_list[iCn] * 100)).zfill(2)

x_processed_file_list = [None] * nCn
for iCn in range(nCn):
    x_processed_file_list[iCn] = (
          'mnist_x_processed_' + file_cn_list[iCn] + '.npy')
y_file = 'mnist_y.npy'

# nTimes=1
nTimes=10
model_mlp_file_array = [None] * nCn
model_mlp_pllay_file_array = [None] * nCn
model_cnn_file_array = [None] * nCn
model_cnn_pllay_file_array = [None] * nCn
model_cnn_pllay_input_file_array = [None] * nCn
for iCn in range(nCn):
    model_mlp_file_array[iCn] = [None] * nTimes
    model_mlp_pllay_file_array[iCn] = [None] * nTimes
    model_cnn_file_array[iCn] = [None] * nTimes
    model_cnn_pllay_file_array[iCn] = [None] * nTimes
    model_cnn_pllay_input_file_array[iCn] = [None] * nTimes
for iCn in range(nCn):
    for iTime in range(nTimes):
        file_time = str(iTime).zfill(2)
        model_mlp_file_array[iCn][iTime] = 'mnist_models/mlp_' + \
              file_cn_list[iCn] + '_' + file_time + '/model'
        model_mlp_pllay_file_array[iCn][iTime] = 'mnist_models/mlp_pllay_' + \
              file_cn_list[iCn] + '_' + file_time + '/model'
        model_cnn_file_array[iCn][iTime] = 'mnist_models/cnn_' + \
              file_cn_list[iCn] + '_' + file_time + '/model'
        model_cnn_pllay_file_array[iCn][iTime] = 'mnist_models/cnn_pllay_' + \
              file_cn_list[iCn] + '_' + file_time + '/model'
        model_cnn_pllay_input_file_array[iCn][iTime] = \
              'mnist_models/cnn_pllay_input_' + file_cn_list[iCn] + '_' + \
              file_time + '/model'

batch_size = 16

mnist_eval(nTimes=nTimes, corrupt_prob_list=corrupt_prob_list,
      noise_prob_list=noise_prob_list,
      x_processed_file_list=x_processed_file_list, y_file=y_file,
      model_mlp_file_array=model_mlp_file_array,
      model_mlp_pllay_file_array=model_mlp_pllay_file_array,
      model_cnn_file_array=model_cnn_file_array,
      model_cnn_pllay_file_array=model_cnn_pllay_file_array,
      model_cnn_pllay_input_file_array=model_cnn_pllay_input_file_array,
      batch_size=batch_size)