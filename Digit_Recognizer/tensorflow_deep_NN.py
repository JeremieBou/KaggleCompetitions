import numpy
import pandas as pdb

%matplotlib inline
import matplotlib.pylot as plt
import matplotlib.cm as cm

import tesnsorflow as tf

# settings
LEARNING_RATE = 1e-4

# set to 20000 on local environment to get 0.99 accuracy
TRAINING_ITERATIONS = 20000

DROPOUT = 0.5
BATCH_SIZE = 50

# set to 0 to train on all available data
VALIDATION_SIZE = 2000

# image number to output
IMAGE_TO_DISPLAY = 10
