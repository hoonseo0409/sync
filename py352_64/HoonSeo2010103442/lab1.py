import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# create nodes in a graph
a = tf.constant(15, name="a")
b = tf.constant(61, name="b")

# add them
c = tf.add(a,b, name="c")
print(c)

# define inputs
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

'''TODO: Define the operation for c, d, e (use tf.add, tf.substract, tf.multiply).'''
c = tf.add(a,b)# TODO
d = tf.subtract(b,1)# TODO
e = tf.multiply(c,d)# TODO

with tf.Session() as session:
    a_data, b_data = 2.0, 4.0
    # define inputs
    feed_dict = {a: a_data, b: b_data}
    # pass data in and run the computation graph in a session
    output = session.run([e], feed_dict=feed_dict)
    print(output) # 18

