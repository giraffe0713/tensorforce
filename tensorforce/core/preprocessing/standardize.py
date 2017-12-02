# Copyright 2017 reinforce.io. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
from tensorforce import util
from tensorforce.core.preprocessing import Preprocessor


class Standardize(Preprocessor):
    """
    Standardize state. Subtract mean and divide by standard deviation.
    """

    def __init__(self, across_batch=False):
        self.across_batch = across_batch

    def process(self, state):
        if self.across_batch:
            axes = np.arange(0, util.rank(state))
        else:
            axes = np.arange(1, util.rank(state))
        mean, variance = tf.nn.moments(x=state, axes=axes)
        return (state - mean) / tf.maximum(x=variance, y=util.epsilon)
