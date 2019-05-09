# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:54:46 2019

@author: Lahiru D. Chamain
"""
import numpy as np
from numpy.linalg import inv

def getTcdf97(height):
    """
    returns the square matrix A and A^T with dimention-height.
    """
    a1 = -1.586134342
    a2 = -0.05298011854
    a3 = 0.8829110762
    a4 = 0.4435068522

    # Scale coeff:
    k1 = 0.8128662109 # 1/1.230174104914 // 0,2,4,6
    k2 = 0.6149902344 # 1.230174104914/2 // 5038 1,3,5,7
    X1 = np.identity(height)
    X2 = np.identity(height)
    X3 = np.identity(height)
    X4 = np.identity(height)
    X5 = np.zeros((height,height)).astype('float32')
    for col in range(1,height-2,2):
        X1[col-1,col]=X1[col+1,col]=a1
    X1[height-2,height-1] = 2*a1
    
    #print(X1)
    for col in range(2,height-1,2):
        X2[col-1,col]=X2[col+1,col]=a2
    X2[1,0] = 2*a2
    #print(X2)
    for col in range(1,height-2,2):
        X3[col-1,col]=X3[col+1,col]=a3
    X3[height-2,height-1] = 2*a3
    
    #print(X1)
    for col in range(2,height-1,2):
        X4[col-1,col]=X4[col+1,col]=a4
    X4[1,0] = 2*a4
    
    for col in range(0,height,1):
        if(col%2==0 ):
            #print(col)
            X5[col,int(col/2)]=k1
        else:
            X5[col,int(height/2 + (col-1)/2)]=k2
    #print(X3)
    X =np.matmul(np.matmul(np.matmul(np.matmul(X1,X2),X3),X4),X5)
    return X,inv(X)