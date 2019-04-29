import tensorflow.contrib.slim as sl
import tensorflow as tf

# Custom Layer
def upsample_and_concat(c1, c2, output_channels, in_channels):
    pool_size = 2
    dcf = tf.Variable(tf.truncated_normal([pool_size, pool_size, output_channels, in_channels], stddev=0.02))
    dc = tf.nn.conv2d_transpose(c1, dcf, tf.shape(c2), strides=[1, pool_size, pool_size, 1])

    output = tf.concat([dc, c2], 3)
    output.set_shape([None, None, None, output_channels * 2])

    return output

# Custom Activation
def leaky_relu(x):
    return tf.maximum(x * 0.2, x) 

# Network
def network(input_image):
    c1 = sl.conv2d(input_image, 32,[3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    c1 = sl.conv2d(c1, 32,[3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    p1 = sl.max_pool2d(c1, [2,2], padding='SAME')
# Unit 2
    c2 = sl.conv2d(p1, 64,[3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    c2 = sl.conv2d(c2, 64,[3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    p2 = sl.max_pool2d(c2, [2,2], padding='SAME')
# Unit 3
    c3 = sl.conv2d(p2, 128,[3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    c3 = sl.conv2d(c3, 128,[3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    p3 = sl.max_pool2d(c3, [2,2], padding='SAME')
# Unit 4
    c4 = sl.conv2d(p3, 256,[3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    c4 = sl.conv2d(c4, 256,[3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    p4 = sl.max_pool2d(c4, [2,2], padding='SAME')
# Unit 5
    c5 = sl.conv2d(p4, 512,[3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    c5 = sl.conv2d(c5, 512,[3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
# Unit 6
    uc6 = upsample_and_concat(c5,c4,256,512)
    c6 = sl.conv2d(uc6, 256, [3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    c6 = sl.conv2d(c6, 256, [3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
# Unit 7
    uc7 = upsample_and_concat(c6,c3,128,256)
    c7 = sl.conv2d(uc7, 128, [3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    c7 = sl.conv2d(c7, 128, [3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
# Unit 8
    uc8 = upsample_and_concat(c7,c2,64,128)
    c8 = sl.conv2d(uc8, 64, [3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    c8 = sl.conv2d(c8, 64, [3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
# Unit 9
    uc9 = upsample_and_concat(c8,c1,32,64)
    c9 = sl.conv2d(uc9, 32, [3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
    c9 = sl.conv2d(c9, 32, [3,3], activation_fn=leaky_relu, weights_regularizer=sl.l2_regularizer(0.001))
# Final Unit
    c10 = sl.conv2d(c9, 12, [1,1], activation_fn=None)
    output_image = tf.depth_to_space(c10,2)
    return output_image

