'''
descirbe:

'''

import os
import shutil
import cv2
import math
import numpy as np
import datetime
from PIL import Image
import sys
import shapeFinding

def dir_check(filepath, print_flag=True, empty_flag=False):
    """
    Empty all contents in the folder
    :param filepath: input file path
    :param empty_flag: empty flag
    :param print_flag: print flag
    :return: None
    """
    if os.path.exists(filepath) and empty_flag:
        del_file(filepath)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    if print_flag:
        print('%s folder has been emptied and recreated' % filepath)

def del_file(filepath):
    """
    Empty all contents in the folder
    :param filepath: input file path
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def imgProcessing(dataset):
    # Process the dataset
    if dataset == 'PH2':  # drive dataset
        print('PH2 dataset is preprocessing')
        # input and output folder
        # D:\python_project\gray\Dataset\MNIST\Test
        # input_dir = ['D:\Data\\UCMerced_LandUse\Images\Train', 'D:\Data\\UCMerced_LandUse\Images\Test']
        # input_dir = ['D:\Data\\NWPU_VHR-10_dataset\Train', 'D:\Data\\NWPU_VHR-10_dataset\Test']
        input_dir = ['D:\Data\\NWPU_RESISC45dataset\\45dataset\Train',
                     'D:\Data\\retina-unet-master\DRIVE\\training\images']
        # \N 会有歧义
        output_dir = ['train', 'test']
        # Empty the output folder
        dir_check(output_dir[0], empty_flag=True)
        dir_check(output_dir[1], empty_flag=True)
        num = 0  # image number
        
        #train
        for f in os.listdir(input_dir[0]):
            img_path = os.path.join(input_dir[0], f)  # image path
            # 用来读取ppm格式文件
            # 可以直接读取转化成png格式
            '''
            if f[-4:] == '.ppm':
                print('shifting from ppm to png')
                img = Image.open(img_path)
                newname = img_path[:-4] + '.png'
                img.save(newname)
            '''
            img = cv2.imread(img_path)  # read the image
            cv2.imwrite(os.path.join(output_dir[0], '%d.png' % num), img)  # save the image
            num = num + 1
        '''
        # 将训练集图片降采样之后放入训练集中
        img_path_list = os.listdir(input_dir[0])
        img_path_list = img_path_list[0:round(len(img_path_list) * 0.5)]
        for path in img_path_list:
            img_path = os.path.join(input_dir[0], path)  # image path
            img = cv2.imread(img_path)  # read the image
            img = cv2.pyrDown(img)
            cv2.imwrite(os.path.join(output_dir[0], '%d.png' % num), img)  # save the image
            num = num + 1
        '''
        num_train = num
        print(str(num_train) + 'images have been saved in train folder.')

        #test
        for f in os.listdir(input_dir[1]):
            img_path = os.path.join(input_dir[1], f)  # image path
            img = cv2.imread(img_path)  # read the image
            cv2.imwrite(os.path.join(output_dir[1], '%d.png' % num), img)  # save the image
            num = num + 1
        '''
        #将原有test数据集的70%剪裁后放入测试集中
        img_path_list = os.listdir(input_dir[1])
        img_path_list = img_path_list[0:round(len(img_path_list) * 0.7)]
       
        for path in img_path_list:
            img_path = os.path.join(input_dir[1], path)  # image path
            img = cv2.imread(img_path)  # read the image
            img = cv2.resize(img, (200, 200))  # resize
            cv2.imwrite(os.path.join(output_dir[1], '%d.png' % num), img)  # save the image
            num = num + 1
        '''

        # test rough
        '''
        for f in os.listdir(input_dir[1]):
            img_path = os.path.join(input_dir[1], f)  # image path
            img = cv2.imread(img_path)  # read the image
            img = img.astype(np.int16)
            b, g, r = cv2.split(img)  # split the image
            y, u, v = shapeFinding.BGRtoYUV(b, g, r)  # mapping from bgr to yuv
            
            img_y = shapeFinding.new_represent(y)
            img_y = img_y % math.pow(2, 4)
            img_y = img_y.astype(np.int16)
            img_u = shapeFinding.new_represent(y)
            img_u = img_u % math.pow(2, 4)
            img_u = img_u.astype(np.int16)
            img_v = shapeFinding.new_represent(y)
            img_v = img_v % math.pow(2, 4)
            img_v = img_v.astype(np.int16)
            cv2.imwrite(os.path.join(output_dir[2], '%d_y.png' % num), img)  # save the image
            cv2.imwrite(os.path.join(output_dir[2], '%d_u.png' % num), img)
            cv2.imwrite(os.path.join(output_dir[2], '%d_v.png' % num), img)
            num = num + 1
        '''
        num_test = num - num_train
        print(str(num_test) + 'images have been saved in test folder.')    
    else:
        raise NameError('Input dataset does not exist')
    
if __name__ == '__main__':     
    print('start imgprocessing')
    dataset = 'PH2'
    imgProcessing(dataset)
    print('ending')

