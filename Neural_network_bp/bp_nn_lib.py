# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 23:02:51 2018

@author: SW
summary:
This is a step by step BP neural network coding practice.

"""
import numpy as np
from scipy.special  import expit as sigmoid



# nerual network class definition
class neuralNetwork:
    
    # initializer
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        
        ## initialize learning rate
        self.lr = learningrate
        
        # create the activation function
        self.activation_function = lambda x: sigmoid(x)
        
        pass
    
    # train the nn model
    def train():
        pass
    
    # query the nerual network
    
    def query(self, inputs_list):
        # convert input ;ist to 2d aaary
        inputs = np.array(inputs_list, ndmin = 2).T
        hidden_inputs = np.dot(self.wih, inputs)
        
        hidden_outputs = self.activation_function(hidden_inputs)
        
        final_inputs = np.dot(self.who, hidden_outputs)
        
        final_outputs = self.activation_function(final_inputs)
        
        return final_outputs
    
    
    
## try some number
        
input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate = 0.2

## create an instance of the class
n_1 = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

np.array([[1], [2], [3], [56], [43], [33], [5], [6], [52]], ndmin = 2)

