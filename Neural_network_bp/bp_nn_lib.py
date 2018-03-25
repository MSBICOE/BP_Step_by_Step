# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 23:02:51 2018

@author: shang
summary:
"""

# nerual network class definition
class neuralNetwork:
    
    # initializer
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        ## initialize learning rate
        self.lr = learningrate
        pass
    
    # train the nn model
    def train():
        pass
    
    # query the nerual network
    
    def query():
        pass
    
    
    
## try some number
        
input_nodes = 3
hidden_nodes = 3
output_nodes = 3
learning_rate = 0.2

## create an instance of the class
n_1 = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
