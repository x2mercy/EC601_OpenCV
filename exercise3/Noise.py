#Copyright 2017 mengxi wang wmx@bu.edu
import cv2
import numpy as np

def addGaussianNoise(image,mean,sigma): 
    G_Noiseimg = image.copy()
    cv2.randn(G_Noiseimg,mean,sigma)
    cv2.add(image,G_Noiseimg,G_Noiseimg)
    return G_Noiseimg

def addPepperSalt(image,pa,pb):
    NoiseImg=image
    NoiseNum1=int(pa*image.shape[0]*image.shape[1])
    NoiseNum2=int(pb*image.shape[0]*image.shape[1])
    for i in range(NoiseNum1):
        randX=np.random.randint(0,image.shape[0]-1)
        randY=np.random.randint(0,image.shape[1]-1)
        NoiseImg[randX,randY]=0
    for i in range(NoiseNum2):
        randX=np.random.randint(0,image.shape[0]-1)
        randY=np.random.randint(0,image.shape[1]-1)
        NoiseImg[randX,randY]=255          
    return NoiseImg 

def boxfilter(image):
    filtered=cv2.boxFilter(image, -1, (3, 3))
    return filtered

def gaussfilter(image):
    filtered=cv2.GaussianBlur(image, (3,3), 1.5, 3) 
    return filtered

def medianfilter(image):
    filtered=cv2.medianBlur(image,5)
    return filtered
    
def main():
    mean=0
    sigma=20
    pa=0.01
    pb=0.01
    img=cv2.imread("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex3/Lenna.png")
    grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex3/gray.png",grayImage)


    gauss_noiseImage = addGaussianNoise(grayImage,mean,sigma)
    cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex3/gaussiannoise.png",gauss_noiseImage)
    boxfilter_img = boxfilter(gauss_noiseImage)
    cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex3/gauss_boxfilter.png",boxfilter_img)
    gaussfilter_img=gaussfilter(gauss_noiseImage)
    cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex3/gauss_gaussfilter.png",gaussfilter_img)
    medianfilter_img=medianfilter(gauss_noiseImage)
    cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex3/gauss_medianfilter.png",medianfilter_img)
    
    pepper_saltImage=addPepperSalt(grayImage,pa,pb)
    cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex3/psnoise.png",pepper_saltImage)
    boxfilter_img = boxfilter(pepper_saltImage)
    cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex3/ps_boxfilter.png",boxfilter_img)
    gaussfilter_img=gaussfilter(pepper_saltImage)
    cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex3/ps_gaussfilter.png",gaussfilter_img)
    medianfilter_img=medianfilter(pepper_saltImage)
    cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex3/ps_medianfilter.png",medianfilter_img)
    
if __name__ == "__main__":
    main()
