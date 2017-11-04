# OpenCVExercise
## Exercise one
1. How does a program read the cvMat object, in particular, what is the
order of the pixel structure?       <br />
## Exercise two
1. ColorImage.cpp is a program that takes a look at colorspace conversions in OpenCV. Run the code in ColorImage.cpp and comment on the outputs. Implement the same thing in Python and save each image.  <br />

The only thing different from what I thought is the image of Channel R,G,B 
I think the image of R channel should be a image contains only red, and the same for the G and B. But what the code gave me is three gray images. Then I try another kind of thing that set other two channel to zeros but make red/green/blue remain what they are and I get what I want.


2. Print out the values of the pixel at (20,25) in the RGB, YCbCr and HSV versions of the image. What are the ranges of pixel values in each channel of each of the above mentioned colorspaces? <br />

``` python
('value at R(20,25):', 153)
('value at G(20,25):', 215)
('value at B(20,25):', 252)
('value at Y(20,25):', 201)
('value at Cb(20,25):', 94)
('value at Cr(20,25):', 157)
('value at H(20,25):', 101)
('value at S(20,25):', 100)
('value at V(20,25):', 252)
value range of R,G,B : 0~255
value range of Y,U,V : 16~235,16~240,16~240
value range of H,S,V : 0~180,0~255,0~255
value range of L,A,B : 0~100,-127~127,-127~127
value range of C,M,Y,K : 0~100
```


## Exercise three
1. Look at the code in Noise.cpp and implement the code in Python. Also, print the results for di↵erent noise values in the Gaussian case, mean = 0, 5, 10, 20 and sigma = 0, 20, 50, 100 and for the salt-and-pepper case, pa = 0.01, 0.03, 0.05, 0.4 and pb = 0.01, 0.03, 0.05, 0.4. <br />

2. Change the kernel sizes for all the filters with all di↵erent values for noises and print the results for 3x3, 5x5 and 7x7 kernels. Comment on the results. Which filter seems to work ”better” for images with salt-and-pepper noise and gaussian noise?<br />

with the increase of the kernel size, the image will become more blurring;Median filter works better for images with salt-and-pepper noise.Gaussian filter works better for images with gaussian noise.<br />

## Exercise four
1.Look at Threshold.cpp and implement the code in Python, and observe the results for di↵erent threshold values. Comment on the results. <br />

it is easy to understand the Truncate/Binary/Binary_inv. And for the band filter, what the code do is to make f(x) = maxval (27<f(x)<125) and f(x) = 0 (otherwise); do not really understand what the semi filter do. and the algorithm of Adaptive filter calculate the threshold for a small regions of the image. So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.<br />

2.What are the disadvantages of binary threshold?<br />

it may not be good in all the conditions where image has different lighting conditions in different areas.<br />

3.When is Adaptive Threshold useful?<br />

when image has different lighting conditions in different areas







