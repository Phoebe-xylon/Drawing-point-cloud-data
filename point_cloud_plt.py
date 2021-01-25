import numpy as np
import scipy.io as scio
import time
import matplotlib.pyplot as plt
import sys
'''
# point cloud path of the source file
point_cloud_path = sys.argv[1]
# Directory to store the processed frames
dir = sys.argv[2]
'''
point_cloud_path = './data/seq1_001.mat'
dir='./output/'

data = scio.loadmat(point_cloud_path )
train=[]
train=(data['Img'])
size=train.shape
X=np.arange(0,size[0],1)
Y=np.arange(0,size[1],1)
X,Y=np.meshgrid(X,Y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
elev = 90.0
azim = 90.0
ax.view_init(elev, azim)
ax.scatter(X,  # x
            Y,  # y
            train,# z
            c=train,  # height data for color
            marker="x")
plt.savefig(dir + 'plot.png')
plt.show()