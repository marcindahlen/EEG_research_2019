from functools import reduce
from typing import Tuple

import tensorflow as tf
import numpy

from layers.ilayer import ILayer
from utils.utility import sigmoid, tanh


class LSTMLayer(ILayer):
    def __init__(self, in_shape: Tuple, out_shape: Tuple, size: int):
        self.outputs = None
        self.previous_outputs = None
        self.memories = None
        self.in_shape = in_shape
        self.out_shape = out_shape
        self.size = size
        self.weights = []

    def forward_pass(self, input) -> numpy.ndarray:
        input = tf.reshape(input, self.in_shape)
        input = numpy.append(input, [1])  # append bias
        if not self.previous_outputs:
            input = numpy.append(input, [0])  # append neutral 0 if no previous output present
        else:
            input = numpy.append(input, self.previous_outputs)
        input_gates = [numpy.matmul(input, self.weights[w][0]) for w in range(self.size)]
        input_gates = [numpy.sum(e) for e in input_gates]
        input_gates = [sigmoid(s) for s in input_gates]
        forget_gates = [numpy.matmul(input, self.weights[w][1]) for w in range(self.size)]
        forget_gates = [numpy.sum(e) for e in forget_gates]
        forget_gates = [sigmoid(s) for s in forget_gates]
        memory_gates = [numpy.matmul(input, self.weights[w][2]) for w in range(self.size)]
        memory_gates = [numpy.sum(e) for e in memory_gates]
        memory_gates = [numpy.delete(e, -1) for e in memory_gates]  # previous output not relevant in this gate
        memory_gates = [tanh(memory_gates) for s in forget_gates]
        self.memories = [forget_gates[cell] * self.memories[cell] +
                         input_gates[cell] * memory_gates[cell] for cell in range(self.size)]
        output_gates = [numpy.matmul(input, self.weights[w][3]) for w in range(self.size)]
        output_gates = [numpy.sum(e) for e in output_gates]
        output_gates = [numpy.delete(e, -1) for e in output_gates]  # previous output not relevant in this gate
        output_gates = [sigmoid(s) for s in output_gates]

        self.outputs = [tanh(self.memories[cell]) * output_gates[cell] for cell in range(self.size)]
        self.previous_outputs = self.outputs
        return self.outputs

    def get_all_weights(self) -> numpy.ndarray:
        pass

    def set_all_weights(self, new_weights):
        pass

    def decomposed_weights(self):
        pass

    def rebuild_weights(self, flat_weights):
        pass

    def init_weights(self, in_shape: Tuple, size: int) -> numpy.ndarray:
        self.in_shape = reduce(lambda x, y: x * y, in_shape)
        size = (size, 4, self.in_shape + 1 + 1)  # (no_of_neurons, no_of_gates, no_of_weights + bias + previous_out)
        return numpy.random.normal(loc=0, scale=0.25, size=size)
