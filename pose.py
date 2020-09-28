# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:41:50 2019

@author: richardg71
"""

import argparse
import logging
import time

import cv2
import numpy as np

from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh
