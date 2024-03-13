# URL: https://neetcode.io/problems/basics-of-pytorch

# DESCRIPTION: PyTorch is the industry standard library for deep learning and was used to train ChatGPT. Checkout the first 9 minutes of this video for a summary of the basic functions.

# You will use built in PyTorch functions to manipulate tensors. These are important to understand before building more interesting & powerful neural networks.

# Your tasks:

#     Reshape an M×NM×N tensor into a (M⋅N // 2)×2(M⋅N//2)×2 tensor.
#     Find the average of every column in a tensor.
#     Combine an M×NM×N tensor and a M×MM×M tensor into a M×(M+N)M×(M+N) tensor.
#     Calculate the mean squared error loss between a prediction and target tensor.

# Inputs:

#     to_reshape - a tensor to reshape
#     to_avg - a tensor to average column wise
#     cat_one - the first tensor to concatenate
#     cat_two - the second tensor to concatenate
#     prediction - the output tensor of a model
#     target - the true labels for the model inputs


import torch
import torch.nn
from torchtyping import TensorType

# Helpful functions:
# https://pytorch.org/docs/stable/generated/torch.reshape.html
# https://pytorch.org/docs/stable/generated/torch.mean.html
# https://pytorch.org/docs/stable/generated/torch.cat.html
# https://pytorch.org/docs/stable/generated/torch.nn.functional.mse_loss.html

# Round your answers to 4 decimal places using torch.round(input_tensor, decimals = 4)

class Solution:
    def reshape(self, to_reshape: TensorType[float]) -> TensorType[float]:
        # torch.reshape() will be useful - check out the documentation
        M, N = to_reshape.shape
        reshaped = torch.reshape(to_reshape, (M * N // 2, 2))
        return torch.round(reshaped, decimals=4)

    def average(self, to_avg: TensorType[float]) -> TensorType[float]:
        # torch.mean() will be useful - check out the documentation
        avg = torch.mean(to_avg, 0)
        return torch.round(avg, decimals=4)

    def concatenate(self, cat_one: TensorType[float], cat_two: TensorType[float]) -> TensorType[float]:
        # torch.cat() will be useful - check out the documentation
        cat = torch.cat((cat_one, cat_two), 1)
        return torch.round(cat, decimals=4)
        
    def get_loss(self, prediction: TensorType[float], target: TensorType[float]) -> TensorType[float]:
        # torch.nn.functional.mse_loss() will be useful - check out the documentation
        mse_loss = torch.nn.functional.mse_loss(prediction, target)
        return torch.round(mse_loss, decimals=4)
