# Decrypted

print("init")
import matplotlib, sys, os, \
    glob, cPickle, scipy, \
    argparse, errno, json, \
    copy, re, time, imp, datetime, \
    cv2, logging

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os.path as osp
import scipy.io as sio

from pprint import pprint
import subprocess

# _shell_cmd = "rm -f __init__.pyc init.pyc load_transfer_data.pyc  net2net.pyc"
# if subprocess.call(_shell_cmd.split()) == 0:
#     print("reload")

keras_backend = "tensorflow"  # tensorflow
gpu = True
if keras_backend == "theano":
    _shell_cmd = "cp /home/xlwang/.keras/keras.json.th /home/xlwang/.keras/keras.json"
    if subprocess.call(_shell_cmd.split()) == 0: print("using keras backend theano")
    if not gpu:
        _shell_cmd = "cp /home/xlwang/.theanorc.cpu /home/xlwang/.theanorc"
        if subprocess.call(_shell_cmd.split()) == 0: print("using cpu")
        os.environ['THEANO_FLAGS'] = \
            "floatX=float32,device=cpu," \
            "fastmath=True,ldflags=-lopenblas"
    else:
        _shell_cmd = "cp /home/xlwang/.theanorc.gpu /home/xlwang/.theanorc"
        if subprocess.call(_shell_cmd.split()) == 0: print("using gpu")
else:
    _shell_cmd = "cp /home/xlwang/.keras/keras.json.tf /home/xlwang/.keras/keras.json"
    if subprocess.call(_shell_cmd.split()) == 0: print("using keras backend tf")

# def add_path(path):
#     if path not in sys.path:
#         sys.path.insert(0, path)
# run_root = os.getcwd()
root_dir = osp.normpath(
    osp.join(osp.dirname(__file__), "..")
)

with_caffe = False
if with_caffe == True:
    if os.path.isfile("/home/luzai/luzai/luzai"):
        caffe_root = "/home/luzai/App/caffe"
    elif os.path.exists("/home/vipa"):
        caffe_root = "/home/luzai/App/caffe"
    else:
        caffe_root = input("input your caffe root")
    os.chdir(caffe_root + "/python")
    sys.path.insert(0, caffe_root + "/python")
    print(sys.path)
    try:
        import caffe
        # caffe = imp.load_source('caffe', '/home/luzai/App/caffe/python')
    except Exception as inst:
        print(inst)
    finally:
        pass
        os.chdir(root_dir)

import keras
from keras.callbacks import ReduceLROnPlateau, CSVLogger, EarlyStopping
from keras.datasets import cifar10
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Input, Dropout, Activation, BatchNormalization, \
    Embedding, MaxPool2D, MaxPooling1D, AveragePooling2D
from keras.models import Sequential, model_from_json, Model
from keras.optimizers import SGD
from keras.utils import np_utils, vis_utils
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K

print("\n------------------------------\n")
