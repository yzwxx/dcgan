import os
import sys
import scipy.misc
import pprint
import numpy as np
import time
import tensorflow as tf
import tensorlayer as tl
from tensorlayer.layers import *
from glob import glob
from random import shuffle
from model import *
from utils import *
from bird_test import *

pp = pprint.PrettyPrinter()

"""
load DCGAN to generate bird image.

Usage : run after running main_bird.py
"""

flags = tf.app.flags
flags.DEFINE_integer("batch_size", 64, "The number of batch images [64]")
flags.DEFINE_integer("output_size", 64, "The size of the output images to produce [64]")
flags.DEFINE_integer("sample_size", 64, "The number of sample images [64]")
flags.DEFINE_integer("c_dim", 3, "Dimension of image color. [3]")
flags.DEFINE_string("dataset", "CUB_200_2011", "The name of dataset")
flags.DEFINE_string("checkpoint_dir", "checkpoint", "Directory name to save the checkpoints [checkpoint]")
flags.DEFINE_string("sample_dir", "samples", "Directory name to save the image samples [samples]")
flags.DEFINE_boolean("is_train", False, "True for training, False for testing [False]")
FLAGS = flags.FLAGS

def main(_):
    # random noise vector
    z_dim = 100

    with tf.device("/gpu:0"):
        # ========================build the model=========================
        z = tf.placeholder(tf.float32, [FLAGS.batch_size, z_dim], name='z_noise')
        net_g, g_logits = generator_simplified_api(z, is_train=False, reuse=False)

    sess = tf.InteractiveSession()
    tl.layers.initialize_global_variables(sess)

    # model save_dir under checkpoint_dir
    model_dir = "%s_%s_%s" % (FLAGS.dataset, FLAGS.batch_size, FLAGS.output_size)
    save_dir = os.path.join(FLAGS.checkpoint_dir, model_dir)
    # net_g_name = os.path.join(save_dir, 'net_g.npz')
    # print(save_dir)

    # generate the random noise vector Z with size of (64,100)
    sample_seed = np.random.normal(loc=0.0, scale=1.0, size=(FLAGS.sample_size, z_dim)).astype(np.float32)

    # ==========================evaluate model===============================
    # load all parameters in the generator
    load_params = tl.files.load_npz(path=save_dir,name='/net_g.npz')
    # assign the parameters to customize your own network(net_g)
    tl.files.assign_params(sess, load_params, net_g)
    net_g.print_params(True)
    print(len(load_params))

    # generate images with random seed
    img = sess.run(net_g.outputs,feed_dict={z : sample_seed})
    save_images(img, [8, 8],'./{}/test.png'.format(FLAGS.sample_dir))
    print('finished')




if __name__ == '__main__':
    tf.app.run()
