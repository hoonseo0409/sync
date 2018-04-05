import os
os._exit(00)

import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()
import tensorflow as tf

print(tf.add(1, 2))