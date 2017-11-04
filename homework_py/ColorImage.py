#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:44:03 2017

@author: chenrui
"""
#    typedef struct CvMat
#    {
#        int type;    
#        int step;
#    
#        /* for internal use only */
#        int* refcount;
#        int hdr_refcount;
#    
#        union
#        {
#            uchar* ptr;
#            short* s;
#            int* i;
#            float* fl;
#            double* db;
#        } data;
import cv2
import numpy as np
def convert_ex(image_path):
    image = cv2.imread(image_path,1)
    cv2.namedWindow('Display Window')
    cv2.imshow('Display Window', image)
    print("size of image: ", image.shape) ## print size of image
#    cv2.waitKey(0) ## Wait for keystroke  用commind line运行可以关掉窗口！！！！！        
    # RGB
    (B, G, R) = cv2.split(image)
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    print('value at R(20,25):',R[20][25])
    print('value at G(20,25):',G[20][25])
    print('value at B(20,25):',B[20][25])
##---------------------------FOR FUN------------------------------------------------##    
    # just for fun
    zeros = np.zeros(image.shape[:2], dtype = "uint8")

    # split and merge will get what I had thought it should be
    cv2.imshow("Blue_3_channel", cv2.merge([B, zeros, zeros]))
    cv2.imshow("Green_3_channel", cv2.merge([zeros, G, zeros]))
    cv2.imshow("Red_3_channel", cv2.merge([zeros, zeros, R]))


##----------------------------YCrCb-------------------------------------------------##
#    res_Y = np.zeros(image.shape, np.uint8)
    res_Y=cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb) # HLS, HSV, YCrCb, ....
    cv2.imshow("CvtColor", res_Y)
    (Y, Cb, Cr) = cv2.split(res_Y)
    cv2.imshow("Y", Y)
    cv2.imshow("Cb", Cb)
    cv2.imshow("Cr", Cr)
    print('value at Y(20,25):',Y[20][25])
    print('value at Cb(20,25):',Cb[20][25])
    print('value at Cr(20,25):',Cr[20][25])
    
##-----------------------------HSV--------------------------------------------------##
#    res_H = np.zeros(image.shape, np.uint8)
    res_H=cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # HLS, HSV, YCrCb, ....
    cv2.imshow("CvtColor", res_H)
    (H, S, V) = cv2.split(res_H)
    cv2.imshow("Hue", H)
    cv2.imshow("Saturation", S)
    cv2.imshow("Value", V)
    print('value at H(20,25):',H[20][25])
    print('value at S(20,25):',S[20][25])
    print('value at V(20,25):',V[20][25]) 
##-------------------------value-range-of-channels-----------------------------------##    
    print('value range of R,G,B : 0~255')   
    print('value range of Y,U,V : 16~235,16~240,16~240')    
    print('value range of H,S,V : 0~180,0~255,0~255')
    print('value range of L,A,B : 0~100,-127~127,-127~127')
    print('value range of C,M,Y,K : 0~100')
    

    cv2.waitKey(0)
    cv2.destroyAllWindows() ## Destroy all windows
def main():
    image_path = "/Users/chenrui/Desktop/test/auditorium.jpg"
    convert_ex(image_path)
#    print(fft([0,1,2]))
#    print(np.fft.fft([0,1,2]))


if __name__ == '__main__':
  main()