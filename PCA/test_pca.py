#coding:utf-8
'''
Created on 2018年10月12日

@author:China
'''
import os
import os.path as op
import numpy as np
from sklearn.decomposition import PCA


def getdata(shape=[10, 14],low=0,high=100):
    #数据每一列为一个数据,行数就是数据的维数
    #默认10维度数据，14个数据
    tep=np.random.randint(low,high, shape)
    #tep=[[1,2,3],         [3,2,1]        ]
    return np.mat(tep)

def pca(mat):
    meanval=np.mean(mat, axis=1)
    mat=mat-meanval
    #------------------------------------------------
    '''
    np_cov=mat*(mat.T)/(mat.shape[-1]-1)
    print (np_cov)
    
    #print (np.sum(mat,axis=1))
    #利用numpy中寻找特征值和特征向量的模块linalg中的eig()方法
    #np_cov=np.cov(mat,rowvar=True)

    eigVals,eigVects=np.linalg.eigh(np_cov)
    print (eigVals)
    '''
    #-------------------------------------------------
    np_cov=np.cov(mat,rowvar=True)
    print (np_cov)
    eigVals,eigVects=np.linalg.eigh(np_cov)
    print (eigVals)
    

if __name__ == '__main__':
    pca(getdata())