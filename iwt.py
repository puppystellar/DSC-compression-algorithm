# author : lgy
# date : 2022.6.27
# decription : IWT(integer wavelet transform) to get the processed image to get better result
# Copyright (c) 2021-2022 ISILab.Co.Ltd

import cv2
import os
import math
from matplotlib.colors import rgb2hex
import numpy as np
import datetime
from PIL import Image
import sys 
import shapeFinding 
import imgProcessing
import numpy as np
np.set_printoptions(threshold=np.inf)


def SDecompose(img, dim1, dim2):
    # dim1: length
    # dim2: width
    img_der1, img_dec1 = decompose(img, dim1, dim2)
    # img_der: 行变换之后的结果， img_dec：再经过列变换之后的结果
    #img_der2, img_dec2 = decompose(img_dec1, int(dim1/2), int(dim2/2))
    #img_der3, img_dec3 = decompose(img_dec2, int(dim1/4), int(dim2/4))
    #img_der4, img_dec4 = decompose(img_dec3, int(dim1/8), int(dim2/8))
    #img_der5, img_dec5 = decompose(img_dec4, int(dim1/16), int(dim2/16))
    
    return img_der1, img_dec1



def decompose(img, dim1, dim2):

    
    # 对每一行和列交替进行一次S分解变换，dim1是图像长度（行维度），dim2是图像宽度（列维度）
    imgder = img
    imgdec = img

    # step1: row transform
    for i in range(dim2):
        # 1-128
        for j in range(0,dim1,2):
            print(i,j)
            # calculate the later part of the row ,Dj-1,k
            imgder[i, int(dim1/2+(j-1)/2)] = img[i-1, j] - img[i, j]
            # calculate the former part of the row, Sj-1,k
            imgder[i, int((j-1)/2)] = img[i, j] + np.floor(imgder[i, int(dim1/2+(j-1)/2)] /2)
    
    # step2: column transform
    for i in range(0, dim1-1):
        for j in range(0, dim2-1, 2):
            imgdec[int(dim2/2+(j)/2),i] = imgder[j+1,i] - imgder[j,i]
            imgdec[int((j)/2), i] = imgder[j,i] + np.floor(imgdec[int(dim2/2+(j)/2),i]/2)
    
    return imgder, imgdec

if __name__ == '__main__':
    print('start IWT transforming')
    start = datetime.datetime.now()
    dataset = 'datasetpath'
    input_dir = ['yourpath1','yourpath2']
    output_dir = ['train', 'test', 'iwt']

    num = 0  # image number
    imgProcessing.dir_check(output_dir[2], empty_flag=True)
    for f in os.listdir(input_dir[0]):
        num += 1
        img_path = os.path.join(input_dir[0], f)  # image path
        
        img = cv2.imread(img_path)  # read the image
        img = img.astype(np.int16)
        #b, g, r = cv2.split(img)  # split the image
        #y, u, v = shapeFinding.BGRtoYUV(b, g, r)
        '''
        y1 = shapeFinding.new_represent(y)
        y1 = y1.astype(np.int16)
        y2 = shapeFinding.new_represent2(y)
        y2 = y2.astype(np.int16)
        cv2.imwrite(os.path.join(output_dir[2], '%d_pre1.png' % num), y1)
        cv2.imwrite(os.path.join(output_dir[2], '%d_pre2.png' % num), y2)
        '''
        img1, img2= SDecompose(img,256,256)
        #img2= SDecompose(y2,256,256)
        cv2.imwrite(os.path.join(output_dir[2], '%d_iwt1.png' % num), img1)
        cv2.imwrite(os.path.join(output_dir[2], '%d_iwt2.png' % num), img2)
        #cv2.imwrite(os.path.join(output_dir[2], '%d_iwt2.png' % num), img2)
        print(str(num)+' images has been IWT transformed and save in folder')
    end = datetime.datetime.now()
    print('encoding time consuming:',end-start)
