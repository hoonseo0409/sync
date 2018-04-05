

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

n_input_nodes = 2
n_output_nodes = 1
x = tf.placeholder(tf.float32, (None, n_input_nodes))
W = tf.Variable(tf.ones((n_input_nodes, n_output_nodes)), dtype=tf.float32)
b = tf.Variable(tf.zeros(n_output_nodes), dtype=tf.float32)

'''TODO: Define the operation for z (use tf.matmul).'''
z = tf.matmul(x, W) + b

'''TODO: Define the operation for out (use tf.sigmoid).'''
out = tf.sigmoid(z)

test_input = [[0.25, 0.15]]
graph=tf.Graph()
with tf.Session() as session:
    tf.global_variables_initializer().run(session=session)
    ''' TODO: Define the input'''
    feed_dict = {x: test_input} ## TODO
    ''' TODO: Run the session and get the output of the perceptron!'''
    output = session.run(out, feed_dict=feed_dict) ## TODO
    print(output[0]) # This should output 0.59868765.

import os
os._exit(00)



#os._exit(00) 호출에 의해 아래 코드가 실행되지 않으므로, 주석처리하였습니다. 만약 위의 코드의 실행을 보고 싶다면 주석 처리를 해제하면 됩니다만 그러면 아래 코드는 실행되지 않습니다.
"""
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()
import tensorflow as tf

print(tf.add(1, 2))

def f(x):
    # f(x) = x^2 + 3
    return tf.multiply(x, x) + 3

print( "f(4) = %.2f" % f(4.) )

# First order derivative
df = tfe.gradients_function(f)
print( "df(4) = %.2f" % df(4.)[0] )

# Second order derivative
d2f = tfe.gradients_function(lambda x: df(x)[0])
print( "d2f(4) = %.2f" % d2f(4.)[0] )

a = tf.constant(12)
counter = 0

while not tf.equal(a, 1):
  if tf.equal(a % 2, 0):
    a = a / 2
  else:
    a = 3 * a + 1
  print(a)
  
  """