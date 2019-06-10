from skimage import io
import numpy as np
import math
import matplotlib.pyplot as plt

def to_gray(img):
    w, h,_ = img.shape
    ret = np.empty((w, h), dtype=np.uint8)
    retf = np.empty((w, h), dtype=np.float)
    imgf = img.astype(float)
    retf[:, :] = ((imgf[:, :, 1] + imgf[:, :, 2] + imgf[:, :, 0])/3)
    ret = retf.astype(np.uint8)
    return ret

def radia_transform(img,w,h):
    shape = im.shape

    new_im = np.zeros(shape)
    print(shape)
    print(len(shape))
    print('w',w)
    print('h',h)
    width = shape[1]
    height = shape[0]
    lens = len(shape)
    for i in range(0,width):
	    xita = 2*3.14159*i/width
	    for a in range(0,height):
		    x = (int)(math.floor(a * math.cos(xita)))
		    y = (int)(math.floor(a * math.sin(xita)))
		    new_y = (int)(h+x)
		    new_x = (int)(w+y)
		    #print(h.dtype)
		    if new_x>=0 and new_x<width:
			    if new_y>=0 and new_y<height:
				    if lens==3:
					    new_im[a,i,0] = (im[new_y,new_x,0]-127.5)/128
					    new_im[a,i,1] = (im[new_y,new_x,1]-127.5)/128
					    new_im[a,i,2] = (im[new_y,new_x,2]-127.5)/128
				    else:
					    new_im[a,i] = (im[new_y,new_x]-127.5)/128
					    new_im[a,i] = (im[new_y,new_x]-127.5)/128
					    new_im[a,i] = (im[new_y,new_x]-127.5)/128
    return new_im

im = io.imread('E:/1.jpg')
im = to_gray(im)
h = im.shape[0]
w = im.shape[1]

new_im1 = radia_transform(im,(int)(w/2),(int)(h/2))

new_im2 = radia_transform(im,(int)(w/4),(int)(h/4))

new_im3 = radia_transform(im,(int)(w*0.5),(int)(h*0.75))


#io.imshow(im)
#io.imsave('E:/112.jpg',new_im3)
#io.show()


plt.figure(num='astronaut',figsize=(8,8))  

plt.subplot(2,2,1)     
plt.title('origin image')  
plt.imshow(im,plt.cm.gray)      

plt.subplot(2,2,2)    
plt.title('0.5')  
plt.imshow(new_im1,plt.cm.gray)     
plt.axis('off')    

plt.subplot(2,2,3)    
plt.title('0.25')  
plt.imshow(new_im2,plt.cm.gray)     
plt.axis('off')    

plt.subplot(2,2,4)    
plt.title('0.75')  
plt.imshow(new_im3,plt.cm.gray)     
plt.axis('off')     

plt.show()  
