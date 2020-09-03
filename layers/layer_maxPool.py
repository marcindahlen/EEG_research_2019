import tensorflow
import numpy

from layers.ilayer import ILayer


class MaxPool(ILayer):
    def __init__(self):
        self.output = None
        self.in_shape = None
        self.out_shape = None
        self.weights = None

    def forward_pass(self, input):
        self.in_shape = len(numpy.shape(input))

        if self.in_shape == 1:
            self.output = input[None][:, :, None]
            self.output = tensorflow.nn.max_pool1d(self.output, 5, 5, padding='SAME')
        elif self.in_shape == 3:
            self.output = input[None][:, :, None]
            self.output = tensorflow.nn.max_pool1d(self.output, [5, 5, 5], [5, 5, 5], padding='SAME')
        else:
            raise Exception("Invalid input shape in AvgPool layer: " + str(self.in_shape))

        return self.output